# Mesa 042794 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.891380+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA VICTORIA
- **Local de votación**: IE EMBLEMATICA 1120 PEDRO ADOLFO LABARTHE EFFIO (código 2896)
- **Ubigeo**: 140109

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 229
- Votos válidos: 210
- Participación: 76.589%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:32:42+00:00` | `2026-04-12 21:32:42 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:32:42+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:32:42+00:00` | `2026-04-12 21:32:42 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:04:55+00:00` | `2026-04-13 09:04:55 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:05:48+00:00` | `2026-04-13 09:05:48 (Lima)` |
| Última firma humana | `2026-04-13T14:06:52+00:00` | `2026-04-13 09:06:52 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.55 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:32:42 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:05:48 (Lima), es decir **11.55 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:25:47+00:00` | `2026-04-12 21:25:47 (Lima)` | -0.12h |
| 1 | ESPINOZA MUCHA gustavo Arturo FIR 07489563 sw 2a0d806b7a6bdacdeee9adca70623ea21c806eac | 07489563 | `2026-04-13T14:05:48+00:00` | `2026-04-13 09:05:48 (Lima)` | +11.55h |
| 2 | ESPINOZA COLQUI diana Eugenia FIR 41084824 sw cb80a77a91e057b936fce579798b177d6fd61c87 | 41084824 | `2026-04-13T14:06:32+00:00` | `2026-04-13 09:06:32 (Lima)` | +11.56h |
| 3 | FARFAN FERNANDEZ amalia FIR 44782931 sw e135e2412a3a05461cd07dc2225b7924ae7c91e5 | 44782931 | `2026-04-13T14:06:52+00:00` | `2026-04-13 09:06:52 (Lima)` | +11.57h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042794**
2. Descargar el PDF del acta
3. Verificar SHA-256: `fc6921f9ce1294567ec0c3b3733e674dc5d3360ca0567d9b8c3d31d549adbacb`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
