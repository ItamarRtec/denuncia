# Mesa 082633 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.000294+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: BELLAVISTA
- **Local de votación**: UNIVERSIDAD NACIONAL DEL CALLAO (código 17916)
- **Ubigeo**: 240102

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 295
- Votos emitidos: 218
- Votos válidos: 197
- Participación: 73.898%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T04:21:31+00:00` | `2026-04-12 23:21:31 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T04:21:31+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T04:21:31+00:00` | `2026-04-12 23:21:31 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:21:25+00:00` | `2026-04-13 09:21:25 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T15:29:44+00:00` | `2026-04-13 10:29:44 (Lima)` |
| Última firma humana | `2026-04-13T15:31:13+00:00` | `2026-04-13 10:31:13 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.14 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 23:21:31 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 10:29:44 (Lima), es decir **11.14 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T04:21:28+00:00` | `2026-04-12 23:21:28 (Lima)` | -0.00h |
| 1 | VILCHEZ HARHUAS angie Esperanza FIR 72924111 sw c3180e5dc70f3e49fbf1c12b771129810b85b4f2 | 72924111 | `2026-04-13T15:29:44+00:00` | `2026-04-13 10:29:44 (Lima)` | +11.14h |
| 2 | VILLAFUERTE PRIETO ruben FIR 09272619 sw 05c94b0b1970981d353935e879bc70a33137a02f | 09272619 | `2026-04-13T15:30:38+00:00` | `2026-04-13 10:30:38 (Lima)` | +11.15h |
| 3 | VILLAR AGUILAR enrique Arturo FIR 25744454 sw e89b4c3c5350695f78015d5f248e8ea8bed49769 | 25744454 | `2026-04-13T15:31:13+00:00` | `2026-04-13 10:31:13 (Lima)` | +11.16h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082633**
2. Descargar el PDF del acta
3. Verificar SHA-256: `483815719c9194ab859529fe32048be185a0e44e4c64494dea292fb12b24a14a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
