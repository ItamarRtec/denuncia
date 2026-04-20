# Mesa 041354 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.255479+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IEP GETSEMANI (código 52859)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 242
- Votos válidos: 202
- Participación: 80.936%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:54:02+00:00` | `2026-04-12 19:54:02 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:54:02+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:54:02+00:00` | `2026-04-12 19:54:02 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T01:36:06+00:00` | `2026-04-12 20:36:06 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T01:36:31+00:00` | `2026-04-12 20:36:31 (Lima)` |
| Última firma humana | `2026-04-13T01:36:54+00:00` | `2026-04-12 20:36:54 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.71 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:54:02 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 20:36:31 (Lima), es decir **0.71 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:54:00+00:00` | `2026-04-12 19:54:00 (Lima)` | -0.00h |
| 1 | AREVALO ORIHUELA jean Carlos FIR 48459800 sw 02282dd45845ab74d2562bd923a66b3907b9507a | 48459800 | `2026-04-13T01:36:31+00:00` | `2026-04-12 20:36:31 (Lima)` | +0.71h |
| 2 | CESPEDES PEREZ valery Roxana FIR 74194685 sw b9eba44554ff4dc027f48a057799a100ec3537fa | 74194685 | `2026-04-13T01:36:42+00:00` | `2026-04-12 20:36:42 (Lima)` | +0.71h |
| 3 | CARDENAS VALLADOLID ruben Dario Alessandro FIR 75192189 sw 2a276f19d1a386b284100594bf2bfbe902c675d9 | 75192189 | `2026-04-13T01:36:54+00:00` | `2026-04-12 20:36:54 (Lima)` | +0.71h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041354**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e3b03dfbd01eed0def7fe8252b6788392a5dd0013fb8f1cbbc7e6682b5eaef9d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
