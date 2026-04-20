# Mesa 056570 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.814469+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IE 119 CANTO BELLO (código 3421)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 255
- Votos válidos: 225
- Participación: 85.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:08:20+00:00` | `2026-04-12 21:08:20 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:08:20+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:08:20+00:00` | `2026-04-12 21:08:20 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:33:44+00:00` | `2026-04-13 08:33:44 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:46:16+00:00` | `2026-04-13 08:46:16 (Lima)` |
| Última firma humana | `2026-04-13T13:50:58+00:00` | `2026-04-13 08:50:58 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.63 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:08:20 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:46:16 (Lima), es decir **11.63 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:08:18+00:00` | `2026-04-12 21:08:18 (Lima)` | -0.00h |
| 1 | AYMA CARRASCO guillermo Alejandro FIR 61251624 sw b8d6245dee06c43ed8714314ecf271f1a707ea77 | 61251624 | `2026-04-13T13:46:16+00:00` | `2026-04-13 08:46:16 (Lima)` | +11.63h |
| 2 | ARI CONDORI valentin FIR 06189178 sw 5f8b62d2e3bf17cfb68549a5afcfbaea55c53d1f | 06189178 | `2026-04-13T13:49:03+00:00` | `2026-04-13 08:49:03 (Lima)` | +11.68h |
| 3 | ARTEAGA VASQUEZ jean Paul FIR 60768781 sw 2d415a3adfe12598147eed4128c98f4d25b7b13a | 60768781 | `2026-04-13T13:50:58+00:00` | `2026-04-13 08:50:58 (Lima)` | +11.71h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **056570**
2. Descargar el PDF del acta
3. Verificar SHA-256: `10abf1f4a84f6dd99cdce85cfea12cfc44191ed7c36007135830076dd8e7c3ea`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
