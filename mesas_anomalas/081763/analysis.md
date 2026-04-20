# Mesa 081763 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.314413+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CALLAO
- **Local de votación**: COMPLEJO DEPORTIVO RAMÓN CASTILLA (código 17604)
- **Ubigeo**: 240101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 232
- Votos válidos: 200
- Participación: 77.592%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:02:18+00:00` | `2026-04-12 21:02:18 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:02:18+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:02:18+00:00` | `2026-04-12 21:02:18 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T10:41:19+00:00` | `2026-04-13 05:41:19 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T10:41:33+00:00` | `2026-04-13 05:41:33 (Lima)` |
| Última firma humana | `2026-04-13T10:42:04+00:00` | `2026-04-13 05:42:04 (Lima)` |

**Brecha primera firma humana vs publicación:** **+8.65 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:02:18 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 05:41:33 (Lima), es decir **8.65 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:02:16+00:00` | `2026-04-12 21:02:16 (Lima)` | -0.00h |
| 1 | ZAVALA MENESES miguel Angel FIR 40266213 sw ae74839a77c433cc429fedd5a9c4609a04b27176 | 40266213 | `2026-04-13T10:41:33+00:00` | `2026-04-13 05:41:33 (Lima)` | +8.65h |
| 2 | VIRU FLORES jose Antonio FIR 42512660 sw bc187ca57ae0ce8de0432bece912e4213d54250d | 42512660 | `2026-04-13T10:41:52+00:00` | `2026-04-13 05:41:52 (Lima)` | +8.66h |
| 3 | YAUSIN ELGUERA jose Andres FIR 42883387 sw 1b056ddb589cc7c8902cc33b48268eb98b15e95a | 42883387 | `2026-04-13T10:42:04+00:00` | `2026-04-13 05:42:04 (Lima)` | +8.66h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **081763**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2ad85af072227e86590abb1e8544fe38bae4f02c737ed0ef2f777aea3eaab251`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
