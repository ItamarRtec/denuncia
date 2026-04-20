# Mesa 043042 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.288324+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA VICTORIA
- **Local de votación**: IE 020 MADRE TERESA DE CALCUTA (código 53361)
- **Ubigeo**: 140109

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 218
- Votos válidos: 202
- Participación: 72.91%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:11:02+00:00` | `2026-04-12 21:11:02 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:11:02+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:11:02+00:00` | `2026-04-12 21:11:02 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:14:59+00:00` | `2026-04-13 00:14:59 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:17:28+00:00` | `2026-04-13 00:17:28 (Lima)` |
| Última firma humana | `2026-04-13T05:20:44+00:00` | `2026-04-13 00:20:44 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.11 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:11:02 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:17:28 (Lima), es decir **3.11 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:10:59+00:00` | `2026-04-12 21:10:59 (Lima)` | -0.00h |
| 1 | TELLO MEDINA michael Edwin FIR 21465415 sw 2a5e81b5494cbe0aab08b4c0c21638403086a864 | 21465415 | `2026-04-13T05:17:28+00:00` | `2026-04-13 00:17:28 (Lima)` | +3.11h |
| 2 | VEGA FRANCO maria Margarita FIR 10783605 sw e28d973bf7c37acee8cc5ea1e38270d626011039 | 10783605 | `2026-04-13T05:17:51+00:00` | `2026-04-13 00:17:51 (Lima)` | +3.11h |
| 3 | SILVA MARTINEZ alfredo FIR 06943132 sw 209796024a1e40dad7f1796fcab7e7fba207f5c8 | 06943132 | `2026-04-13T05:18:23+00:00` | `2026-04-13 00:18:23 (Lima)` | +3.12h |
| 4 | CERQUIN SACAICO mauricio Jose Maria FIR 74883284 sw eb208977d93dd39fd7b73fc1aa384198c5ab2eae | 74883284 | `2026-04-13T05:19:51+00:00` | `2026-04-13 00:19:51 (Lima)` | +3.15h |
| 5 | HUANCA QUISPE hugo Cesar FIR 07493596 sw 12e3b0f35339ec315c4128ed8780036ead6726a8 | 07493596 | `2026-04-13T05:20:44+00:00` | `2026-04-13 00:20:44 (Lima)` | +3.16h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **043042**
2. Descargar el PDF del acta
3. Verificar SHA-256: `d67baeb7ce4c9322ce565bd4830e6982df51bb30fb350872acb66545c2e1f79f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
