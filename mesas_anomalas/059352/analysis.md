# Mesa 059352 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.163398+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN BORJA
- **Local de votación**: IEP MARIA REICHE (código 54280)
- **Ubigeo**: 140140

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 252
- Votos válidos: 244
- Participación: 84.281%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:48:16+00:00` | `2026-04-12 20:48:16 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:48:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:48:16+00:00` | `2026-04-12 20:48:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:47:49+00:00` | `2026-04-13 00:47:49 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:48:24+00:00` | `2026-04-13 00:48:24 (Lima)` |
| Última firma humana | `2026-04-13T05:49:00+00:00` | `2026-04-13 00:49:00 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.00 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:48:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:48:24 (Lima), es decir **4.00 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:48:12+00:00` | `2026-04-12 20:48:12 (Lima)` | -0.00h |
| 1 | HERRERA GUERRA daniel Andres FIR 09542620 sw fcbb4c567e58755bdbb23061bcc858a39d34856c | 09542620 | `2026-04-13T05:48:24+00:00` | `2026-04-13 00:48:24 (Lima)` | +4.00h |
| 2 | HINOSTROZA BARRIONUEVO victor FIR 20064081 sw 180c014402726904e265a4cc0eb41e5289cc9f5a | 20064081 | `2026-04-13T05:48:44+00:00` | `2026-04-13 00:48:44 (Lima)` | +4.01h |
| 3 | IPENZA ALDAZABAL edson Pavel FIR 24004927 sw 8b410318248b22b50faa3d59e3f53b70130596ea | 24004927 | `2026-04-13T05:49:00+00:00` | `2026-04-13 00:49:00 (Lima)` | +4.01h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **059352**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3426572277eb85fab3a92f80766de179ded78e695d58520b523d6005007562a8`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
