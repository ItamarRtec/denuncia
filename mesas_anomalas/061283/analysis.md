# Mesa 061283 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.417305+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LOS OLIVOS
- **Local de votación**: IEP BARBARA D´ACHILLE SCHOOL (código 17391)
- **Ubigeo**: 140142

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 257
- Votos válidos: 233
- Participación: 85.953%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:36:27+00:00` | `2026-04-12 20:36:27 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:36:27+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:36:27+00:00` | `2026-04-12 20:36:27 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:19:06+00:00` | `2026-04-12 23:19:06 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:19:28+00:00` | `2026-04-12 23:19:28 (Lima)` |
| Última firma humana | `2026-04-13T04:20:15+00:00` | `2026-04-12 23:20:15 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.72 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:36:27 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:19:28 (Lima), es decir **2.72 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:36:26+00:00` | `2026-04-12 20:36:26 (Lima)` | -0.00h |
| 1 | VILLACORTA FLORIAN arlene Gisella FIR 43334260 sw 8182ee2bc666f4a7859b3f8958b9cb09b3eebd85 | 43334260 | `2026-04-13T04:19:28+00:00` | `2026-04-12 23:19:28 (Lima)` | +2.72h |
| 2 | VELASQUEZ BOJORQUEZ yonathan Carlos FIR 43646946 sw 3d4cf09b1182e72e1455b5968ddfb68e57c3fdb8 | 43646946 | `2026-04-13T04:20:15+00:00` | `2026-04-12 23:20:15 (Lima)` | +2.73h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061283**
2. Descargar el PDF del acta
3. Verificar SHA-256: `f76ae57218c3afd79aef087fa977b0798b1eb1aa02a6a405d1c21e2718820b1a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
