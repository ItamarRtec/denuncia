# Mesa 052077 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.814532+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IE 6019 MARIANO MELGAR (código 3244)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 234
- Votos válidos: 198
- Participación: 78.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:39:50+00:00` | `2026-04-12 21:39:50 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:39:50+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:39:50+00:00` | `2026-04-12 21:39:50 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:35:01+00:00` | `2026-04-13 08:35:01 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:35:15+00:00` | `2026-04-13 08:35:15 (Lima)` |
| Última firma humana | `2026-04-13T13:36:36+00:00` | `2026-04-13 08:36:36 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.92 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:39:50 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:35:15 (Lima), es decir **10.92 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:39:48+00:00` | `2026-04-12 21:39:48 (Lima)` | -0.00h |
| 1 | CALLUPE HUARCO maribel Yvet FIR 10085755 sw a01ffbed10e44b7abf3f6d4d5a4102be15271557 | 10085755 | `2026-04-13T13:35:15+00:00` | `2026-04-13 08:35:15 (Lima)` | +10.92h |
| 2 | CALZADO ACERO camila Del Pilar FIR 76047219 sw d01fd5936655ff13ce1b853ff391aa630f3c3d68 | 76047219 | `2026-04-13T13:36:22+00:00` | `2026-04-13 08:36:22 (Lima)` | +10.94h |
| 3 | CARBAJAL GALVEZ rigoberto Deyver FIR 10076790 sw 64d2e3893eee72fdf87328ebea9bdee572af566f | 10076790 | `2026-04-13T13:36:36+00:00` | `2026-04-13 08:36:36 (Lima)` | +10.95h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **052077**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5469065a8fdfcdd94544ed32597b948e2173fded673c6bb24844e976d8f04f47`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
