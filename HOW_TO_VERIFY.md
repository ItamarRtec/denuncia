# Cómo verificar esta evidencia (independientemente)

Esta evidencia está diseñada para que **cualquier persona** la verifique sin tener que confiar en nosotros. Hay cuatro niveles de verificación:

## Nivel A — Verificación rápida (3 minutos)

Para cualquier mesa del listado:

1. Abrí `EVIDENCE_INDEX.csv` y elegí una fila — por ejemplo Mesa **039957**
2. Andá a https://resultadoelectoral.onpe.gob.pe
3. Buscá la mesa por su código
4. Verificá que ONPE muestre los mismos datos:
   - Estado: Contabilizada
   - Total de votos coincide con la columna `votos_validos`
   - Local de votación coincide
5. Descargá el PDF del acta desde la web ONPE
6. Comparalo contra `mesas_anomalas/<codigo_mesa>/acta.pdf` — los SHA-256 deben ser idénticos
7. Para verificar el SHA-256:

   En Windows:
   ```cmd
   certutil -hashfile "ruta\al\acta.pdf" SHA256
   ```

   En Linux/Mac:
   ```bash
   shasum -a 256 acta.pdf
   ```

## Nivel B — Verificación de la inconsistencia temporal (5 minutos)

Para una mesa cualquiera (ej. Mesa 039957):

### Paso 1: obtener el momento de publicación (`fechaRegistro`)

```bash
curl "https://resultadoelectoral.onpe.gob.pe/presentacion-backend/actas/buscar/mesa?codigoMesa=039957&idEleccion=10"
```

En la respuesta, buscar `data[0].lineaTiempo`. Es un array; encontrar la entrada con `codigoEstadoActa = "C"` y mirar su campo `fechaRegistro` (epoch milliseconds UTC).

Convertir a hora legible:
- En Linux/Mac: `date -ud @$(($fechaRegistro / 1000))`
- O usar: https://www.epochconverter.com (Lima = UTC-5)

### Paso 2: obtener los timestamps de las firmas humanas

1. Descargar el PDF de la mesa desde la web ONPE
2. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador, no en Edge/Chrome viewer)
3. En la barra izquierda, click en el icono de **pluma** (panel "Firmas")
4. Vas a ver 4 firmas. Click derecho sobre cada una → "Mostrar propiedades de la firma"
5. Verificá:
   - 3 firmas con nombres reales y DNI peruano (presidente, secretario, vocal)
   - 1 firma con motivo "Firma de agente automatizado - STAE"
6. En cada firma, mirá la **"Fecha de firma"** (también llamado "M") — es el momento criptográfico de firma

### Paso 3: comparar

- Las **3 firmas humanas** deberían tener fecha **POSTERIOR** al `fechaRegistro` del estado `C`
- La firma del **AGENTE AUTOMATIZADO STAE** debería ser cercana al `fechaRegistro` (en ±5 min en la mayoría de casos)

Si la fecha de las firmas humanas es POSTERIOR al `fechaRegistro`, esta es la inconsistencia que denunciamos: ONPE marcó la mesa como Contabilizada y publicó su resultado antes de que existieran las firmas humanas.

## Nivel C — Verificación criptográfica del repo completo (1 minuto)

Si tenés este repo descargado y querés verificar que **NADIE** lo alteró:

```bash
cd denuncia
python scripts/verify_manifest.py
```

Esto verifica:
1. Que el `ROOT_HASH.txt` coincida con `sha256(manifest.json)` actual
2. Que cada archivo listado en `manifest.json` tenga su SHA-256 esperado

Si todo está bien:
```
OK  ROOT_HASH coincide: <hash>
Resultado: N/N OK, 0 alterados, 0 faltantes
```

Si algún archivo fue modificado, el script lo reporta:
```
TAMPERED mesas_anomalas/039957/acta.pdf
         esperado: 0c937ce286db81e8e94f0d714868fd627bbd246501c9ca86ab407849d8f2ac38
         actual:   abcdef12345...
```

## Nivel D — Reproducibilidad total

Si querés reconstruir esto desde cero (auditoría máxima):

```bash
git clone <este-repo>
cd denuncia
pip install cryptography pymupdf httpx asyncpg
PYTHONIOENCODING=utf-8 python scripts/build_evidence.py
PYTHONIOENCODING=utf-8 python scripts/recompute_with_fechaRegistro.py
```

Esto re-descarga los PDFs desde la API pública de ONPE y vuelve a generar todo aplicando la métrica correcta. Si ONPE no alteró sus archivos, el resultado debe coincidir con el repo. Si difieren:

- **PDFs con SHA-256 diferente**: ONPE re-emitió los archivos (evidencia adicional)
- **API responses diferentes**: ONPE cambió lo que su API devuelve para esas mesas (evidencia adicional)

## Sello cripto-temporal de tercera parte (opcional, recomendado)

Para que nadie pueda alegar "este repo se hizo después y los hashes son inventados", se puede sellar este repo con [OpenTimestamps](https://opentimestamps.org/), que crea una prueba criptográfica vía blockchain Bitcoin de que el repo existía en cierto momento.

```bash
pip install opentimestamps-client
ots stamp ROOT_HASH.txt
# Genera ROOT_HASH.txt.ots — guardar también
```

Cualquier tercero puede luego verificar:
```bash
ots verify ROOT_HASH.txt.ots
```

## Contacto para reportar inconsistencias

Si encontrás algo que no coincide, podés:
- Abrir un issue en este repo
- Verificarlo independientemente y publicar tus resultados
- Reportar a la prensa con tu evidencia + la nuestra

La evidencia es tan fuerte como la cantidad de personas que la verifican independientemente.
