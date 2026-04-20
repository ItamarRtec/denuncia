# Mesa 055306 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.190892+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE DE ACCION CONJUNTA PADRE ILUMINATO (código 3375)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 249
- Votos válidos: 224
- Participación: 83.278%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:27:33+00:00` | `2026-04-12 21:27:33 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:23:52+00:00` | `2026-04-12 21:23:52 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:27:33+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:27:33+00:00` | `2026-04-12 21:27:33 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T06:06:48+00:00` | `2026-04-13 01:06:48 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:11:54+00:00` | `2026-04-13 01:11:54 (Lima)` |
| Última firma humana | `2026-04-13T06:12:24+00:00` | `2026-04-13 01:12:24 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.74 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:27:33 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:11:54 (Lima), es decir **3.74 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:23:49+00:00` | `2026-04-12 21:23:49 (Lima)` | -0.06h |
| 1 | VELARDE ZAMORA david Arturo FIR 43209273 sw dc006a3d099ca55407de473de98eb5b19ecd6c75 | 43209273 | `2026-04-13T06:11:54+00:00` | `2026-04-13 01:11:54 (Lima)` | +3.74h |
| 2 | VEGA ESPINOZA DE ABRAMONTE justa FIR 09721637 sw 026703d6dd872831f707bdadcc53b62113f7b123 | 09721637 | `2026-04-13T06:12:09+00:00` | `2026-04-13 01:12:09 (Lima)` | +3.74h |
| 3 | VASQUEZ MARRUFO yoni Teodoro FIR 45299336 sw 3d33f62eef07f9c4109641e6ef0a7d756b306939 | 45299336 | `2026-04-13T06:12:24+00:00` | `2026-04-13 01:12:24 (Lima)` | +3.75h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055306**
2. Descargar el PDF del acta
3. Verificar SHA-256: `cf1e007320fbe2d0c5e1e244b049ab53b2cf33ad8123c7baaed5d3caf160987b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
