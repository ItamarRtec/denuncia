# Mesa 054218 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.424206+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: INDEPENDENCIA
- **Local de votación**: IEP CESAR VALLEJO DE PAYET (código 54297)
- **Ubigeo**: 140134

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 215
- Votos válidos: 169
- Participación: 71.906%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:45:24+00:00` | `2026-04-12 19:45:24 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:45:24+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:45:24+00:00` | `2026-04-12 19:45:24 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T01:56:15+00:00` | `2026-04-12 20:56:15 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T01:56:28+00:00` | `2026-04-12 20:56:28 (Lima)` |
| Última firma humana | `2026-04-13T01:57:00+00:00` | `2026-04-12 20:57:00 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.18 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:45:24 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 20:56:28 (Lima), es decir **1.18 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:45:22+00:00` | `2026-04-12 19:45:22 (Lima)` | -0.00h |
| 1 | AKAMINE OCHOA jorge Esteban FIR 74978837 sw c37a15274fccf2275b863928f9b374f012f80f3b | 74978837 | `2026-04-13T01:56:28+00:00` | `2026-04-12 20:56:28 (Lima)` | +1.18h |
| 2 | ALCANTARA PORTILLO ariana Araceli FIR 74853811 sw 44a773a6b64e105b77f8e87294a08cf48bdb1932 | 74853811 | `2026-04-13T01:56:44+00:00` | `2026-04-12 20:56:44 (Lima)` | +1.19h |
| 3 | BAYLON CAMPOJO luis Fabrizzio FIR 75679184 sw e8c74030bbf9d07c0b03d8f44e41de435b70f5c6 | 75679184 | `2026-04-13T01:57:00+00:00` | `2026-04-12 20:57:00 (Lima)` | +1.19h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054218**
2. Descargar el PDF del acta
3. Verificar SHA-256: `36787f704b5122f69d439934168bb8b9667fba0e4535e102d2c684880745fd9a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
