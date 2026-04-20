# Mesa 062138 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.299899+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IEP UNIVERSITY SANTA ANITA (código 50548)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 235
- Votos válidos: 201
- Participación: 78.595%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:53:23+00:00` | `2026-04-12 20:53:23 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:53:23+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:53:23+00:00` | `2026-04-12 20:53:23 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:35:40+00:00` | `2026-04-12 21:35:40 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:36:00+00:00` | `2026-04-12 21:36:00 (Lima)` |
| Última firma humana | `2026-04-13T02:39:24+00:00` | `2026-04-12 21:39:24 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.71 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:53:23 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:36:00 (Lima), es decir **0.71 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:53:20+00:00` | `2026-04-12 20:53:20 (Lima)` | -0.00h |
| 1 | AYALA JIMENEZ romulo Eduardo FIR 41015871 sw 74ae0fe6afcbb1259368459a152cc5c362fe0c5e | 41015871 | `2026-04-13T02:36:00+00:00` | `2026-04-12 21:36:00 (Lima)` | +0.71h |
| 2 | ARENAS PINTO edwin Antonio FIR 40829770 sw 07ad7ac8da0f346fceaff5c087f3e44f58623f35 | 40829770 | `2026-04-13T02:36:20+00:00` | `2026-04-12 21:36:20 (Lima)` | +0.72h |
| 3 | CABEZAS BOLEJE isabel FIR 07089166 sw 566b9731429463ad249be199815cc8905f08130e | 07089166 | `2026-04-13T02:36:59+00:00` | `2026-04-12 21:36:59 (Lima)` | +0.73h |
| 4 | ROJAS HUAMAN paolo Jesus FIR 48456871 sw af291d24097375277d4bc6800a167c47a7b54ddb | 48456871 | `2026-04-13T02:37:42+00:00` | `2026-04-12 21:37:42 (Lima)` | +0.74h |
| 5 | SANCHEZ PALOMINO nicolas FIR 21809917 sw 57bd89d1661ba676def00a0c9f85f24fab01041c | 21809917 | `2026-04-13T02:38:37+00:00` | `2026-04-12 21:38:37 (Lima)` | +0.75h |
| 6 | RIVERA RAMIREZ jaime Elipio FIR 10418445 sw 864a277d050fd51d571f490b4dcf1da3a74a083b | 10418445 | `2026-04-13T02:38:58+00:00` | `2026-04-12 21:38:58 (Lima)` | +0.76h |
| 7 | CAHUANA CACERES ursula Maribel FIR 40799471 sw 8ebff4da69bf14f4b16c19f453441ac534c2678d | 40799471 | `2026-04-13T02:39:24+00:00` | `2026-04-12 21:39:24 (Lima)` | +0.77h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **062138**
2. Descargar el PDF del acta
3. Verificar SHA-256: `07625eae7a261f02babd291859a692e60bf9186a921e01717e7a0714e7868fa5`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **7** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
