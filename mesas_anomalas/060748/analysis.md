# Mesa 060748 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.586800+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LOS OLIVOS
- **Local de votación**: IE 2078 NUESTRA SEÑORA DE LOURDES (código 3546)
- **Ubigeo**: 140142

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 251
- Votos válidos: 233
- Participación: 83.946%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:55:43+00:00` | `2026-04-12 20:55:43 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:55:43+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:55:43+00:00` | `2026-04-12 20:55:43 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T08:09:33+00:00` | `2026-04-13 03:09:33 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T08:10:17+00:00` | `2026-04-13 03:10:17 (Lima)` |
| Última firma humana | `2026-04-13T08:10:40+00:00` | `2026-04-13 03:10:40 (Lima)` |

**Brecha primera firma humana vs publicación:** **+6.24 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:55:43 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 03:10:17 (Lima), es decir **6.24 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:55:40+00:00` | `2026-04-12 20:55:40 (Lima)` | -0.00h |
| 1 | PINTO CHALLAPA yeny FIR 41166497 sw 156fdaf2fa48c8be6654a0bf81c12ecce073cba3 | 41166497 | `2026-04-13T08:10:17+00:00` | `2026-04-13 03:10:17 (Lima)` | +6.24h |
| 2 | PISCO DEL AGUILA klid FIR 42627357 sw 627db3e2ac9a05cf5ca518000c1911833d737557 | 42627357 | `2026-04-13T08:10:30+00:00` | `2026-04-13 03:10:30 (Lima)` | +6.25h |
| 3 | PEREZ QUISPE celestino FIR 25729391 sw c6207dc545b33ee109f047898159e80e74e84bef | 25729391 | `2026-04-13T08:10:40+00:00` | `2026-04-13 03:10:40 (Lima)` | +6.25h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **060748**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c389c121126c8d7475faa0011dd0e367c6aa0470fe1f41887fa39b480da2e2ff`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
