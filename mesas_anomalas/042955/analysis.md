# Mesa 042955 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.259113+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA VICTORIA
- **Local de votación**: UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS - ESCUELA DE OBSTETRICIA Y ESCUELA DE NUTRICIÓN (código 2911)
- **Ubigeo**: 140109

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 241
- Votos válidos: 197
- Participación: 80.602%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:37:09+00:00` | `2026-04-12 20:37:09 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:37:09+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:37:09+00:00` | `2026-04-12 20:37:09 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:37:58+00:00` | `2026-04-12 21:37:58 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:38:25+00:00` | `2026-04-12 21:38:25 (Lima)` |
| Última firma humana | `2026-04-13T02:38:47+00:00` | `2026-04-12 21:38:47 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.02 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:37:09 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:38:25 (Lima), es decir **1.02 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:37:07+00:00` | `2026-04-12 20:37:07 (Lima)` | -0.00h |
| 1 | VASQUEZ FACIO katherine Maria FIR 74988866 sw 65ef86657531f20d3fd404ed0d6efec8915edac7 | 74988866 | `2026-04-13T02:38:25+00:00` | `2026-04-12 21:38:25 (Lima)` | +1.02h |
| 2 | VASQUEZ NINA arturo FIR 07509928 sw c913b12e926844ea50e8b4258d8e35523f15b223 | 07509928 | `2026-04-13T02:38:37+00:00` | `2026-04-12 21:38:37 (Lima)` | +1.02h |
| 3 | YNFANTES ROJAS fermin Andres FIR 44517201 sw 9fa3a97563ded3b045e27e93c54a2fb78b5abd50 | 44517201 | `2026-04-13T02:38:47+00:00` | `2026-04-12 21:38:47 (Lima)` | +1.03h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042955**
2. Descargar el PDF del acta
3. Verificar SHA-256: `63141d50751e396939287d08eaf7ec7d7e23e1405da023d44006ffb3fc289aa6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
