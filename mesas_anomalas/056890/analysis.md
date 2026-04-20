# Mesa 056890 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.447249+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IE 149 CAPITAN PNP JORGE CIEZA LACHOS (código 3441)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 250
- Votos válidos: 228
- Participación: 83.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:52:24+00:00` | `2026-04-12 20:52:24 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:52:24+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:52:24+00:00` | `2026-04-12 20:52:24 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:55:51+00:00` | `2026-04-12 21:55:51 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:56:02+00:00` | `2026-04-12 21:56:02 (Lima)` |
| Última firma humana | `2026-04-13T02:56:25+00:00` | `2026-04-12 21:56:25 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.06 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:52:24 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:56:02 (Lima), es decir **1.06 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:52:22+00:00` | `2026-04-12 20:52:22 (Lima)` | -0.00h |
| 1 | VASQUEZ TAIPE ariana Milagros FIR 60978504 sw 695fe792d09cd618572b1efa092fa38f13e161e1 | 60978504 | `2026-04-13T02:56:02+00:00` | `2026-04-12 21:56:02 (Lima)` | +1.06h |
| 2 | VILCARROMERO DAVILA pedro Jesus Alexander FIR 75323657 sw 2dccac65eaf92209794b8e9290cf9e3b4ab6c6e3 | 75323657 | `2026-04-13T02:56:14+00:00` | `2026-04-12 21:56:14 (Lima)` | +1.06h |
| 3 | VALLE ECHEVERRIA alan Orlando FIR 42006336 sw 35ae0fea41dbbb04e4a17b55fe6512cb4621073c | 42006336 | `2026-04-13T02:56:25+00:00` | `2026-04-12 21:56:25 (Lima)` | +1.07h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **056890**
2. Descargar el PDF del acta
3. Verificar SHA-256: `9dd922adc307ececbc674a340631c9da9eab64e8a768c7f38aafbdf43b55ffd3`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
