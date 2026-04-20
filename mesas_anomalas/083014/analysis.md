# Mesa 083014 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.079980+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: LA PERLA
- **Local de votación**: IEPM COLEGIO MILITAR LEONCIO PRADO (código 40913)
- **Ubigeo**: 240105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 230
- Votos emitidos: 163
- Votos válidos: 139
- Participación: 70.87%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:30:59+00:00` | `2026-04-12 21:30:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:30:59+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:30:59+00:00` | `2026-04-12 21:30:59 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:40:37+00:00` | `2026-04-13 08:40:37 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:41:14+00:00` | `2026-04-13 08:41:14 (Lima)` |
| Última firma humana | `2026-04-13T13:41:41+00:00` | `2026-04-13 08:41:41 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.17 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:30:59 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:41:14 (Lima), es decir **11.17 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:30:55+00:00` | `2026-04-12 21:30:55 (Lima)` | -0.00h |
| 1 | AGUIRRE SARAVIA andrea Luciana FIR 75254941 sw 3092a7c16b064c659243fd5261e9a253eca80b8b | 75254941 | `2026-04-13T13:41:14+00:00` | `2026-04-13 08:41:14 (Lima)` | +11.17h |
| 2 | ALBERTI RAMIREZ clara Tamara Ben-oni FIR 76589497 sw 70bdcfc80e1dfefb2484e85fd05573aef0812c69 | 76589497 | `2026-04-13T13:41:29+00:00` | `2026-04-13 08:41:29 (Lima)` | +11.18h |
| 3 | ADRIANZEN BERNAL olga FIR 40528354 sw f2bad5d35b13f24c51b0f3c091996030c0e8a952 | 40528354 | `2026-04-13T13:41:41+00:00` | `2026-04-13 08:41:41 (Lima)` | +11.18h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083014**
2. Descargar el PDF del acta
3. Verificar SHA-256: `27ec016ccb5050a0e2d02b239d0ddd15621fbabd1a488a19b63ca9258fbce58c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
