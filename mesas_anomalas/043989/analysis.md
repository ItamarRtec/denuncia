# Mesa 043989 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.845337+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LINCE
- **Local de votación**: IEE 1070 MELITON CARVAJAL - ESTADIO (código 35741)
- **Ubigeo**: 140111

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 212
- Votos válidos: 195
- Participación: 70.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:02:00+00:00` | `2026-04-12 21:02:00 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:02:00+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:02:00+00:00` | `2026-04-12 21:02:00 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:41:34+00:00` | `2026-04-13 08:41:34 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:42:49+00:00` | `2026-04-13 08:42:49 (Lima)` |
| Última firma humana | `2026-04-13T13:43:04+00:00` | `2026-04-13 08:43:04 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.68 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:02:00 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:42:49 (Lima), es decir **11.68 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:01:30+00:00` | `2026-04-12 21:01:30 (Lima)` | -0.01h |
| 1 | VILLARREAL SERNAQUE christhian Jhosep FIR 03684748 sw 78a2dcfa1ac28289c13bf1fe8000519b7258e57c | 03684748 | `2026-04-13T13:42:49+00:00` | `2026-04-13 08:42:49 (Lima)` | +11.68h |
| 2 | VIVAS TAYPE marcos Omar FIR 75608038 sw 03bbbeb1b4c01799cceb74f6bd80bec5159bd271 | 75608038 | `2026-04-13T13:43:04+00:00` | `2026-04-13 08:43:04 (Lima)` | +11.68h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **043989**
2. Descargar el PDF del acta
3. Verificar SHA-256: `a596f7c14a337cddd31f2e3db1d215387a891042ad9e44fa8d8830d5a2ecaed6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
