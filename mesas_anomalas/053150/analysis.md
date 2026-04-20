# Mesa 053150 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.650742+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IE PARROQUIAL NUESTRO SALVADOR (código 18293)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 297
- Votos emitidos: 247
- Votos válidos: 209
- Participación: 83.165%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:02:37+00:00` | `2026-04-12 20:02:37 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:02:37+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:02:37+00:00` | `2026-04-12 20:02:37 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:25:19+00:00` | `2026-04-12 21:25:19 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:26:06+00:00` | `2026-04-12 21:26:06 (Lima)` |
| Última firma humana | `2026-04-13T02:26:36+00:00` | `2026-04-12 21:26:36 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.39 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:02:37 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:26:06 (Lima), es decir **1.39 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:02:35+00:00` | `2026-04-12 20:02:35 (Lima)` | -0.00h |
| 1 | HUAMANI CRUZ lorena Anahi FIR 74536523 sw 48ec209b1124307ea0f441ada9339a14ed3b2f13 | 74536523 | `2026-04-13T02:26:06+00:00` | `2026-04-12 21:26:06 (Lima)` | +1.39h |
| 2 | HUARAC QUISPE omar FIR 71081916 sw f15231f8483232597473e676d5aaf1dc4572b121 | 71081916 | `2026-04-13T02:26:21+00:00` | `2026-04-12 21:26:21 (Lima)` | +1.40h |
| 3 | HUAMANI SERRANO edwin Efrain FIR 75357428 sw d61fd252a2bd76d63d76f0806c5f3eb800b0759b | 75357428 | `2026-04-13T02:26:36+00:00` | `2026-04-12 21:26:36 (Lima)` | +1.40h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **053150**
2. Descargar el PDF del acta
3. Verificar SHA-256: `ba92e265d484382b4e0b362b240cd59a499e18b0ee1bf0c610de85b938a7cad2`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
