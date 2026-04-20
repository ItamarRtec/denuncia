# Mesa 052658 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.018776+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IE TUPAC AMARU (código 3275)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 240
- Votos válidos: 213
- Participación: 80.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:36:15+00:00` | `2026-04-12 20:36:15 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:36:15+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:36:15+00:00` | `2026-04-12 20:36:15 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:12:50+00:00` | `2026-04-12 22:12:50 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:14:58+00:00` | `2026-04-12 22:14:58 (Lima)` |
| Última firma humana | `2026-04-13T03:15:18+00:00` | `2026-04-12 22:15:18 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.65 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:36:15 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:14:58 (Lima), es decir **1.65 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:36:13+00:00` | `2026-04-12 20:36:13 (Lima)` | -0.00h |
| 1 | CUENCA MALLMA martin Huber FIR 46883508 sw c2dbb1ba5175ac854e1e5f583e1925cafe658ed4 | 46883508 | `2026-04-13T03:14:58+00:00` | `2026-04-12 22:14:58 (Lima)` | +1.65h |
| 2 | DELGADO FLORES diana Esmenia FIR 71020259 sw ecb2c9783e7cfd49ba2a185d9ffcdbfc30140bd5 | 71020259 | `2026-04-13T03:15:18+00:00` | `2026-04-12 22:15:18 (Lima)` | +1.65h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **052658**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4aa2f1614b3521dc8f88a2c9d8be4870b2852123338e869f56b15a9f8bd2ef7b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
