# Metodología

## Fuente de datos

Toda la evidencia proviene de **dos fuentes públicas de ONPE** consultadas vía su API REST oficial:

1. **Endpoint de búsqueda por mesa**:
   `https://resultadoelectoral.onpe.gob.pe/presentacion-backend/actas/buscar/mesa?codigoMesa={CODIGO}&idEleccion=10`

   Devuelve los datos del resultado (totales, votos por partido, estado del acta), un array `lineaTiempo` con el historial de estados de la mesa, y referencias a los archivos asociados.

2. **Endpoint de archivo (PDF del acta)**:
   `https://resultadoelectoral.onpe.gob.pe/presentacion-backend/actas/file?id={ARCHIVO_ID}`

   Devuelve una URL pre-firmada (S3) desde la cual se descarga el PDF del acta.

## El timestamp de "publicación" — IMPORTANTE

El campo correcto que indica **cuándo ONPE marcó una mesa como Contabilizada** (es decir, cuándo el resultado se hizo público en su sistema) es:

```
data[0].lineaTiempo[i].fechaRegistro    donde lineaTiempo[i].codigoEstadoActa == "C"
```

Este campo es un timestamp epoch en milisegundos (UTC).

**Por qué este campo y no otros**:

1. `lineaTiempo` es el historial de **cambios de estado** de la mesa, devuelto por la API pública en el mismo endpoint que un usuario consulta.
2. Cuando el estado pasa a `C` (Contabilizada), la mesa **aparece en los conteos públicos** de ONPE.
3. Empíricamente, el `fechaRegistro` del estado `C` coincide casi exactamente con el momento en que el AGENTE AUTOMATIZADO STAE firma el PDF (73.2% de los casos dentro de ±5 minutos), lo que es coherente con que el agente firma cuando el sistema procesa la transmisión.

### Errata: corrección de métrica

Una versión inicial de este análisis usó otro campo, `daudFechaCreacion`, que es un atributo del **archivo adjunto** (no del estado de la mesa). Ese campo refleja un timestamp administrativo del registro del adjunto y NO el momento de publicación.

**Diferencia observada en las 361 mesas inicialmente analizadas**:
- Para muchas digitales: `daudFechaCreacion` ocurría DESPUÉS del `fechaRegistro` real (mediana +1.10 horas)
- Para algunas escaneadas: `daudFechaCreacion` ocurría DÍAS antes del `fechaRegistro` real (hasta -97.93h)

La corrección eliminó completamente el "Nivel 1" (12 mesas escaneadas) que parecían tener brecha pero no la tenían cuando se medía con `fechaRegistro`. También afinó el "Nivel 2" digital, descartando 12 mesas que no cumplían el criterio estricto, dejando 337 mesas con anomalía confirmada.

## Cómo se calcula la brecha

```python
fr = datetime.fromtimestamp(fechaRegistro_ms / 1000, tz=timezone.utc)  # publicación

# Para cada firma humana en el PDF:
delta_h = (signing_time_utc - fr).total_seconds() / 3600  # horas

# Mesa se incluye en la denuncia si:
all(delta_h > 0.1 for human in humanos)  # TODAS las firmas humanas son >6 min después
```

Umbral de 0.1h (6 minutos) para descartar coincidencias de timing dentro del margen de error.

## Verificación de integridad de los timestamps

### El `creation_date` del PDF NO cambia con la descarga

Para asegurarnos de que el `creation_date` del PDF es el original (no algo que ONPE re-genera al servir cada descarga), hicimos dos descargas separadas en el tiempo de las mismas mesas y comparamos:

- SHA-256 byte-a-byte: idéntico en ambas descargas
- `creation_date` interno: idéntico
- Tamaño del archivo: idéntico

Conclusión: ONPE sirve **archivos estáticos**.

### El parsing de timezones

- **PDF `/CreationDate`** usa formato `D:YYYYMMDDHHMMSS-HH'MM'` con timezone explícito (siempre `-05'00'` = Lima).
  Ejemplo: `D:20260413120614-05'00'` → `2026-04-13T17:06:14+00:00 UTC`

- **`fechaRegistro`** viene en epoch milliseconds UTC.
  Ejemplo: `1776045741000` → `2026-04-13T02:02:21+00:00 UTC` = `2026-04-12 21:02:21 (Lima)`

## Análisis de firmas digitales

