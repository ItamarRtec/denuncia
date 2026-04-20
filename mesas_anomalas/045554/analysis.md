# Mesa 045554 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.051681+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PACHACÁMAC
- **Local de votación**: IE ISAIAS ARDILES (código 3006)
- **Ubigeo**: 140116

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 262
- Votos válidos: 221
- Participación: 87.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T04:12:18+00:00` | `2026-04-12 23:12:18 (Lima)` |
| `C` | Contabilizada | `2026-04-13T03:58:25+00:00` | `2026-04-12 22:58:25 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T04:12:18+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T04:12:18+00:00` | `2026-04-12 23:12:18 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T15:26:50+00:00` | `2026-04-13 10:26:50 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T15:31:52+00:00` | `2026-04-13 10:31:52 (Lima)` |
| Última firma humana | `2026-04-13T15:34:30+00:00` | `2026-04-13 10:34:30 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.33 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 23:12:18 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 10:31:52 (Lima), es decir **11.33 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:58:23+00:00` | `2026-04-12 22:58:23 (Lima)` | -0.23h |
| 1 | CUYA DIAZ felipe Emilio FIR 07893159 sw 6a7f96893a71babf8b839f708cbfe3365d665b65 | 07893159 | `2026-04-13T15:31:52+00:00` | `2026-04-13 10:31:52 (Lima)` | +11.33h |
| 2 | CUARESMA VALVERDE maribel Felisa FIR 45059832 sw 6bd7b4d4068dcb753711edbcac773874c70a30aa | 45059832 | `2026-04-13T15:34:07+00:00` | `2026-04-13 10:34:07 (Lima)` | +11.36h |
| 3 | CHUMPITAZ MENDOZA edwin Alex FIR 07893978 sw 52b8211c76c49dab46ee171df5deeab2d3754ac7 | 07893978 | `2026-04-13T15:34:30+00:00` | `2026-04-13 10:34:30 (Lima)` | +11.37h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045554**
2. Descargar el PDF del acta
3. Verificar SHA-256: `82efea673d5d71795f4da865d604963cc4aa5d4bd3e718fefb37958257929c8e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
