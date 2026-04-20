# Mesa 050826 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.240847+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: MONTERRICO IE APLICACION (código 3209)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 245
- Votos válidos: 238
- Participación: 81.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:53:58+00:00` | `2026-04-12 19:53:58 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:53:58+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:53:58+00:00` | `2026-04-12 19:53:58 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:19:58+00:00` | `2026-04-12 23:19:58 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:20:52+00:00` | `2026-04-12 23:20:52 (Lima)` |
| Última firma humana | `2026-04-13T04:21:51+00:00` | `2026-04-12 23:21:51 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.45 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:53:58 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:20:52 (Lima), es decir **3.45 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:53:56+00:00` | `2026-04-12 19:53:56 (Lima)` | -0.00h |
| 1 | LEEY CASELLA luis Alberto FIR 15857806 sw 249e6ac01e32525ee5da8bb80f3f9affe423bb8c | 15857806 | `2026-04-13T04:20:52+00:00` | `2026-04-12 23:20:52 (Lima)` | +3.45h |
| 2 | HARTLEY SOTOMAYOR alex Christian FIR 10287477 sw 0143bd08a37d4e3bdee259aea0e0dc39f8cce3d9 | 10287477 | `2026-04-13T04:21:06+00:00` | `2026-04-12 23:21:06 (Lima)` | +3.45h |
| 3 | HERRERA MINAYA rodrigo Ernesto FIR 75189679 sw 2fdbbace22adae825bf8c74017b8d706c8060b2b | 75189679 | `2026-04-13T04:21:20+00:00` | `2026-04-12 23:21:20 (Lima)` | +3.46h |
| 4 | GONZALEZ CALDERON eduardo Octavio FIR 17917690 sw a8350d15a34b33068daeb8899b74b0e112363af1 | 17917690 | `2026-04-13T04:21:51+00:00` | `2026-04-12 23:21:51 (Lima)` | +3.46h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050826**
2. Descargar el PDF del acta
3. Verificar SHA-256: `1f25da37b710cc7c733189ba790bd2f6670f9797fd54c9dc168e7105c8e395fe`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
