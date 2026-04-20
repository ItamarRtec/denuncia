# Mesa 051873 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.447535+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: COMPLEJO DEPORTIVO PAUL HARRIS - MOROCOCHA (código 14161)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 238
- Votos válidos: 218
- Participación: 79.599%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:31:08+00:00` | `2026-04-12 21:31:08 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:31:08+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:31:08+00:00` | `2026-04-12 21:31:08 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:02:52+00:00` | `2026-04-12 23:02:52 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:03:38+00:00` | `2026-04-12 23:03:38 (Lima)` |
| Última firma humana | `2026-04-13T04:04:11+00:00` | `2026-04-12 23:04:11 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.54 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:31:08 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:03:38 (Lima), es decir **1.54 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:31:05+00:00` | `2026-04-12 21:31:05 (Lima)` | -0.00h |
| 1 | FALEN LARA luis Alexei FIR 06171696 sw 21cbb1bb2e68a65933afe94f0cc271b97207ce38 | 06171696 | `2026-04-13T04:03:38+00:00` | `2026-04-12 23:03:38 (Lima)` | +1.54h |
| 2 | FLORES RAMIREZ jesus Elena FIR 42069295 sw 356140951a2ef06292cde7876cc5be6198d34b83 | 42069295 | `2026-04-13T04:03:57+00:00` | `2026-04-12 23:03:57 (Lima)` | +1.55h |
| 3 | FLORES LOPEZ leonor Elva FIR 10342677 sw 41685c9df1f12f18eaf34efc4a8df4d0f0b5836d | 10342677 | `2026-04-13T04:04:11+00:00` | `2026-04-12 23:04:11 (Lima)` | +1.55h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051873**
2. Descargar el PDF del acta
3. Verificar SHA-256: `0102c6213f08d18a577df8e9a89a4e5185003d7c2f722f8f2971ee46bf91305d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