Cada PDF digital tiene **objetos `/Type /Sig`** con un blob PKCS#7/CMS (`/Contents <hex>`) que contiene:
- Certificado X.509 del firmante
- Firma criptográfica del contenido
- Timestamp `/M` con el momento de firma

Extraemos cada objeto y parseamos:
- `/Name`: nombre del firmante (a veces incluye DNI)
- `/Reason`: motivo declarado de la firma
- `/M`: timestamp de firma (formato PDF date string, inmanipulable sin invalidar la firma)
- `/Contents`: PKCS#7 SignedData → de ahí extraemos los certificados X.509

Los certificados X.509 nos permiten identificar:
- **Subject CN**: nombre completo del firmante
- **Subject 2.5.4.5**: DNI peruano (formato `PNOPE-XXXXXXXX`)
- **Issuer**: autoridad certificadora (debe ser cadena ECEP-ONPE)

### Distinción agente vs humano

Una firma se clasifica como del **AGENTE AUTOMATIZADO STAE** si:
- `/Name` está vacío, O
- `/Reason` contiene "agente automatizado"

El certificado del agente tiene `CN=AGENTE AUTOMATIZADO STAE` y un OU institucional (no es persona).

### Patrón normal documentado por ONPE para EG2026

Fuente primaria: `Cartilla-Personeros_STAE_EG2026.pdf` (incluida en este repo, generada el 26 enero 2026 por ONPE).

Fase ESCRUTINIO (página 18 de la cartilla):
> "Presenciar que los **miembros de mesa firmen digitalmente** las actas de escrutinio.
> Firmar digitalmente (si lo desea) las actas de escrutinio.
> Presenciar **la impresión de las actas de escrutinio y del 'Cartel de resultados'**."

Fase TRANSMISIÓN (página 19 de la cartilla):
> "Presenciar, únicamente desde el área de observación del punto de transmisión, **el envío de los resultados de la mesa** en la que se encuentra acreditado."

El orden temporal es explícito y secuencial:
1. Miembros de mesa firman digitalmente actas de escrutinio
2. Se imprimen las actas físicas + cartel de resultados
3. **Recién después** se transmiten los resultados a ONPE

La cartilla **NO documenta** la existencia de un "Agente Automatizado STAE" como firmante. Solo se mencionan firmas humanas (miembros de mesa y personeros opcionales).

### Patrón anómalo detectado en 337 mesas (todas LIMA o CALLAO)

1. Cierre de mesa
2. Agente automatizado STAE firma (no documentado en la cartilla)
3. Estado de la mesa pasa a `C` (Contabilizada) — `fechaRegistro` registrado
4. ONPE publica el resultado en su web pública
5. **HORAS DESPUÉS** (mediana +4.07h, máximo +14.50h): los miembros de mesa firman digitalmente con sus certificados personales

Esto invierte el orden documentado en la cartilla: en lugar de **firma → transmisión**, observamos **transmisión → firma**.

## Filtro de inclusión de mesas

Las 337 mesas incluidas cumplen **TODOS** estos criterios:

1. Acta digital (no escaneada)
2. Tienen al menos una firma humana en el PDF (con DNI peruano en su certificado X.509)
3. **TODAS** las firmas humanas tienen timestamp `/M` posterior a `fechaRegistro` (estado C) por **más de 6 minutos**
4. Tienen `lineaTiempo` con al menos una entrada en estado `C`

Las 12 mesas evaluadas pero NO incluidas están preservadas en `mesas_descartadas/` con un archivo `DESCARTE_RAZON.txt` que documenta por qué no cumplieron el criterio.

## Renders visuales (eliminados)

Una versión inicial incluía PNG renders de actas escaneadas. Como Nivel 1 fue eliminado tras la corrección de métrica, los renders también se eliminaron por dejar de ser relevantes para esta denuncia.

## Reproducibilidad

Cualquier persona con conexión a Internet puede reproducir esta evidencia:

```bash
git clone <este-repo>
cd denuncia
pip install cryptography pymupdf httpx asyncpg
python scripts/verify_manifest.py    # verifica que los archivos no fueron alterados
```

Para reconstruir desde cero:

```bash
# Asume tener el dataset previo de ULTRON con los PDFs descargados
python scripts/build_evidence.py             # construye el repositorio inicial
python scripts/recompute_with_fechaRegistro.py  # aplica la métrica correcta
```

El script consulta la misma API ONPE pública. Si ONPE no ha alterado sus datos, el resultado debe ser idéntico al checked-in. Si ONPE alteró sus datos, las diferencias quedan documentadas y son evidencia adicional.
