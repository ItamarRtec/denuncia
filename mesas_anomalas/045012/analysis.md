# Mesa 045012 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.387963+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: CEBE 4 MIRAFLORES (código 2979)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 256
- Votos emitidos: 176
- Votos válidos: 167
- Participación: 68.75%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:01:10+00:00` | `2026-04-12 21:01:10 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:01:10+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:01:10+00:00` | `2026-04-12 21:01:10 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:05:07+00:00` | `2026-04-12 23:05:07 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:05:28+00:00` | `2026-04-12 23:05:28 (Lima)` |
| Última firma humana | `2026-04-13T04:06:47+00:00` | `2026-04-12 23:06:47 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.07 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:01:10 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:05:28 (Lima), es decir **2.07 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:00:33+00:00` | `2026-04-12 21:00:33 (Lima)` | -0.01h |
| 1 | AGUILAR VASQUEZ melina Paola FIR 45197327 sw 53fa61b0c58f4b811e6c837df49953a004ce775c | 45197327 | `2026-04-13T04:05:28+00:00` | `2026-04-12 23:05:28 (Lima)` | +2.07h |
| 2 | ARANA REYES GARCIA marianella Ana FIR 10277959 sw 27b5734588fecba55fff5c72f455dbfcb2ff2483 | 10277959 | `2026-04-13T04:05:48+00:00` | `2026-04-12 23:05:48 (Lima)` | +2.08h |
| 3 | ALBINAGORTA GUERRERO roberto FIR 71274938 sw ed25fe7bd58e92f71058dec8a58c8662f7666a0e | 71274938 | `2026-04-13T04:06:10+00:00` | `2026-04-12 23:06:10 (Lima)` | +2.08h |
| 4 | GALVEZ GUEVARA gisella Maria Del Carmen FIR 42632506 sw c07102a8e1dd00757d0702e83b5321c1fc79dee4 | 42632506 | `2026-04-13T04:06:47+00:00` | `2026-04-12 23:06:47 (Lima)` | +2.09h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045012**
2. Descargar el PDF del acta
3. Verificar SHA-256: `0c20fa18be26b54d4c708dea4e9476bdddc6fe8a2fa1b3a846c3276d24b2a7c4`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
