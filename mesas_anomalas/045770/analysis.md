# Mesa 045770 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.175028+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PACHACÁMAC
- **Local de votación**: IEP VIRGEN DE LA PUERTA (código 54006)
- **Ubigeo**: 140116

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 243
- Votos válidos: 203
- Participación: 81.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:11:49+00:00` | `2026-04-12 21:11:49 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:11:49+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:11:49+00:00` | `2026-04-12 21:11:49 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:32:31+00:00` | `2026-04-13 00:32:31 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:32:48+00:00` | `2026-04-13 00:32:48 (Lima)` |
| Última firma humana | `2026-04-13T05:33:09+00:00` | `2026-04-13 00:33:09 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.35 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:11:49 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:32:48 (Lima), es decir **3.35 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:11:47+00:00` | `2026-04-12 21:11:47 (Lima)` | -0.00h |
| 1 | QUINTANA HUAMAN cesar Augusto FIR 09442305 sw cf708c33a50d15e09fa692ce4615a661da294c36 | 09442305 | `2026-04-13T05:32:48+00:00` | `2026-04-13 00:32:48 (Lima)` | +3.35h |
| 2 | QUISPE QUISPE maruja Dominga FIR 23946857 sw c4b37ec9612ac97523c988127410ac05fb8a0b3b | 23946857 | `2026-04-13T05:33:09+00:00` | `2026-04-13 00:33:09 (Lima)` | +3.36h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045770**
2. Descargar el PDF del acta
3. Verificar SHA-256: `05aa350fad528ada5db9f3d76d099b0582886725573647bdfda87d4b85898fe9`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
