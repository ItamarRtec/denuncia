# Mesa 053656 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.944081+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: JESÚS MARÍA
- **Local de votación**: PARQUE CACERES (código 55320)
- **Ubigeo**: 140133

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 223
- Votos válidos: 210
- Participación: 74.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:07:53+00:00` | `2026-04-12 21:07:53 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:07:53+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:07:53+00:00` | `2026-04-12 21:07:53 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:37:28+00:00` | `2026-04-13 08:37:28 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:38:09+00:00` | `2026-04-13 08:38:09 (Lima)` |
| Última firma humana | `2026-04-13T13:38:31+00:00` | `2026-04-13 08:38:31 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.50 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:07:53 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:38:09 (Lima), es decir **11.50 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:07:51+00:00` | `2026-04-12 21:07:51 (Lima)` | -0.00h |
| 1 | MENESES DE LA CRUZ deysy Lorena Milagros FIR 43328322 sw 8baf74cd66e4798b6ee3c6e56fa3dd6a8e29fdfa | 43328322 | `2026-04-13T13:38:09+00:00` | `2026-04-13 08:38:09 (Lima)` | +11.50h |
| 2 | MORENO SHAPIAMA salvador FIR 72480881 sw 72fda625697c582f3190c07caf144afaefedd768 | 72480881 | `2026-04-13T13:38:19+00:00` | `2026-04-13 08:38:19 (Lima)` | +11.51h |
| 3 | MURGA BORJAS flor Violeta FIR 32130793 sw 7bb3b9cc67c4421675519b5e793494e42817d057 | 32130793 | `2026-04-13T13:38:31+00:00` | `2026-04-13 08:38:31 (Lima)` | +11.51h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **053656**
2. Descargar el PDF del acta
3. Verificar SHA-256: `f121c57cf3d17c8ca52b78477d62b86c807e71ff91aa03d9db1da8b09de1a775`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
