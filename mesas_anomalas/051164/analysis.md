# Mesa 051164 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.465094+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: CLUB SOCIAL DEPORTIVO CULTURAL ZETA SANTA ROSA (código 32651)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 224
- Votos válidos: 209
- Participación: 74.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:23:19+00:00` | `2026-04-12 20:23:19 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:23:19+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:23:19+00:00` | `2026-04-12 20:23:19 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:31:37+00:00` | `2026-04-12 23:31:37 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:32:40+00:00` | `2026-04-12 23:32:40 (Lima)` |
| Última firma humana | `2026-04-13T04:33:15+00:00` | `2026-04-12 23:33:15 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.16 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:23:19 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:32:40 (Lima), es decir **3.16 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:23:17+00:00` | `2026-04-12 20:23:17 (Lima)` | -0.00h |
| 1 | ESPINOZA CANO rosa Milagros FIR 09878082 sw e13ac9486d48b274ad4eeaae75fb9a20660bbefe | 09878082 | `2026-04-13T04:32:40+00:00` | `2026-04-12 23:32:40 (Lima)` | +3.16h |
| 2 | CONTRERAS QUISPE carla Isabel FIR 73062672 sw 387d1fab0325b8b0d23818b23675ee022b7867f4 | 73062672 | `2026-04-13T04:32:59+00:00` | `2026-04-12 23:32:59 (Lima)` | +3.16h |
| 3 | COCA CALDERON gladys Alejandrina FIR 40231721 sw ad7a45b387df94bd5815c4523425cece6cadbfcc | 40231721 | `2026-04-13T04:33:15+00:00` | `2026-04-12 23:33:15 (Lima)` | +3.17h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051164**
2. Descargar el PDF del acta
3. Verificar SHA-256: `39869506a44f8813bac9ca4cf0c158ab8884294dff51686c1c391749624e4176`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
