# Mesa 052449 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.481357+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IE 7055 TUPAC AMARU II (código 3262)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 248
- Votos válidos: 212
- Participación: 82.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:42:54+00:00` | `2026-04-12 21:42:54 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:42:54+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:42:54+00:00` | `2026-04-12 21:42:54 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:52:55+00:00` | `2026-04-13 08:52:55 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:53:16+00:00` | `2026-04-13 08:53:16 (Lima)` |
| Última firma humana | `2026-04-13T13:53:52+00:00` | `2026-04-13 08:53:52 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.17 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:42:54 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:53:16 (Lima), es decir **11.17 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:37:26+00:00` | `2026-04-12 21:37:26 (Lima)` | -0.09h |
| 1 | VARGAS PAREDES sara Elizabeth FIR 10706415 sw 0c41bf67a19f7f42a8c566f20faeb3775573405a | 10706415 | `2026-04-13T13:53:16+00:00` | `2026-04-13 08:53:16 (Lima)` | +11.17h |
| 2 | VALLEJOS VASQUEZ pamela Katherine FIR 47835431 sw 7713a7a3cd8b15665fa60ad912dac9b5d8a85130 | 47835431 | `2026-04-13T13:53:36+00:00` | `2026-04-13 08:53:36 (Lima)` | +11.18h |
| 3 | VASQUEZ HUAPAYA jose Orlando FIR 43471478 sw c5e61f5b5c4611e7e28044c3e95e5330e54d3e2f | 43471478 | `2026-04-13T13:53:52+00:00` | `2026-04-13 08:53:52 (Lima)` | +11.18h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **052449**
2. Descargar el PDF del acta
3. Verificar SHA-256: `9f945817d47018e728c09a3eebb13652191bf6ab8934e587a42173b57fcbaa3b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
