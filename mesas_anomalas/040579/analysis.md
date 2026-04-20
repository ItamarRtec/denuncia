# Mesa 040579 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.553251+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IEP MARIO VARGAS LLOSA (código 2845)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 240
- Votos válidos: 213
- Participación: 80.268%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:04:08+00:00` | `2026-04-12 20:04:08 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:04:08+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:04:08+00:00` | `2026-04-12 20:04:08 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:29:27+00:00` | `2026-04-12 23:29:27 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:29:46+00:00` | `2026-04-12 23:29:46 (Lima)` |
| Última firma humana | `2026-04-13T04:30:17+00:00` | `2026-04-12 23:30:17 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.43 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:04:08 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:29:46 (Lima), es decir **3.43 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:04:06+00:00` | `2026-04-12 20:04:06 (Lima)` | -0.00h |
| 1 | RAMIREZ FELIPE nelly Esther FIR 09990380 sw aeabc7a77ebff496a31a92085f7e6b2b922da254 | 09990380 | `2026-04-13T04:29:46+00:00` | `2026-04-12 23:29:46 (Lima)` | +3.43h |
| 2 | RODRIGUEZ HUAMANI DE HUAMAN victoria Florinda FIR 09964524 sw bf12de4228daa5e17bf978146943a7c1a039239c | 09964524 | `2026-04-13T04:30:01+00:00` | `2026-04-12 23:30:01 (Lima)` | +3.43h |
| 3 | ROSALES CORTEZ olmedo Teodolfo FIR 10390257 sw 0aee00100861d5b4b5241e2e8100b6fe19893f00 | 10390257 | `2026-04-13T04:30:17+00:00` | `2026-04-12 23:30:17 (Lima)` | +3.44h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **040579**
2. Descargar el PDF del acta
3. Verificar SHA-256: `d91809daf5f597dcdf7021624db9465ec441e496eeaaf776a7f62574ed539beb`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
