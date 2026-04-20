# Mesa 051061 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.196130+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IE 6097 MATEO PUMACAHUA (código 5120)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 236
- Votos válidos: 224
- Participación: 78.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:10:22+00:00` | `2026-04-12 20:10:22 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:10:22+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:10:22+00:00` | `2026-04-12 20:10:22 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:41:05+00:00` | `2026-04-12 23:41:05 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:42:08+00:00` | `2026-04-12 23:42:08 (Lima)` |
| Última firma humana | `2026-04-13T04:42:28+00:00` | `2026-04-12 23:42:28 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.53 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:10:22 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:42:08 (Lima), es decir **3.53 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:10:20+00:00` | `2026-04-12 20:10:20 (Lima)` | -0.00h |
| 1 | CONDE PUCHURI donny Alexis FIR 74860735 sw b22d3ac5947ba1fcf5894ed602a9d847c8483e3a | 74860735 | `2026-04-13T04:42:08+00:00` | `2026-04-12 23:42:08 (Lima)` | +3.53h |
| 2 | CONTRERAS PACOSONCCO leidy Brigitte FIR 61212931 sw 51d5dce36d5d0228232bc4c6541d647d303f15ea | 61212931 | `2026-04-13T04:42:19+00:00` | `2026-04-12 23:42:19 (Lima)` | +3.53h |
| 3 | CRUCES FERNANDEZ diego Enrique FIR 70612267 sw 1a58be2f5ced799bd016e9c39df3d193c01ceaf6 | 70612267 | `2026-04-13T04:42:28+00:00` | `2026-04-12 23:42:28 (Lima)` | +3.54h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051061**
2. Descargar el PDF del acta
3. Verificar SHA-256: `71bb4616a4e16e0f879085dae3188f12b7f0115f54defaf006c2799c298a4eb6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
