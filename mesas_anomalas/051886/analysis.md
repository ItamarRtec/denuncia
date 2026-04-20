# Mesa 051886 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.440256+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: COMPLEJO DEPORTIVO PAUL HARRIS - MOROCOCHA (código 14161)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 219
- Votos válidos: 195
- Participación: 73.244%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:29:29+00:00` | `2026-04-12 20:29:29 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:29:29+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:29:29+00:00` | `2026-04-12 20:29:29 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:30:57+00:00` | `2026-04-12 22:30:57 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:31:26+00:00` | `2026-04-12 22:31:26 (Lima)` |
| Última firma humana | `2026-04-13T03:32:45+00:00` | `2026-04-12 22:32:45 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.03 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:29:29 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:31:26 (Lima), es decir **2.03 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:29:28+00:00` | `2026-04-12 20:29:28 (Lima)` | -0.00h |
| 1 | SEMINARIO SOSA hernan Alberto FIR 08825125 sw 47ca2de448f37f4653c119a21b47b741e3c9f6dd | 08825125 | `2026-04-13T03:31:26+00:00` | `2026-04-12 22:31:26 (Lima)` | +2.03h |
| 2 | SERPA MACCHIAVELLO alex Augusto FIR 07547342 sw 47e632d7e23900f9fec333b74d6eec302eabb17e | 07547342 | `2026-04-13T03:32:15+00:00` | `2026-04-12 22:32:15 (Lima)` | +2.05h |
| 3 | SORIA LOPEZ pedro Eduardo Sebastian FIR 42223337 sw f025d7f73f452a72c6da13b339f7ee233a9cd8ba | 42223337 | `2026-04-13T03:32:45+00:00` | `2026-04-12 22:32:45 (Lima)` | +2.05h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051886**
2. Descargar el PDF del acta
3. Verificar SHA-256: `997e136554ab8c58beaca5e547e04c157ae49dcb81b1b9f1492de882320690ee`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
