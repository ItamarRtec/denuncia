# Mesa 058816 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.662691+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN LUIS
- **Local de votación**: IE LOS EDUCADORES (código 3482)
- **Ubigeo**: 140138

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 295
- Votos emitidos: 239
- Votos válidos: 211
- Participación: 81.017%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:48:05+00:00` | `2026-04-12 21:48:05 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:48:05+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:48:05+00:00` | `2026-04-12 21:48:05 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:23:56+00:00` | `2026-04-13 08:23:56 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:24:18+00:00` | `2026-04-13 08:24:18 (Lima)` |
| Última firma humana | `2026-04-13T13:25:59+00:00` | `2026-04-13 08:25:59 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.60 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:48:05 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:24:18 (Lima), es decir **10.60 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:42:55+00:00` | `2026-04-12 21:42:55 (Lima)` | -0.09h |
| 1 | MORCCOLLA SEGOVIA isabel FIR 40756689 sw bfeb49137323bfec9fdbd7bff00676157e464e1f | 40756689 | `2026-04-13T13:24:18+00:00` | `2026-04-13 08:24:18 (Lima)` | +10.60h |
| 2 | MUNAYLLA SALAZAR daniel Fernando FIR 76631156 sw 4a1c97b715a478c24253d4781fcd24829e77aec8 | 76631156 | `2026-04-13T13:24:30+00:00` | `2026-04-13 08:24:30 (Lima)` | +10.61h |
| 3 | NISHIMAZURUGA LIMA miguel Junior FIR 47961514 sw fcb58ab7b8949d73775408cf4bb28e1cba137fc6 | 47961514 | `2026-04-13T13:24:40+00:00` | `2026-04-13 08:24:40 (Lima)` | +10.61h |
| 4 | RAMOS AGAPITO rafael Alex FIR 06792265 sw 6109230f55bc915b314f483a266c9b92094df958 | 06792265 | `2026-04-13T13:25:33+00:00` | `2026-04-13 08:25:33 (Lima)` | +10.62h |
| 5 | MENDOZA MICHUY roger Manuel FIR 08425421 sw 44613c1921aee4377320459bf29abe47f3f2c8b5 | 08425421 | `2026-04-13T13:25:59+00:00` | `2026-04-13 08:25:59 (Lima)` | +10.63h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **058816**
2. Descargar el PDF del acta
3. Verificar SHA-256: `7926d94a82e9e0a71786cbe8c4c1bcca818fcc217bcc7eda19d870ee846f3c87`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
