# Mesa 036292 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.339377+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE EMBLEMATICA HIPOLITO UNANUE (código 2659)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 214
- Votos válidos: 195
- Participación: 71.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:49:03+00:00` | `2026-04-12 20:49:03 (Lima)` |
| `C` | Contabilizada | `2026-04-13T01:44:45+00:00` | `2026-04-12 20:44:45 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:49:03+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:49:03+00:00` | `2026-04-12 20:49:03 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:22:51+00:00` | `2026-04-13 00:22:51 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:23:05+00:00` | `2026-04-13 00:23:05 (Lima)` |
| Última firma humana | `2026-04-13T05:23:39+00:00` | `2026-04-13 00:23:39 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.57 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:49:03 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:23:05 (Lima), es decir **3.57 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:44:43+00:00` | `2026-04-12 20:44:43 (Lima)` | -0.07h |
| 1 | SOLORZANO YAURIMAN adriana FIR 76388047 sw 1fa20c0e1a1d8b70e16c4f6f6c858899a92c5bc4 | 76388047 | `2026-04-13T05:23:05+00:00` | `2026-04-13 00:23:05 (Lima)` | +3.57h |
| 2 | SOSA CERNA diana Elizabeth FIR 09464218 sw 72073e179449001a8ebbcbd68bd5bad10d205d7d | 09464218 | `2026-04-13T05:23:25+00:00` | `2026-04-13 00:23:25 (Lima)` | +3.57h |
| 3 | SILVA MERINO jorge Augusto FIR 09959591 sw f18572be64aa7a402dc75ec9865cdf12a71bd4c4 | 09959591 | `2026-04-13T05:23:39+00:00` | `2026-04-13 00:23:39 (Lima)` | +3.58h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036292**
2. Descargar el PDF del acta
3. Verificar SHA-256: `25fa7585d4524843548ec2b50bdfc8292f472bc0a375a18fd047fcb9cb016bda`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
