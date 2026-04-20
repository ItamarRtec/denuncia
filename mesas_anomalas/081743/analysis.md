# Mesa 081743 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.495983+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CALLAO
- **Local de votación**: COMPLEJO DEPORTIVO RAMÓN CASTILLA (código 17604)
- **Ubigeo**: 240101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 225
- Votos válidos: 204
- Participación: 75.251%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:48:38+00:00` | `2026-04-12 19:48:38 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:48:38+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:48:38+00:00` | `2026-04-12 19:48:38 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:20:26+00:00` | `2026-04-12 21:20:26 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:20:49+00:00` | `2026-04-12 21:20:49 (Lima)` |
| Última firma humana | `2026-04-13T02:21:19+00:00` | `2026-04-12 21:21:19 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.54 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:48:38 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:20:49 (Lima), es decir **1.54 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:48:37+00:00` | `2026-04-12 19:48:37 (Lima)` | -0.00h |
| 1 | CAPILLO SOLIS deysi Diana FIR 41582909 sw 3c4e032b92c88e9da89c160ce4dd03a065e066e9 | 41582909 | `2026-04-13T02:20:49+00:00` | `2026-04-12 21:20:49 (Lima)` | +1.54h |
| 2 | CAPILLO SOLIS mirtha Andrea FIR 40866523 sw 31acf23ccedfe0e1dd0315384b9c212410c798a2 | 40866523 | `2026-04-13T02:21:07+00:00` | `2026-04-12 21:21:07 (Lima)` | +1.54h |
| 3 | CARRION BARRIENTOS betzabeth Dennis FIR 43271541 sw 7a388fa25a89e4cdaf59e237fd00d992da4a8797 | 43271541 | `2026-04-13T02:21:19+00:00` | `2026-04-12 21:21:19 (Lima)` | +1.54h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **081743**
2. Descargar el PDF del acta
3. Verificar SHA-256: `9e3dc95821d4e9239da004cb7df851d5c2d7108eb388f34ab82f0feae3d5acd8`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
