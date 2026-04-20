# Mesa 082789 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.795193+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CARMEN DE LA LEGUA - REYNOSO
- **Local de votación**: IE RAUL PORRAS BARRENECHEA (código 4840)
- **Ubigeo**: 240104

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 290
- Votos emitidos: 240
- Votos válidos: 209
- Participación: 82.759%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:58:50+00:00` | `2026-04-12 21:58:50 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:58:50+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:58:50+00:00` | `2026-04-12 21:58:50 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:42:17+00:00` | `2026-04-12 23:42:17 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:42:39+00:00` | `2026-04-12 23:42:39 (Lima)` |
| Última firma humana | `2026-04-13T04:44:55+00:00` | `2026-04-12 23:44:55 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.73 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:58:50 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:42:39 (Lima), es decir **1.73 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:58:49+00:00` | `2026-04-12 21:58:49 (Lima)` | -0.00h |
| 1 | VASQUEZ MILLAN daron Jamin FIR 61106148 sw 8b8a43ce4b9caca5c3b6dd46f96b79886f96ab80 | 61106148 | `2026-04-13T04:42:39+00:00` | `2026-04-12 23:42:39 (Lima)` | +1.73h |
| 2 | VARGAS CASTRO jean Franco FIR 70965637 sw 6e1f5994d62b95e7fbd8ad7d11c34c1d13d65dd3 | 70965637 | `2026-04-13T04:42:55+00:00` | `2026-04-12 23:42:55 (Lima)` | +1.73h |
| 3 | VELAZCO HEREDIA david FIR 25649383 sw 1b0bbb1abc01affc4dacd65eaa37cc9406d48696 | 25649383 | `2026-04-13T04:44:55+00:00` | `2026-04-12 23:44:55 (Lima)` | +1.77h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082789**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8d6aebe42f87ef61f15331815809179262afbf63b2758b0562618795fe3f9a44`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
