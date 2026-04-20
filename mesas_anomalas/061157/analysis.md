# Mesa 061157 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.956463+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LOS OLIVOS
- **Local de votación**: IE 2005 LOS OLIVOS (código 13331)
- **Ubigeo**: 140142

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 266
- Votos válidos: 248
- Participación: 88.963%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:19:54+00:00` | `2026-04-12 20:19:54 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:19:54+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:19:54+00:00` | `2026-04-12 20:19:54 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:26:21+00:00` | `2026-04-12 21:26:21 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:26:48+00:00` | `2026-04-12 21:26:48 (Lima)` |
| Última firma humana | `2026-04-13T02:27:51+00:00` | `2026-04-12 21:27:51 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.11 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:19:54 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:26:48 (Lima), es decir **1.11 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:19:51+00:00` | `2026-04-12 20:19:51 (Lima)` | -0.00h |
| 1 | DE LA CRUZ ACHULLA victoria Gregoria FIR 08677229 sw 64b64792e659fccb6d197900e8652cbfbdb0d134 | 08677229 | `2026-04-13T02:26:48+00:00` | `2026-04-12 21:26:48 (Lima)` | +1.11h |
| 2 | CASTRO MENDOZA daira Ayelen FIR 73122184 sw cb4dfe0d2916296011bd05eb9a5f0837d59041b0 | 73122184 | `2026-04-13T02:27:03+00:00` | `2026-04-12 21:27:03 (Lima)` | +1.12h |
| 3 | CASTRO MAMANI claudia Anabel FIR 74719283 sw d129e5a1f2cedf8ca8ec58c52a292cff6217838e | 74719283 | `2026-04-13T02:27:15+00:00` | `2026-04-12 21:27:15 (Lima)` | +1.12h |
| 4 | CASTRO CHUNGA DE CIEZA selene Elizabeth FIR 25683978 sw abf847749af9ed7a0256a1b617e3756466358b1c | 25683978 | `2026-04-13T02:27:51+00:00` | `2026-04-12 21:27:51 (Lima)` | +1.13h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061157**
2. Descargar el PDF del acta
3. Verificar SHA-256: `ff2766afb2d2044250f5ac14a6de7bdadd9b3f323f5e5a2a0f3d032d3a4f11a8`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
