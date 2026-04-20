# Mesa 083918 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.024573+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: MI PERÚ
- **Local de votación**: IE FE Y ALEGRIA 33 (código 4870)
- **Ubigeo**: 240107

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 230
- Votos emitidos: 188
- Votos válidos: 157
- Participación: 81.739%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:09:22+00:00` | `2026-04-12 20:09:22 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:09:22+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:09:22+00:00` | `2026-04-12 20:09:22 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:02:11+00:00` | `2026-04-12 21:02:11 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:02:32+00:00` | `2026-04-12 21:02:32 (Lima)` |
| Última firma humana | `2026-04-13T02:04:16+00:00` | `2026-04-12 21:04:16 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.89 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:09:22 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:02:32 (Lima), es decir **0.89 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:09:20+00:00` | `2026-04-12 20:09:20 (Lima)` | -0.00h |
| 1 | ALVA BERCERA abner FIR 44765190 sw 1fe69b700b4664c7c9118f1d35930b74461e8d28 | 44765190 | `2026-04-13T02:02:32+00:00` | `2026-04-12 21:02:32 (Lima)` | +0.89h |
| 2 | ADRIANZEN DURAND sheyla Guadalupe FIR 73784957 sw f917254c50af93c5b2ae44894e799d08695eab26 | 73784957 | `2026-04-13T02:02:46+00:00` | `2026-04-12 21:02:46 (Lima)` | +0.89h |
| 3 | ALARCON ANGELES anibal Andy FIR 45862342 sw d626bf7962ca091be653afe574efebaa2b9be46e | 45862342 | `2026-04-13T02:03:04+00:00` | `2026-04-12 21:03:04 (Lima)` | +0.90h |
| 4 | TORRES QUISPE rosa Gloria FIR 80269757 sw 360bbd2984540b1899cff3aa5ef0265f92208e41 | 80269757 | `2026-04-13T02:03:34+00:00` | `2026-04-12 21:03:34 (Lima)` | +0.90h |
| 5 | LANDIO BURGA maria Elizabeth FIR 41648540 sw dc5bb42eed322cb1b39e000edfe0450e267d8c7a | 41648540 | `2026-04-13T02:03:55+00:00` | `2026-04-12 21:03:55 (Lima)` | +0.91h |
| 6 | MIRANDA CRUZADO daysi Isabel FIR 41800324 sw 690211e83ae9ab11e7faddcd3f2f5d7268883567 | 41800324 | `2026-04-13T02:04:16+00:00` | `2026-04-12 21:04:16 (Lima)` | +0.92h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083918**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3b703bc2eb8df7663e5c0da4d8f6fa4847fa011885a86c22262024fb6202314c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **6** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
