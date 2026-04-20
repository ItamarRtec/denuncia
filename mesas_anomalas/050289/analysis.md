# Mesa 050289 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.097344+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: COLEGIO SACO OLIVEROS DE SAN MIGUEL (código 52595)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 243
- Votos válidos: 231
- Participación: 81.271%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:31:38+00:00` | `2026-04-12 20:31:38 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:31:38+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:31:38+00:00` | `2026-04-12 20:31:38 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T11:33:55+00:00` | `2026-04-13 06:33:55 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T11:34:20+00:00` | `2026-04-13 06:34:20 (Lima)` |
| Última firma humana | `2026-04-13T11:35:19+00:00` | `2026-04-13 06:35:19 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.04 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:31:38 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 06:34:20 (Lima), es decir **10.04 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:31:36+00:00` | `2026-04-12 20:31:36 (Lima)` | -0.00h |
| 1 | BUSTAMANTE POEMAPE thalia Alessandra FIR 70173867 sw c8d9263a00f320f9b43755b94c44167ed8ae7181 | 70173867 | `2026-04-13T11:34:20+00:00` | `2026-04-13 06:34:20 (Lima)` | +10.04h |
| 2 | BURGOS CASTRO henrry Ronal FIR 07398912 sw 241c3dfd76e9c075f7887403356575e99a17554a | 07398912 | `2026-04-13T11:34:53+00:00` | `2026-04-13 06:34:53 (Lima)` | +10.05h |
| 3 | BONILLA RUJEL bryditt Del Pilar FIR 00241673 sw ed244f3a7753debd3fd417a583edb448b110fc55 | 00241673 | `2026-04-13T11:35:19+00:00` | `2026-04-13 06:35:19 (Lima)` | +10.06h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050289**
2. Descargar el PDF del acta
3. Verificar SHA-256: `f3723ddf8daf17c140fc58a10c3d2c8e2e071813d0ad31f5b1271a9dcc8a2455`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
