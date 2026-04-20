# Mesa 054847 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.404601+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 7211 VIRGEN INMACULADA (código 3346)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 270
- Votos válidos: 233
- Participación: 90.301%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:56:10+00:00` | `2026-04-12 20:56:10 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:56:10+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:56:10+00:00` | `2026-04-12 20:56:10 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:26:55+00:00` | `2026-04-12 23:26:55 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:27:13+00:00` | `2026-04-12 23:27:13 (Lima)` |
| Última firma humana | `2026-04-13T04:28:26+00:00` | `2026-04-12 23:28:26 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.52 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:56:10 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:27:13 (Lima), es decir **2.52 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:56:07+00:00` | `2026-04-12 20:56:07 (Lima)` | -0.00h |
| 1 | DIAZ ULLOA walter Hermenegildo FIR 17859885 sw f99377e2c1d4a2ca9ce65dfe96998c20d5740267 | 17859885 | `2026-04-13T04:27:13+00:00` | `2026-04-12 23:27:13 (Lima)` | +2.52h |
| 2 | FLORES ARIAS edmer Robinson FIR 09651732 sw a7a1ae36c63a34c0f0f061a3c21b57b69f73e81f | 09651732 | `2026-04-13T04:27:27+00:00` | `2026-04-12 23:27:27 (Lima)` | +2.52h |
| 3 | GARCIA LEDESMA felipe FIR 07951987 sw 9ff23f0ee67d6f11f047c81d4e071a8b0367dd7b | 07951987 | `2026-04-13T04:27:38+00:00` | `2026-04-12 23:27:38 (Lima)` | +2.52h |
| 4 | ALDORADIN TOMAYQUISPE maria Esther FIR 09143855 sw 28f3ae9e874e36feb56e0004e282dfcab61cc7f5 | 09143855 | `2026-04-13T04:28:04+00:00` | `2026-04-12 23:28:04 (Lima)` | +2.53h |
| 5 | LAZARO QUISPE herlinda FIR 07421394 sw 00537ac8f9914286087ace81f49e9803517f91d9 | 07421394 | `2026-04-13T04:28:16+00:00` | `2026-04-12 23:28:16 (Lima)` | +2.54h |
| 6 | PUMA VALERIANO DE YTO carmen FIR 06930106 sw 74f13cbe4079b826dff83990f11111fa8edcc6e4 | 06930106 | `2026-04-13T04:28:26+00:00` | `2026-04-12 23:28:26 (Lima)` | +2.54h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054847**
2. Descargar el PDF del acta
3. Verificar SHA-256: `6274245532a561d9affdd2ef2b1ad84af7b8b91c90ddf8b320003d0f012e7cae`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **6** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
