# Mesa 045999 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.415031+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUEBLO LIBRE
- **Local de votación**: IEP JORGE POLAR (código 50564)
- **Ubigeo**: 140117

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 261
- Votos válidos: 245
- Participación: 87.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:57:08+00:00` | `2026-04-12 19:57:08 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:57:08+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:57:08+00:00` | `2026-04-12 19:57:08 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:32:27+00:00` | `2026-04-12 21:32:27 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:32:40+00:00` | `2026-04-12 21:32:40 (Lima)` |
| Última firma humana | `2026-04-13T02:33:04+00:00` | `2026-04-12 21:33:04 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.59 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:57:08 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:32:40 (Lima), es decir **1.59 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:57:06+00:00` | `2026-04-12 19:57:06 (Lima)` | -0.00h |
| 1 | PITA PALACIOS hector Guillermo FIR 09946107 sw 4ef96d46d1921389f6d5b3f6fc2e15f948621b85 | 09946107 | `2026-04-13T02:32:40+00:00` | `2026-04-12 21:32:40 (Lima)` | +1.59h |
| 2 | RIOS AGUSTIN dante Leonidas FIR 45093421 sw a372efc58551b13ae0d35d974623297854bad0bd | 45093421 | `2026-04-13T02:32:52+00:00` | `2026-04-12 21:32:52 (Lima)` | +1.60h |
| 3 | RAMOS BURGOS salvador Manuel Maximo FIR 07944231 sw 873451fc5e484b59c25fd068d1f6c3bb85279871 | 07944231 | `2026-04-13T02:33:04+00:00` | `2026-04-12 21:33:04 (Lima)` | +1.60h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045999**
2. Descargar el PDF del acta
3. Verificar SHA-256: `9c362653c0dc33a9980924629733f77f2a72c12552d6c26fdfa5204d8aeb89c7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
