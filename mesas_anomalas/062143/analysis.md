# Mesa 062143 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.085941+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IEP UNIVERSITY SANTA ANITA (código 50548)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 241
- Votos válidos: 205
- Participación: 80.602%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:33:07+00:00` | `2026-04-12 20:33:07 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:33:07+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:33:07+00:00` | `2026-04-12 20:33:07 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:10:08+00:00` | `2026-04-12 21:10:08 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:10:25+00:00` | `2026-04-12 21:10:25 (Lima)` |
| Última firma humana | `2026-04-13T02:12:07+00:00` | `2026-04-12 21:12:07 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.62 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:33:07 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:10:25 (Lima), es decir **0.62 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:33:04+00:00` | `2026-04-12 20:33:04 (Lima)` | -0.00h |
| 1 | POZO RIVERA jose Florentino FIR 10699106 sw 99ea39ef45edf5c1194dbe51fae2de3be4ac5c48 | 10699106 | `2026-04-13T02:10:25+00:00` | `2026-04-12 21:10:25 (Lima)` | +0.62h |
| 2 | PEREZ AGREDA felicita Melissa FIR 09497992 sw 59b204f30d845f7f882f7b6516f939006f1dae33 | 09497992 | `2026-04-13T02:11:07+00:00` | `2026-04-12 21:11:07 (Lima)` | +0.63h |
| 3 | QUISPE TAQUIRE nayelis Abigail FIR 61042869 sw ca85b6eb4e029412f97139a1e8597285b8b6e633 | 61042869 | `2026-04-13T02:11:23+00:00` | `2026-04-12 21:11:23 (Lima)` | +0.64h |
| 4 | QUILCA REYES frida Martha FIR 09386537 sw b403cfb99553610285350cf7b7e95717c16bb33c | 09386537 | `2026-04-13T02:11:51+00:00` | `2026-04-12 21:11:51 (Lima)` | +0.65h |
| 5 | HUETE GARCIA haydee Hermelinda FIR 06107936 sw 9fe3c7c26d26793bcbbabb536f7f3e8a4723a095 | 06107936 | `2026-04-13T02:12:07+00:00` | `2026-04-12 21:12:07 (Lima)` | +0.65h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **062143**
2. Descargar el PDF del acta
3. Verificar SHA-256: `dd91ad82ff0f88265dc046a22450ecf27310545dfb37e853d62c88ba54cee414`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
