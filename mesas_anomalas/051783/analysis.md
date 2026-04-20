# Mesa 051783 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.548159+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: IE NUESTRA SEÑORA DE LOURDES (código 3233)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 238
- Votos válidos: 214
- Participación: 79.599%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:33:26+00:00` | `2026-04-12 20:33:26 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:33:26+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:33:26+00:00` | `2026-04-12 20:33:26 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:56:54+00:00` | `2026-04-12 21:56:54 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:57:10+00:00` | `2026-04-12 21:57:10 (Lima)` |
| Última firma humana | `2026-04-13T02:57:35+00:00` | `2026-04-12 21:57:35 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.40 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:33:26 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:57:10 (Lima), es decir **1.40 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:33:23+00:00` | `2026-04-12 20:33:23 (Lima)` | -0.00h |
| 1 | ARELLANO ROMERO seth Isaac FIR 81695236 sw 5dfeb2edd29f142a234b942974e6ce4bb23d0d82 | 81695236 | `2026-04-13T02:57:10+00:00` | `2026-04-12 21:57:10 (Lima)` | +1.40h |
| 2 | ALVAREZ CARREON itala Elizabeth FIR 71500103 sw 99ff28d68225bc534588d9fe6b66c210d1aa99b5 | 71500103 | `2026-04-13T02:57:23+00:00` | `2026-04-12 21:57:23 (Lima)` | +1.40h |
| 3 | ASCOY VELASQUEZ alex Jorge FIR 44898384 sw 7aa0ed731ff3d98c0e537c13d20158919fd1c3ce | 44898384 | `2026-04-13T02:57:35+00:00` | `2026-04-12 21:57:35 (Lima)` | +1.40h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051783**
2. Descargar el PDF del acta
3. Verificar SHA-256: `bfe6e93690c4936aab965ca26577fc8b250f47addb9d73fc89cfc308d9752485`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
