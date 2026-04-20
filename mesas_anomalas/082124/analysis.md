# Mesa 082124 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.302915+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CALLAO
- **Local de votación**: IEP DIVINO MAESTRO (código 52998)
- **Ubigeo**: 240101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 199
- Votos válidos: 154
- Participación: 66.555%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:43:25+00:00` | `2026-04-12 20:43:25 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:43:25+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:43:25+00:00` | `2026-04-12 20:43:25 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:30:15+00:00` | `2026-04-12 22:30:15 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:31:25+00:00` | `2026-04-12 22:31:25 (Lima)` |
| Última firma humana | `2026-04-13T03:32:51+00:00` | `2026-04-12 22:32:51 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.80 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:43:25 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:31:25 (Lima), es decir **1.80 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:43:22+00:00` | `2026-04-12 20:43:22 (Lima)` | -0.00h |
| 1 | PFLUCKER GUTTY patricia Beatriz FIR 19239051 sw 881cbe4b7b5cd20847d4aadbf0be3dca9be1e693 | 19239051 | `2026-04-13T03:31:25+00:00` | `2026-04-12 22:31:25 (Lima)` | +1.80h |
| 2 | ZEVALLOS CHUMBIRAY patricia Milagros FIR 80236694 sw 6f6e0d86732a37cdcc53ed1beedadf579217d752 | 80236694 | `2026-04-13T03:31:48+00:00` | `2026-04-12 22:31:48 (Lima)` | +1.81h |
| 3 | CABALLERO CASTRO yolanda FIR 25478798 sw ce4696d48cb77c086d72bd5793b201fd2fb76073 | 25478798 | `2026-04-13T03:32:51+00:00` | `2026-04-12 22:32:51 (Lima)` | +1.82h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082124**
2. Descargar el PDF del acta
3. Verificar SHA-256: `caec9d7028729bb8660149e69b0b56c4e8bc3571d3518d394f416769a4154c88`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
