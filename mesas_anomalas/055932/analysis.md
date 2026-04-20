# Mesa 055932 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.503700+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IEP INNOVA SCHOOLS - SAN JUAN DE MIRAFLORES (código 54797)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 231
- Votos válidos: 208
- Participación: 77.258%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:10:22+00:00` | `2026-04-12 21:10:22 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:10:22+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:10:22+00:00` | `2026-04-12 21:10:22 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:35:06+00:00` | `2026-04-12 22:35:06 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:35:33+00:00` | `2026-04-12 22:35:33 (Lima)` |
| Última firma humana | `2026-04-13T03:37:41+00:00` | `2026-04-12 22:37:41 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.42 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:10:22 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:35:33 (Lima), es decir **1.42 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:10:19+00:00` | `2026-04-12 21:10:19 (Lima)` | -0.00h |
| 1 | AYALA MALHABER felix Anderson FIR 75678519 sw b4dbf202a78f9f686f11c1d334921a83ec67c0df | 75678519 | `2026-04-13T03:35:33+00:00` | `2026-04-12 22:35:33 (Lima)` | +1.42h |
| 2 | BARRIAL HUAMAN aracely Anyeli FIR 73800700 sw a97377f03de9d5ef2809f7d9071c5eb816880dcf | 73800700 | `2026-04-13T03:35:56+00:00` | `2026-04-12 22:35:56 (Lima)` | +1.43h |
| 3 | BALBIN ENRIQUE marcos Valentin FIR 78829279 sw 75a7d227a50438e8f8eedae166cd5eac9b16a63a | 78829279 | `2026-04-13T03:36:33+00:00` | `2026-04-12 22:36:33 (Lima)` | +1.44h |
| 4 | FABIAN REYES melania Guadalupe FIR 43466485 sw 1ec0c905a7f761c4f5eb35eadb06eefa0160d44b | 43466485 | `2026-04-13T03:37:02+00:00` | `2026-04-12 22:37:02 (Lima)` | +1.44h |
| 5 | ROJAS PEREZ anamaria Julia FIR 09582605 sw 04786c0b47f80c5c26bdad9b31f6d9bc6b66f8d6 | 09582605 | `2026-04-13T03:37:41+00:00` | `2026-04-12 22:37:41 (Lima)` | +1.46h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055932**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5ce0e2371714b5c3722cc23781137726f640bd02659dbd73dfa0f65c1b66671c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
