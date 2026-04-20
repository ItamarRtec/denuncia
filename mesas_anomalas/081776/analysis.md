# Mesa 081776 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.516076+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CALLAO
- **Local de votación**: ESTADIO MUNICIPAL PREVI (código 17606)
- **Ubigeo**: 240101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 219
- Votos válidos: 183
- Participación: 73.244%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:17:22+00:00` | `2026-04-12 21:17:22 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:17:22+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:17:22+00:00` | `2026-04-12 21:17:22 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:14:35+00:00` | `2026-04-13 08:14:35 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:17:19+00:00` | `2026-04-13 08:17:19 (Lima)` |
| Última firma humana | `2026-04-13T13:25:05+00:00` | `2026-04-13 08:25:05 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.00 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:17:22 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:17:19 (Lima), es decir **11.00 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:16:25+00:00` | `2026-04-12 21:16:25 (Lima)` | -0.02h |
| 1 | GOICOCHEA NAJARRO angel Jackson FIR 76759576 sw d7a8e7e6c0560c4c597e4d67fa0e04e7b9b51e29 | 76759576 | `2026-04-13T13:17:19+00:00` | `2026-04-13 08:17:19 (Lima)` | +11.00h |
| 2 | GONZALES RAMOS bertila Celestina FIR 43675499 sw f1671ee92d0142befca54f2e8c2cbe15dada1068 | 43675499 | `2026-04-13T13:22:47+00:00` | `2026-04-13 08:22:47 (Lima)` | +11.09h |
| 3 | GUERRERO ROJAS victor Oswaldo FIR 40700096 sw b92b0a3e6bfa0db5fb9b1eccdfaf879308c05dfa | 40700096 | `2026-04-13T13:25:05+00:00` | `2026-04-13 08:25:05 (Lima)` | +11.13h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **081776**
2. Descargar el PDF del acta
3. Verificar SHA-256: `af1ac402994f94f7e5204731580c57282e87fa88bc9693d99bc9e4900efd386e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
