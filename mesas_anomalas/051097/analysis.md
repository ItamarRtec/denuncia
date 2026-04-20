# Mesa 051097 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.970414+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: PONTIFICIA UNIVERSIDAD CATOLICA DEL PERU - ESCUELA DE NEGOCIOS CENTRUM PUCP (código 14133)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 279
- Votos válidos: 273
- Participación: 93.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:27:59+00:00` | `2026-04-12 20:27:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:27:59+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:27:59+00:00` | `2026-04-12 20:27:59 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:15:15+00:00` | `2026-04-13 00:15:15 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:15:32+00:00` | `2026-04-13 00:15:32 (Lima)` |
| Última firma humana | `2026-04-13T05:16:19+00:00` | `2026-04-13 00:16:19 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.79 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:27:59 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:15:32 (Lima), es decir **3.79 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:27:57+00:00` | `2026-04-12 20:27:57 (Lima)` | -0.00h |
| 1 | MARQUEZ MARTINEZ valerie Antuane Giovanna FIR 45402274 sw d18374df20a2a4fb0df02081f65888a944b0a9db | 45402274 | `2026-04-13T05:15:32+00:00` | `2026-04-13 00:15:32 (Lima)` | +3.79h |
| 2 | LOZANO MEZA yanira Margarita FIR 10651050 sw 32eb7278591eb5fc494617f8eeffbfdabda32f84 | 10651050 | `2026-04-13T05:15:51+00:00` | `2026-04-13 00:15:51 (Lima)` | +3.80h |
| 3 | MACHER ARAGUNDE rodolfo Jose FIR 08772734 sw 043ed5f8efe9203428f86afcafbcb674c0964d8c | 08772734 | `2026-04-13T05:16:19+00:00` | `2026-04-13 00:16:19 (Lima)` | +3.81h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051097**
2. Descargar el PDF del acta
3. Verificar SHA-256: `b9990182a3e972b5b377c55fe857d7dadee56b4785a2fbe3e240b904f23587ce`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
