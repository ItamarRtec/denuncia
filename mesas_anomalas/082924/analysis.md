# Mesa 082924 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.070597+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: LA PERLA
- **Local de votación**: IE PARROQUIAL SAN JOSE (código 4854)
- **Ubigeo**: 240105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 244
- Votos emitidos: 228
- Votos válidos: 211
- Participación: 93.443%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:20:00+00:00` | `2026-04-12 21:20:00 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:20:00+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:20:00+00:00` | `2026-04-12 21:20:00 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:56:25+00:00` | `2026-04-13 08:56:25 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:57:03+00:00` | `2026-04-13 08:57:03 (Lima)` |
| Última firma humana | `2026-04-13T13:59:05+00:00` | `2026-04-13 08:59:05 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.62 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:20:00 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:57:03 (Lima), es decir **11.62 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:19:57+00:00` | `2026-04-12 21:19:57 (Lima)` | -0.00h |
| 1 | ARNAO GUTIERREZ herlinda Amelia FIR 25709972 sw 7e5990b538a0f447e3ae9efb2a1387836601161c | 25709972 | `2026-04-13T13:57:03+00:00` | `2026-04-13 08:57:03 (Lima)` | +11.62h |
| 2 | AYALA LUPUCHE juan Francisco FIR 25594740 sw 37ecc0d96b49e8bd2876e25b4508b66de10f2099 | 25594740 | `2026-04-13T13:57:34+00:00` | `2026-04-13 08:57:34 (Lima)` | +11.63h |
| 3 | BERNAL JIMENEZ gustavo Enrique FIR 48963881 sw 9b46f529a0b8025875b3c16ca0918dcff8070eab | 48963881 | `2026-04-13T13:57:55+00:00` | `2026-04-13 08:57:55 (Lima)` | +11.63h |
| 4 | MORALES HERNANDEZ rosanna Mercedes FIR 25629942 sw d4843d6e9493f3d71fea6031d0552491f7723a21 | 25629942 | `2026-04-13T13:58:39+00:00` | `2026-04-13 08:58:39 (Lima)` | +11.64h |
| 5 | ROMERO SOLANO jenifer Nicol FIR 73520726 sw 9b267e261f65c718bc00a7eb545210d0b5df46b7 | 73520726 | `2026-04-13T13:59:05+00:00` | `2026-04-13 08:59:05 (Lima)` | +11.65h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082924**
2. Descargar el PDF del acta
3. Verificar SHA-256: `27ab0cdf1bb60362412c1e97b575516ae12446f2403b4a14369379e19fab2183`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
