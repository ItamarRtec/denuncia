# Mesa 082983 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.910352+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: LA PERLA
- **Local de votación**: ESTADIO CAMPOLO ALCALDE (código 35731)
- **Ubigeo**: 240105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 232
- Votos válidos: 215
- Participación: 77.592%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:32:06+00:00` | `2026-04-12 20:32:06 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:32:06+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:32:06+00:00` | `2026-04-12 20:32:06 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:03:35+00:00` | `2026-04-12 22:03:35 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:03:56+00:00` | `2026-04-12 22:03:56 (Lima)` |
| Última firma humana | `2026-04-13T03:05:06+00:00` | `2026-04-12 22:05:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.53 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:32:06 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:03:56 (Lima), es decir **1.53 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:32:03+00:00` | `2026-04-12 20:32:03 (Lima)` | -0.00h |
| 1 | MORALES GUERRERO lucia Augusta FIR 40222233 sw 1bfe4a88ad9b2fb8a8d65b5fd6d163596690a2ad | 40222233 | `2026-04-13T03:03:56+00:00` | `2026-04-12 22:03:56 (Lima)` | +1.53h |
| 2 | MORA CAHUAS abraham Christian FIR 25778234 sw dd590eb4bd3b5e0a32a6c12281a968b2f85de629 | 25778234 | `2026-04-13T03:04:13+00:00` | `2026-04-12 22:04:13 (Lima)` | +1.54h |
| 3 | MORALES GONZALES judith Yngrid FIR 25775863 sw d69feef02bcbfcc162ab81a670b8b8ce80e54b73 | 25775863 | `2026-04-13T03:04:37+00:00` | `2026-04-12 22:04:37 (Lima)` | +1.54h |
| 4 | RETTEZ ERAZO rock Patrick FIR 42385268 sw cf3bf6b691ebd2f567881f93ec8b5eac81036422 | 42385268 | `2026-04-13T03:05:06+00:00` | `2026-04-12 22:05:06 (Lima)` | +1.55h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082983**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3beb86b3909f81a126cc8bdec2221c513f3399e3a2f769549c8acae58289b2a5`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
