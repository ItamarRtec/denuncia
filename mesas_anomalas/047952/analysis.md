# Mesa 047952 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.103493+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN ISIDRO
- **Local de votación**: ESTACIONAMIENTO PETROPERU (código 54844)
- **Ubigeo**: 140124

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 199
- Votos válidos: 182
- Participación: 66.555%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:31:57+00:00` | `2026-04-12 20:31:57 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:31:57+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:31:57+00:00` | `2026-04-12 20:31:57 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:01:28+00:00` | `2026-04-13 08:01:28 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:15:08+00:00` | `2026-04-13 08:15:08 (Lima)` |
| Última firma humana | `2026-04-13T13:22:40+00:00` | `2026-04-13 08:22:40 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.72 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:31:57 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:15:08 (Lima), es decir **11.72 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:31:55+00:00` | `2026-04-12 20:31:55 (Lima)` | -0.00h |
| 1 | SANCHEZ ZAVALETA carlos Alberto FIR 08274394 sw 4faec688c149fa8f6a2ac91752c7d3f63ab30128 | 08274394 | `2026-04-13T13:15:08+00:00` | `2026-04-13 08:15:08 (Lima)` | +11.72h |
| 2 | SANTOS VILLALOBOS gloria FIR 27434447 sw 1c6b801d638699d8303fd70f57fa241f6bc6ac83 | 27434447 | `2026-04-13T13:21:26+00:00` | `2026-04-13 08:21:26 (Lima)` | +11.82h |
| 3 | SCHEUERMANN VELARDE connie Alexandra FIR 72698386 sw 00fa8152e43f2b40fc6b4d294a69b2dd70c30928 | 72698386 | `2026-04-13T13:22:40+00:00` | `2026-04-13 08:22:40 (Lima)` | +11.85h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **047952**
2. Descargar el PDF del acta
3. Verificar SHA-256: `be1b908b1aa48b11afeb08a09ff392b1b492e7a85819b8664398fe28a6bb8c34`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
