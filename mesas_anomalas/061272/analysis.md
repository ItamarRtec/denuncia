# Mesa 061272 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.161561+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LOS OLIVOS
- **Local de votación**: IEP CRISTO REY DE REYES (código 17390)
- **Ubigeo**: 140142

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 234
- Votos válidos: 216
- Participación: 78.261%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:14:40+00:00` | `2026-04-12 21:14:40 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:14:40+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:14:40+00:00` | `2026-04-12 21:14:40 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:43:38+00:00` | `2026-04-13 08:43:38 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:43:59+00:00` | `2026-04-13 08:43:59 (Lima)` |
| Última firma humana | `2026-04-13T13:44:48+00:00` | `2026-04-13 08:44:48 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.49 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:14:40 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:43:59 (Lima), es decir **11.49 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:14:37+00:00` | `2026-04-12 21:14:37 (Lima)` | -0.00h |
| 1 | VITE PIMENTEL emmy Hilary FIR 72962641 sw 4b3b92c284fa87044cdcc7588bdf1f3a304f73f3 | 72962641 | `2026-04-13T13:43:59+00:00` | `2026-04-13 08:43:59 (Lima)` | +11.49h |
| 2 | VEGA SEDANO juan Diego FIR 46827671 sw 02202a2c6a3f57fd53600d600dc854faad1d4844 | 46827671 | `2026-04-13T13:44:15+00:00` | `2026-04-13 08:44:15 (Lima)` | +11.49h |
| 3 | VILLALTA SALAZAR segundo Rogelio FIR 43441261 sw 5e26165468284b4a64dfd61834b4fc3afeec1af8 | 43441261 | `2026-04-13T13:44:48+00:00` | `2026-04-13 08:44:48 (Lima)` | +11.50h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061272**
2. Descargar el PDF del acta
3. Verificar SHA-256: `165caddbcca85ee4878ad5b69cd2043a098383b513ed0259e255f80dbd7df097`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
