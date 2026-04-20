# Mesa 056417 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.032638+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IE 109 INCA MANCO CAPAC (código 3409)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 274
- Votos válidos: 236
- Participación: 91.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:37:51+00:00` | `2026-04-12 21:37:51 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:37:51+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:37:51+00:00` | `2026-04-12 21:37:51 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:45:58+00:00` | `2026-04-13 07:45:58 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:46:25+00:00` | `2026-04-13 07:46:25 (Lima)` |
| Última firma humana | `2026-04-13T12:46:54+00:00` | `2026-04-13 07:46:54 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.14 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:37:51 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:46:25 (Lima), es decir **10.14 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:33:17+00:00` | `2026-04-12 21:33:17 (Lima)` | -0.08h |
| 1 | CHAVEZ MEJIA marco Antonio FIR 10107816 sw 46f0ed1fa09ade3bb2666f98bb5368636d6dcb35 | 10107816 | `2026-04-13T12:46:25+00:00` | `2026-04-13 07:46:25 (Lima)` | +10.14h |
| 2 | CENTENO YARIN yury FIR 43443008 sw 8e47123c1a74f5f1e39b29b2274cbd917d7b6b6a | 43443008 | `2026-04-13T12:46:41+00:00` | `2026-04-13 07:46:41 (Lima)` | +10.15h |
| 3 | CHAVEZ LIMAYMANTA edgar Hugo FIR 42054222 sw 3326f1776050c9d338b9c7cc6a9526978bbac2ab | 42054222 | `2026-04-13T12:46:54+00:00` | `2026-04-13 07:46:54 (Lima)` | +10.15h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **056417**
2. Descargar el PDF del acta
3. Verificar SHA-256: `83511929d2d16b905d442caa3b143eb44dba76e34da6e669712b3c6b963be65d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
