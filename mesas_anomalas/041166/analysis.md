# Mesa 041166 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.839879+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IEP IVAN PAVLOV (código 50489)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 233
- Votos válidos: 200
- Participación: 77.926%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:03:33+00:00` | `2026-04-12 20:03:33 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:03:33+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:03:33+00:00` | `2026-04-12 20:03:33 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:28:57+00:00` | `2026-04-12 21:28:57 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:29:13+00:00` | `2026-04-12 21:29:13 (Lima)` |
| Última firma humana | `2026-04-13T02:30:04+00:00` | `2026-04-12 21:30:04 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.43 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:03:33 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:29:13 (Lima), es decir **1.43 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:03:31+00:00` | `2026-04-12 20:03:31 (Lima)` | -0.00h |
| 1 | MARTINEZ VERA yosimar Luis FIR 72255251 sw 7f96360cf652098ea0628824bb7e401f91b3320d | 72255251 | `2026-04-13T02:29:13+00:00` | `2026-04-12 21:29:13 (Lima)` | +1.43h |
| 2 | MALLQUI QUISPE jesus David FIR 71937086 sw cd29eef1bcf0667427d64a9adf085056127d288c | 71937086 | `2026-04-13T02:29:31+00:00` | `2026-04-12 21:29:31 (Lima)` | +1.43h |
| 3 | LEVANO PORRAS felix David FIR 73577252 sw 6435fc7bc135b1438ecf99acec8bbd7031be8ab7 | 73577252 | `2026-04-13T02:29:44+00:00` | `2026-04-12 21:29:44 (Lima)` | +1.44h |
| 4 | ORRILLO ZEVALLOS willian Bylly Jesus FIR 73824414 sw 1426f2d3da53e767468b56cb717e3b68c80e0a33 | 73824414 | `2026-04-13T02:30:04+00:00` | `2026-04-12 21:30:04 (Lima)` | +1.44h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041166**
2. Descargar el PDF del acta
3. Verificar SHA-256: `99291bc59b599518b2eda67ec1f0088f60b9ed8362777a01a340f22d42197ba1`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
