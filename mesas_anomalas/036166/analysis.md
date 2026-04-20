# Mesa 036166 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.167312+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE 1146 REPUBLICA DE PARAGUAY (código 2651)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 224
- Votos válidos: 193
- Participación: 74.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:57:09+00:00` | `2026-04-12 22:57:09 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:57:09+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:57:09+00:00` | `2026-04-12 22:57:09 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T06:14:41+00:00` | `2026-04-13 01:14:41 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:15:34+00:00` | `2026-04-13 01:15:34 (Lima)` |
| Última firma humana | `2026-04-13T06:16:26+00:00` | `2026-04-13 01:16:26 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.31 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:57:09 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:15:34 (Lima), es decir **2.31 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:57:08+00:00` | `2026-04-12 22:57:08 (Lima)` | -0.00h |
| 1 | CATACORA MENDOZA bernardino FIR 43646968 sw 49ef1b955a0b993cb411c3d763f09e004265cd5e | 43646968 | `2026-04-13T06:15:34+00:00` | `2026-04-13 01:15:34 (Lima)` | +2.31h |
| 2 | CASTRO CASTRO victor FIR 43367281 sw 9c7979630b3de42957d1949da0cf34662410da6b | 43367281 | `2026-04-13T06:16:26+00:00` | `2026-04-13 01:16:26 (Lima)` | +2.32h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036166**
2. Descargar el PDF del acta
3. Verificar SHA-256: `b19c17a45d05f64ea330bbb58f75ee40948919465a029fe6996b4d421342ced5`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
