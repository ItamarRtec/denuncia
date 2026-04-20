# Mesa 047227 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.739455+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: RÍMAC
- **Local de votación**: IE LUCIE RYNNING DE ANTUNEZ DE MAYOLO (código 3063)
- **Ubigeo**: 140122

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 236
- Votos válidos: 215
- Participación: 78.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:56:32+00:00` | `2026-04-12 21:56:32 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:56:32+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:56:32+00:00` | `2026-04-12 21:56:32 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:34:39+00:00` | `2026-04-13 09:34:39 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:34:55+00:00` | `2026-04-13 09:34:55 (Lima)` |
| Última firma humana | `2026-04-13T14:35:21+00:00` | `2026-04-13 09:35:21 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.64 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:56:32 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:34:55 (Lima), es decir **11.64 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:56:15+00:00` | `2026-04-12 21:56:15 (Lima)` | -0.00h |
| 1 | GAMARRA VELEZ mariana Gissilla FIR 41955264 sw b2b6388bf7929f7dbfa101af831ee5f08fdd77d0 | 41955264 | `2026-04-13T14:34:55+00:00` | `2026-04-13 09:34:55 (Lima)` | +11.64h |
| 2 | FAJARDO CELIS victor Hugo FIR 08057294 sw 79c5ad8ca0a827af6e3a2c0def80cd79cf98c76f | 08057294 | `2026-04-13T14:35:08+00:00` | `2026-04-13 09:35:08 (Lima)` | +11.64h |
| 3 | ESPINOZA LOZA cesar Anthony FIR 40594032 sw 5d3d7830e3a3b61aee96ff948148aa16d99ef305 | 40594032 | `2026-04-13T14:35:21+00:00` | `2026-04-13 09:35:21 (Lima)` | +11.65h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **047227**
2. Descargar el PDF del acta
3. Verificar SHA-256: `611fb8862a384531fab1fc222b71a7ffb50cdbc6c82e69127824f80acef89435`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
