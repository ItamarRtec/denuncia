# Mesa 062148 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.259302+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IEP WILLIAM SHAKESPEARE (código 50549)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 258
- Votos válidos: 234
- Participación: 86.288%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:47:56+00:00` | `2026-04-12 20:47:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:47:56+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:47:56+00:00` | `2026-04-12 20:47:56 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:38:40+00:00` | `2026-04-12 23:38:40 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:39:11+00:00` | `2026-04-12 23:39:11 (Lima)` |
| Última firma humana | `2026-04-13T04:39:47+00:00` | `2026-04-12 23:39:47 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.85 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:47:56 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:39:11 (Lima), es decir **2.85 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:47:54+00:00` | `2026-04-12 20:47:54 (Lima)` | -0.00h |
| 1 | MEZA MIRANDA millan FIR 40647319 sw 9309220334e46f595896eaf3db815135b396c457 | 40647319 | `2026-04-13T04:39:11+00:00` | `2026-04-12 23:39:11 (Lima)` | +2.85h |
| 2 | MEZA VILLANUEVA rosario Beatriz FIR 41875383 sw a4dbdbc74392392e9b56055b53f388125bb17754 | 41875383 | `2026-04-13T04:39:28+00:00` | `2026-04-12 23:39:28 (Lima)` | +2.86h |
| 3 | LUQUE CHOQUEMAMANI eduardo FIR 10181499 sw cc1d596e1fc324c870e9e8a6de41d1c8cfbc3a3d | 10181499 | `2026-04-13T04:39:47+00:00` | `2026-04-12 23:39:47 (Lima)` | +2.86h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **062148**
2. Descargar el PDF del acta
3. Verificar SHA-256: `f92550838fb5f5cb55b15ebf4d425504ba7367fb40cc80c9ca97a2895b7f7ede`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
