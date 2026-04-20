# Mesa 052516 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.802800+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IE 7073 SANTA ROSA DE LIMA (código 3264)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 237
- Votos válidos: 209
- Participación: 79.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:08:30+00:00` | `2026-04-12 20:08:30 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:08:30+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:08:30+00:00` | `2026-04-12 20:08:30 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T01:53:09+00:00` | `2026-04-12 20:53:09 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T01:53:27+00:00` | `2026-04-12 20:53:27 (Lima)` |
| Última firma humana | `2026-04-13T01:55:09+00:00` | `2026-04-12 20:55:09 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.75 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:08:30 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 20:53:27 (Lima), es decir **0.75 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:08:28+00:00` | `2026-04-12 20:08:28 (Lima)` | -0.00h |
| 1 | YUPANQUI CHAWIN flor De Maria FIR 70536152 sw cf4f920d50e0f22745b901c09fbae08a1de7c03b | 70536152 | `2026-04-13T01:53:27+00:00` | `2026-04-12 20:53:27 (Lima)` | +0.75h |
| 2 | ZEGARRA ALVARADO luis Alberto FIR 80391585 sw 699e03ec8020e68715313bb35d746a75eac9fd02 | 80391585 | `2026-04-13T01:54:03+00:00` | `2026-04-12 20:54:03 (Lima)` | +0.76h |
| 3 | YARASCA MILLAN karim Danitza FIR 09838859 sw fb01e4250495855a3049d7026882368ddce01e3d | 09838859 | `2026-04-13T01:55:09+00:00` | `2026-04-12 20:55:09 (Lima)` | +0.78h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **052516**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4d9714a25160a1b8c37bfa5d3869ce3cb5388e7faa7782b6d7d9d2a527dc25d8`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
