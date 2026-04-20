# Mesa 058751 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.525588+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN LUIS
- **Local de votación**: IE 1128 SAN LUIS (código 3478)
- **Ubigeo**: 140138

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 243
- Votos válidos: 209
- Participación: 81.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:28:56+00:00` | `2026-04-12 20:28:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:28:56+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:28:56+00:00` | `2026-04-12 20:28:56 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:14:27+00:00` | `2026-04-12 21:14:27 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:14:44+00:00` | `2026-04-12 21:14:44 (Lima)` |
| Última firma humana | `2026-04-13T02:15:10+00:00` | `2026-04-12 21:15:10 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.76 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:28:56 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:14:44 (Lima), es decir **0.76 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:28:54+00:00` | `2026-04-12 20:28:54 (Lima)` | -0.00h |
| 1 | MORALES MARCA orestes Geronimo FIR 09791078 sw 2525a7907d5e8bda246b2b1e122559cd5c954c6c | 09791078 | `2026-04-13T02:14:44+00:00` | `2026-04-12 21:14:44 (Lima)` | +0.76h |
| 2 | MURILLO ALVA gisela Maria Luisa FIR 47508247 sw c96070d4098b4eabe7a5dea7cd70de0d7210eda0 | 47508247 | `2026-04-13T02:14:57+00:00` | `2026-04-12 21:14:57 (Lima)` | +0.77h |
| 3 | MORENO ROQUE irma Esperanza FIR 42932028 sw 4c35d0c1c1bdc42b9cc4c64a382911b0ec36d363 | 42932028 | `2026-04-13T02:15:10+00:00` | `2026-04-12 21:15:10 (Lima)` | +0.77h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **058751**
2. Descargar el PDF del acta
3. Verificar SHA-256: `b60b959d837c437272c1c20ec838999f58c7397c7ca8fa6f79cb16ad2dd4255a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
