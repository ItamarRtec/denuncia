# Comunicado público — inconsistencia documental en publicación de actas ONPE EG2026

**Fecha**: [Por completar al publicar]
**Repositorio de evidencia**: [Por completar con URL pública]
**Hash raíz de la evidencia**: ver `ROOT_HASH.txt`

## Lo que encontramos

Analizando la metadata de las **79,014 mesas contabilizadas** en la Elección General Perú 2026 (EG2026) que publica la Oficina Nacional de Procesos Electorales (ONPE) a través de su API pública oficial, identificamos **337 mesas** donde:

- ONPE marcó la mesa como **Contabilizada** y publicó su resultado en la web pública
- Pero los **miembros de mesa firmaron digitalmente el acta horas DESPUÉS** de esa publicación

Las firmas se realizan con **certificados X.509 personales** emitidos por ONPE a cada miembro de mesa, con su DNI peruano embebido. Los timestamps de cada firma son cripto-verificables: están dentro del PDF que ONPE mismo sirve, y no se pueden modificar sin invalidar la firma.

Esto contradice la declaración pública de ONPE de que *"no se publica ningún resultado sin haber digitalizado el acta"* y contradice también el flujo documentado en su propia **Cartilla de Instrucciones para Personeros STAE EG2026** (incluida en este repositorio).

## Lo que dice la cartilla oficial ONPE

La Cartilla de Personeros STAE EG2026 (documento oficial de ONPE, generado el 26 enero 2026) describe el flujo de escrutinio en su página 18:

> *"Presenciar que los miembros de mesa firmen digitalmente las actas de escrutinio... Presenciar la impresión de las actas de escrutinio y del 'Cartel de resultados'"*

Y en su página 19 describe la transmisión:

> *"Presenciar, únicamente desde el área de observación del punto de transmisión, el envío de los resultados de la mesa"*

El orden documentado es: **miembros firman → se imprime → se transmite a ONPE**.

## Lo que muestra la evidencia

En 337 mesas detectamos el orden opuesto, verificado con certificados X.509:

```
1. AGENTE AUTOMATIZADO STAE (software ONPE, NO mencionado en la cartilla) firma
2. Estado de la mesa pasa a C (Contabilizada) — ONPE marca la mesa publicada
3. HORAS DESPUÉS (mediana +4.07h, máximo +14.50h):
   los miembros de mesa firman digitalmente con sus certificados personales
```

### Distribución del retraso

```
Tiempo entre publicación (fechaRegistro=C) y primera firma humana:
  p25:  +1.80h
  p50:  +4.07h
  p75:  +11.03h
  p90:  +11.57h
  máximo:  +14.50h
```

### Concentración geográfica perfecta

```
LIMA:    298 mesas (88.4%)
CALLAO:   39 mesas (11.6%)
─────────────────────────
TOTAL:   337 mesas — 100% en Lima Metropolitana o Callao
0 casos en los otros 23 departamentos
```

Esta distribución indica que el patrón **no es estructural** del sistema STAE — es específico de cierta infraestructura o centros de procesamiento de Lima/Callao.

## Lo que NO afirmamos

Quiero ser explícito sobre los límites de esta evidencia:

1. **NO es prueba de fraude electoral.** Es prueba de irregularidad procedimental e inconsistencia entre lo declarado por ONPE y los datos verificables de su propia API.
2. **NO verificamos que los conteos publicados sean numéricamente incorrectos.** Para eso se requeriría comparación entre los números escritos a mano en el papel original y los publicados por ONPE; esto está fuera del alcance de esta denuncia.
3. **NO conocemos la causa.** Podría ser falla técnica, decisión administrativa, sobrecarga del sistema, o protocolo no documentado. La denuncia exige explicación, no acusa específicamente.
4. **El conteo podría ser mayor.** Las 337 mesas surgen del análisis de un subconjunto. Una auditoría sobre las 79,014 mesas con la misma metodología podría detectar más casos.

## Lo que SÍ exigimos

ONPE debe explicar públicamente:

1. **¿Por qué 337 mesas tienen firmas humanas posteriores a la publicación del resultado?** ¿Qué documento se publicó como "acta digitalizada" durante la ventana sin firma humana?
2. **¿Por qué las 337 están todas concentradas en Lima/Callao?** Si es un flujo legítimo, debería ser uniforme en todo el país.
3. **¿Cuál es el flujo real de firma en EG2026?** La Cartilla oficial dice una cosa; la metadata de los propios PDFs de ONPE muestra otra.
4. **¿Quién es el "AGENTE AUTOMATIZADO STAE"?** ¿Por qué firma criptográficamente las actas si la cartilla oficial no lo menciona como firmante? ¿Cuál es su rol legal?
5. **¿Hay otras mesas con esta inconsistencia que no detectamos?** Pedimos que ONPE publique la metadata completa del proceso de firma y digitalización para verificación independiente.

## Cómo verificar esto independientemente

Cualquier persona con conexión a internet puede reproducir esta evidencia en menos de 5 minutos:

1. Elegir cualquier mesa del listado, por ejemplo Mesa **039957**
2. Ir a https://resultadoelectoral.onpe.gob.pe → buscar la mesa
3. Descargar el PDF del acta
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador) y abrir el panel "Firmas"
5. Verificar el timestamp (`/M`) de cada firma humana
6. Consultar la API ONPE: `https://resultadoelectoral.onpe.gob.pe/presentacion-backend/actas/buscar/mesa?codigoMesa=<MESA>&idEleccion=10`
7. En la respuesta, mirar `lineaTiempo[i]` con `codigoEstadoActa = "C"` y su campo `fechaRegistro` (epoch milliseconds UTC)
8. Comparar: las firmas humanas son posteriores al `fechaRegistro` del estado `C`

Instrucciones detalladas en el repositorio: ver `HOW_TO_VERIFY.md`.

El repositorio completo de evidencia incluye:
- 337 mesas con su PDF original byte-a-byte
- Captura cruda de la respuesta de la API ONPE para cada mesa
- Análisis de cada firma X.509 con identidad del firmante (incluyendo DNI)
- SHA-256 de cada artefacto en `manifest.json` (tamper-evident)
- Hash raíz publicado en `ROOT_HASH.txt`
- Cartilla oficial STAE EG2026 incluida como fuente primaria del flujo declarado
- Scripts reproducibles para regenerar todo desde la API ONPE

## Errata metodológica (transparencia)

Una versión inicial de este análisis usó el campo `daudFechaCreacion` (timestamp del adjunto digital) en lugar del campo correcto `lineaTiempo[i].fechaRegistro` con `codigoEstadoActa = "C"`. La diferencia es importante: `daudFechaCreacion` no es el momento de publicación. La corrección fue detectada antes de la publicación, está documentada en `METHODOLOGY.md`, y los números publicados aquí utilizan la métrica correcta.

## Preservación de evidencia

Pensando defensivamente:

1. La evidencia está distribuida en múltiples ubicaciones (git público + snapshots de archive.org de las URLs ONPE)
2. Cada PDF tiene SHA-256 publicado: si ONPE re-emite los archivos con timestamps "corregidos", quedarán visibles las diferencias
3. El `git log` provee timeline inmutable; el repo está mirroreado en GitHub público
4. Cada `api_response.json` captura la respuesta exacta de ONPE en el momento: si después modifican lo que devuelve la API, la diferencia es evidencia adicional

## Contacto

[Por completar]
