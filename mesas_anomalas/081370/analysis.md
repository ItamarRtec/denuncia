# Mesa 081370 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.678925+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CALLAO
- **Local de votación**: IE 5080 SOR ANA DE LOS ANGELES (código 4786)
- **Ubigeo**: 240101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 297
- Votos emitidos: 265
- Votos válidos: 250
- Participación: 89.226%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:46:47+00:00` | `2026-04-12 20:46:47 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:46:47+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:46:47+00:00` | `2026-04-12 20:46:47 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:21:05+00:00` | `2026-04-12 22:21:05 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:21:41+00:00` | `2026-04-12 22:21:41 (Lima)` |
| Última firma humana | `2026-04-13T03:22:30+00:00` | `2026-04-12 22:22:30 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.58 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:46:47 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:21:41 (Lima), es decir **1.58 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:46:45+00:00` | `2026-04-12 20:46:45 (Lima)` | -0.00h |
| 1 | VALDIVIEZO OCHOA herminia Sisi FIR 10727802 sw 46a54f94a269230afea14c9ac2d2e47cbab25470 | 10727802 | `2026-04-13T03:21:41+00:00` | `2026-04-12 22:21:41 (Lima)` | +1.58h |
| 2 | VALLEJOS IZASIGA gerardo Percy FIR 25487550 sw f2c924b40b7a0211d73ba036e1c6e41a91da3a58 | 25487550 | `2026-04-13T03:22:16+00:00` | `2026-04-12 22:22:16 (Lima)` | +1.59h |
| 3 | VALIENTE LUQUE daniela Patricia FIR 70862369 sw f289e265201139c93329ce53639cc91f9688f101 | 70862369 | `2026-04-13T03:22:30+00:00` | `2026-04-12 22:22:30 (Lima)` | +1.60h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **081370**
2. Descargar el PDF del acta
3. Verificar SHA-256: `a254ea63d06abfe791269c2221507b100d5ae693015106617c51111d5bc18fcb`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
