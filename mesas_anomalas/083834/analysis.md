# Mesa 083834 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.713662+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: VENTANILLA
- **Local de votación**: IE 4021 DANIEL ALCIDES CARRION (código 52705)
- **Ubigeo**: 240106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 209
- Votos válidos: 185
- Participación: 69.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:37:42+00:00` | `2026-04-12 21:37:42 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:37:42+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:37:42+00:00` | `2026-04-12 21:37:42 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:08:13+00:00` | `2026-04-13 09:08:13 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:14:36+00:00` | `2026-04-13 09:14:36 (Lima)` |
| Última firma humana | `2026-04-13T14:18:59+00:00` | `2026-04-13 09:18:59 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.62 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:37:42 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:14:36 (Lima), es decir **11.62 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:37:40+00:00` | `2026-04-12 21:37:40 (Lima)` | -0.00h |
| 1 | SANCHEZ VASQUEZ maria Consuelo FIR 47618690 sw 18578de8dbdf5f30cff8d13ef6ac1248f8b97b10 | 47618690 | `2026-04-13T14:14:36+00:00` | `2026-04-13 09:14:36 (Lima)` | +11.62h |
| 2 | SAMANIEGO GISMONDI nallely Ana FIR 75222637 sw 3bdf6b06f7fdd22e2de36c3d2b65796e4771cef8 | 75222637 | `2026-04-13T14:16:41+00:00` | `2026-04-13 09:16:41 (Lima)` | +11.65h |
| 3 | SANDOVAL FACHO andy Javier FIR 70443549 sw af9094b28c297707ea5b59e5bbe030c3d8306716 | 70443549 | `2026-04-13T14:18:40+00:00` | `2026-04-13 09:18:40 (Lima)` | +11.68h |
| 4 | OSORIO ZAMBRANO gloria Margarita FIR 08684057 sw fed85b569876063d433d8f472cd7810f4dba67cd | 08684057 | `2026-04-13T14:18:59+00:00` | `2026-04-13 09:18:59 (Lima)` | +11.69h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083834**
2. Descargar el PDF del acta
3. Verificar SHA-256: `7f64dc135cac014aeae9ee4de12c8eb146e9587c057d88b97d03a96c07c93277`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
