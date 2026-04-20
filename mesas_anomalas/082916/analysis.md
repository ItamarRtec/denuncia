# Mesa 082916 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.829419+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: LA PERLA
- **Local de votación**: IE JOSE OLAYA BALANDRA (código 4853)
- **Ubigeo**: 240105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 221
- Votos válidos: 201
- Participación: 73.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:00:44+00:00` | `2026-04-12 21:00:44 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:00:44+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:00:44+00:00` | `2026-04-12 21:00:44 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:11:47+00:00` | `2026-04-13 08:11:47 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:12:14+00:00` | `2026-04-13 08:12:14 (Lima)` |
| Última firma humana | `2026-04-13T13:13:22+00:00` | `2026-04-13 08:13:22 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.19 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:00:44 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:12:14 (Lima), es decir **11.19 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:00:41+00:00` | `2026-04-12 21:00:41 (Lima)` | -0.00h |
| 1 | SALVADOR CORREA cesar Enrique FIR 41238248 sw 16f6bbf2880a020407dbc7b7a9a64903d0300fd6 | 41238248 | `2026-04-13T13:12:14+00:00` | `2026-04-13 08:12:14 (Lima)` | +11.19h |
| 2 | SALAZAR LLAQUE diana Janet FIR 25770851 sw d46f79a01c63d5a67af42939c58696ae117761cd | 25770851 | `2026-04-13T13:12:32+00:00` | `2026-04-13 08:12:32 (Lima)` | +11.20h |
| 3 | SALHUANA CARBONERO pedro Alfonso FIR 25773474 sw a195f06391329f4ada6549101bc20cfeae649aaf | 25773474 | `2026-04-13T13:12:45+00:00` | `2026-04-13 08:12:45 (Lima)` | +11.20h |
| 4 | RODRIGUEZ ROJAS alexis Santos FIR 25792768 sw 8158bac579ef7f96a9b277b8ef39ae15044b5986 | 25792768 | `2026-04-13T13:13:22+00:00` | `2026-04-13 08:13:22 (Lima)` | +11.21h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082916**
2. Descargar el PDF del acta
3. Verificar SHA-256: `18ca2989312389fa8931d7c4a4b36076dea6671e97750e2300d43cbf0473839d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
