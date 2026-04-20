# Mesa 082326 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.777980+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CALLAO
- **Local de votación**: LOSA DEPORTIVA JUAN VELASCO ALVARADO (código 54580)
- **Ubigeo**: 240101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 213
- Votos válidos: 187
- Participación: 71.237%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:28:45+00:00` | `2026-04-12 21:28:45 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:28:45+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:28:45+00:00` | `2026-04-12 21:28:45 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:42:46+00:00` | `2026-04-13 07:42:46 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:58:21+00:00` | `2026-04-13 07:58:21 (Lima)` |
| Última firma humana | `2026-04-13T13:02:40+00:00` | `2026-04-13 08:02:40 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.49 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:28:45 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:58:21 (Lima), es decir **10.49 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:27:24+00:00` | `2026-04-12 21:27:24 (Lima)` | -0.02h |
| 1 | CODARLUPO ALEJOS jose Luis FIR 25525763 sw 54148710982a0d781fa8879ef0628648807ff122 | 25525763 | `2026-04-13T12:58:21+00:00` | `2026-04-13 07:58:21 (Lima)` | +10.49h |
| 2 | CANO ESTRADA cielo Cristina FIR 73263973 sw 5def83f115b4d7e973ba9863c06201c17c9ad4f1 | 73263973 | `2026-04-13T13:00:45+00:00` | `2026-04-13 08:00:45 (Lima)` | +10.53h |
| 3 | CHAVEZ RAMIREZ ana Paula FIR 72578003 sw b83a320dac44f9d46bcaa27c6eb7de5167f3c055 | 72578003 | `2026-04-13T13:02:40+00:00` | `2026-04-13 08:02:40 (Lima)` | +10.57h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082326**
2. Descargar el PDF del acta
3. Verificar SHA-256: `83f838e295c46f5a1c81fd7495558098fac5f667ec41cd2458e2aea73805f3e4`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
