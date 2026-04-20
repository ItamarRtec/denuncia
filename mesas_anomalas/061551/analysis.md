# Mesa 061551 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.680631+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LOS OLIVOS
- **Local de votación**: IEP INNOVA SCHOOLS SEDE VILLA SOL (código 54809)
- **Ubigeo**: 140142

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 226
- Votos válidos: 203
- Participación: 75.585%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:28:29+00:00` | `2026-04-12 20:28:29 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:28:29+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:28:29+00:00` | `2026-04-12 20:28:29 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:31:28+00:00` | `2026-04-12 22:31:28 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:32:13+00:00` | `2026-04-12 22:32:13 (Lima)` |
| Última firma humana | `2026-04-13T03:32:59+00:00` | `2026-04-12 22:32:59 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.06 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:28:29 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:32:13 (Lima), es decir **2.06 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:28:27+00:00` | `2026-04-12 20:28:27 (Lima)` | -0.00h |
| 1 | COLONIA JAUREGUI jean Carlo Gerardo FIR 45876406 sw fdacad88f2dbc535bd74594246e6c529ec00bed2 | 45876406 | `2026-04-13T03:32:13+00:00` | `2026-04-12 22:32:13 (Lima)` | +2.06h |
| 2 | DAVILA CAHUANA cesar Agustin FIR 45627197 sw b7eac7de331e61dea8897b009cc8f3435d13d796 | 45627197 | `2026-04-13T03:32:25+00:00` | `2026-04-12 22:32:25 (Lima)` | +2.07h |
| 3 | CORONEL PAREDES maribel FIR 09622748 sw 02d0516cb686afcdf9146f670f43efa16d1ecd90 | 09622748 | `2026-04-13T03:32:59+00:00` | `2026-04-12 22:32:59 (Lima)` | +2.08h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061551**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e8b3270578224f6407cce6b06edea7b4d773e13dc5645384a3d689412d9d6aa9`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
