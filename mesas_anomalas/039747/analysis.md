# Mesa 039747 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.356742+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CARABAYLLO
- **Local de votación**: IEP SANTIAGO ANTUNEZ DE MAYOLO (código 12913)
- **Ubigeo**: 140105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 245
- Votos válidos: 224
- Participación: 81.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:39:56+00:00` | `2026-04-12 20:39:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:39:56+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:39:56+00:00` | `2026-04-12 20:39:56 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:42:02+00:00` | `2026-04-12 22:42:02 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:43:55+00:00` | `2026-04-12 22:43:55 (Lima)` |
| Última firma humana | `2026-04-13T03:44:46+00:00` | `2026-04-12 22:44:46 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.07 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:39:56 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:43:55 (Lima), es decir **2.07 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:39:54+00:00` | `2026-04-12 20:39:54 (Lima)` | -0.00h |
| 1 | ZABALETA YOPLAC noelita FIR 48105717 sw 03d25dd9ccdac75eb37ce351ff6c147872ca00c2 | 48105717 | `2026-04-13T03:43:55+00:00` | `2026-04-12 22:43:55 (Lima)` | +2.07h |
| 2 | VARGAS SOTELO barbara Luzgarda FIR 06256928 sw 5ed565f100b467d214aad46b86baba175091eda0 | 06256928 | `2026-04-13T03:44:17+00:00` | `2026-04-12 22:44:17 (Lima)` | +2.07h |
| 3 | VILLAFUERTE VENTURA macarena Samantha FIR 70954232 sw 603e2864bb6765580c2b70278499b7388ad126be | 70954232 | `2026-04-13T03:44:46+00:00` | `2026-04-12 22:44:46 (Lima)` | +2.08h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **039747**
2. Descargar el PDF del acta
3. Verificar SHA-256: `6c8420319bf8fb617e89b971f73aae90c964a3914b5d05bef64fa58cfb644a2d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
