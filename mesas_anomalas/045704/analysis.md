# Mesa 045704 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.930464+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PACHACÁMAC
- **Local de votación**: IEP CHARLES FINNEY (código 13539)
- **Ubigeo**: 140116

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 191
- Votos válidos: 172
- Participación: 63.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:22:04+00:00` | `2026-04-12 21:22:04 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:22:04+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:22:04+00:00` | `2026-04-12 21:22:04 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:55:02+00:00` | `2026-04-13 08:55:02 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:55:28+00:00` | `2026-04-13 08:55:28 (Lima)` |
| Última firma humana | `2026-04-13T13:56:04+00:00` | `2026-04-13 08:56:04 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.56 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:22:04 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:55:28 (Lima), es decir **11.56 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:20:00+00:00` | `2026-04-12 21:20:00 (Lima)` | -0.03h |
| 1 | SANTOS ZAVALETA giancarlo Antonio FIR 72901451 sw cb3c9519e648628bad166eb778839d7b6d963c3c | 72901451 | `2026-04-13T13:55:28+00:00` | `2026-04-13 08:55:28 (Lima)` | +11.56h |
| 2 | SANCHEZ TANDAYPAN gianella Jimena FIR 60977928 sw d6609d3ca5779c9bcaf0d2fd4fdc5da3be11859e | 60977928 | `2026-04-13T13:55:40+00:00` | `2026-04-13 08:55:40 (Lima)` | +11.56h |
| 3 | SANCHEZ ESPIRITU jilmer Nelson FIR 20644555 sw 86e705094664f1ad91a1d11fa40e151232e327a1 | 20644555 | `2026-04-13T13:56:04+00:00` | `2026-04-13 08:56:04 (Lima)` | +11.57h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045704**
2. Descargar el PDF del acta
3. Verificar SHA-256: `a4dd4c5166230735ce2a59415cb2b1eee93984fed7a22befcc942f191d6fea93`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
