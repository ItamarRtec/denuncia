# Mesa 060766 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.217243+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LOS OLIVOS
- **Local de votación**: IE 2087 REPUBLICA ORIENTAL DEL URUGUAY (código 3547)
- **Ubigeo**: 140142

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 263
- Votos válidos: 244
- Participación: 87.96%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:42:01+00:00` | `2026-04-12 20:42:01 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:42:01+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:42:01+00:00` | `2026-04-12 20:42:01 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:55:52+00:00` | `2026-04-12 22:55:52 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:56:18+00:00` | `2026-04-12 22:56:18 (Lima)` |
| Última firma humana | `2026-04-13T03:57:06+00:00` | `2026-04-12 22:57:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.24 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:42:01 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:56:18 (Lima), es decir **2.24 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:41:59+00:00` | `2026-04-12 20:41:59 (Lima)` | -0.00h |
| 1 | QUISPE SARAYA yanet FIR 41791681 sw 7acae4729d09f6daac6510c31d5e7294ce944427 | 41791681 | `2026-04-13T03:56:18+00:00` | `2026-04-12 22:56:18 (Lima)` | +2.24h |
| 2 | REQUEJO PINEDO samira Marisol FIR 72729378 sw 6698fda0a335a288371f10c13d98f8a3d60933e1 | 72729378 | `2026-04-13T03:56:29+00:00` | `2026-04-12 22:56:29 (Lima)` | +2.24h |
| 3 | RAMIREZ OLORTEGUI ronald Dante FIR 42919988 sw 1c3862687cf2c3066765bf2a561eea30d8d10ded | 42919988 | `2026-04-13T03:56:40+00:00` | `2026-04-12 22:56:40 (Lima)` | +2.24h |
| 4 | ANCA DELGADO yuli Yvonne FIR 09638717 sw 89c2310930d508d512612131735e6ce96ba90fa7 | 09638717 | `2026-04-13T03:57:06+00:00` | `2026-04-12 22:57:06 (Lima)` | +2.25h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **060766**
2. Descargar el PDF del acta
3. Verificar SHA-256: `b9dc97606a2b7bd3354d2e71680f6722a3923cfb65aef73a2cc0d6d50b210859`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
