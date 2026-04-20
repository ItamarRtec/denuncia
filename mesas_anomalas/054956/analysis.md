# Mesa 054956 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.705816+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 6089 JORGE BASADRE GROHMANN (código 3354)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 228
- Votos válidos: 207
- Participación: 76.254%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:36:55+00:00` | `2026-04-12 21:36:55 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:32:37+00:00` | `2026-04-12 21:32:37 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:36:55+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:36:55+00:00` | `2026-04-12 21:36:55 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:27:04+00:00` | `2026-04-13 08:27:04 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:27:50+00:00` | `2026-04-13 08:27:50 (Lima)` |
| Última firma humana | `2026-04-13T13:31:14+00:00` | `2026-04-13 08:31:14 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.85 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:36:55 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:27:50 (Lima), es decir **10.85 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:32:34+00:00` | `2026-04-12 21:32:34 (Lima)` | -0.07h |
| 1 | HIDALGO GALOC sergio Jamil FIR 75680699 sw 7417bc1a49d1230fcde4fb7ca20e61c225afe195 | 75680699 | `2026-04-13T13:27:50+00:00` | `2026-04-13 08:27:50 (Lima)` | +10.85h |
| 2 | HUACHOS PAREDES sebastian Ricardo FIR 77069286 sw 81cfd16b36b0de517a480412ffd9960a395242ff | 77069286 | `2026-04-13T13:28:05+00:00` | `2026-04-13 08:28:05 (Lima)` | +10.85h |
| 3 | HERRERA MEDRANO enrique Martin FIR 10008802 sw fd87eb13c5508d94347ce4ff39602a211a24ed12 | 10008802 | `2026-04-13T13:28:25+00:00` | `2026-04-13 08:28:25 (Lima)` | +10.86h |
| 4 | RUIZ SAAVEDRA roy Anthony FIR 71031711 sw 1d42a789b22778bed6437110d198e10d03f7051b | 71031711 | `2026-04-13T13:31:14+00:00` | `2026-04-13 08:31:14 (Lima)` | +10.91h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054956**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2bedef2113be3bae158f5f968a1e5ddd47ddb5e826d1a3768af2bd580f9c6ccb`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
