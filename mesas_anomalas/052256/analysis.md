# Mesa 052256 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.846073+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IE 6060 JULIO C TELLO (código 3253)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 240
- Votos válidos: 207
- Participación: 80.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T05:55:33+00:00` | `2026-04-13 00:55:33 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T05:55:33+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T05:55:33+00:00` | `2026-04-13 00:55:33 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T17:25:47+00:00` | `2026-04-13 12:25:47 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T17:26:11+00:00` | `2026-04-13 12:26:11 (Lima)` |
| Última firma humana | `2026-04-13T17:26:46+00:00` | `2026-04-13 12:26:46 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.51 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-13 00:55:33 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 12:26:11 (Lima), es decir **11.51 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T05:55:30+00:00` | `2026-04-13 00:55:30 (Lima)` | -0.00h |
| 1 | SALAZAR POLO abigail FIR 46541313 sw ebbecdc639e0c0b7448fb7a562d2013eb96d0383 | 46541313 | `2026-04-13T17:26:11+00:00` | `2026-04-13 12:26:11 (Lima)` | +11.51h |
| 2 | SAAVEDRA CUNYARACHE leonardi FIR 40296976 sw b3382c0ff91f5458141a9c38a74e49dc1f7eb530 | 40296976 | `2026-04-13T17:26:32+00:00` | `2026-04-13 12:26:32 (Lima)` | +11.52h |
| 3 | ROSAS CORAQUILLO percy Victorio FIR 75081652 sw 093f9806f9b06f81fd18e24d9ac715e434665b78 | 75081652 | `2026-04-13T17:26:46+00:00` | `2026-04-13 12:26:46 (Lima)` | +11.52h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **052256**
2. Descargar el PDF del acta
3. Verificar SHA-256: `cb36e3635926662cd5761b11dea807d42e16466216754704996430b0068deb33`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
