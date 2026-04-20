# Mesa 051521 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.115275+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: ESCUELA DE EDUCACION SUPERIOR PEDAGOGICA PUBLICA MONTERRICO (código 54054)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 183
- Votos válidos: 175
- Participación: 61.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:59:36+00:00` | `2026-04-12 21:59:36 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:59:36+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:59:36+00:00` | `2026-04-12 21:59:36 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T07:07:56+00:00` | `2026-04-13 02:07:56 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T07:08:21+00:00` | `2026-04-13 02:08:21 (Lima)` |
| Última firma humana | `2026-04-13T07:09:44+00:00` | `2026-04-13 02:09:44 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.15 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:59:36 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 02:08:21 (Lima), es decir **4.15 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:59:33+00:00` | `2026-04-12 21:59:33 (Lima)` | -0.00h |
| 1 | SUAREZ VELARDE carla Hortencia FIR 44388996 sw dad37a73906f910589470dd660e5bb1f0a72d8ee | 44388996 | `2026-04-13T07:08:21+00:00` | `2026-04-13 02:08:21 (Lima)` | +4.15h |
| 2 | SOTO CEBRIAN jorge Alejandro FIR 08808091 sw 54ecab83aaf1f7a378e59ebadfb3e1c166bdeec3 | 08808091 | `2026-04-13T07:08:40+00:00` | `2026-04-13 02:08:40 (Lima)` | +4.15h |
| 3 | SUBAUSTE URIBE claudia Celia FIR 07904007 sw 7e41bbc1bfea4831a8580ad578aa11b905a2de4e | 07904007 | `2026-04-13T07:09:03+00:00` | `2026-04-13 02:09:03 (Lima)` | +4.16h |
| 4 | AGURTO SCHROTH camila FIR 43399322 sw 42a98bc2a34f9a10f9b8e9a871c0092c3308ea13 | 43399322 | `2026-04-13T07:09:44+00:00` | `2026-04-13 02:09:44 (Lima)` | +4.17h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051521**
2. Descargar el PDF del acta
3. Verificar SHA-256: `1da67a2132cafcc874e4a3772018498e91894c73cb345c65495b1fa372fc742d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
