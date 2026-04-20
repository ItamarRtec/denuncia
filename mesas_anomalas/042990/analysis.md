# Mesa 042990 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.101460+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA VICTORIA
- **Local de votación**: IEP SACO OLIVEROS (código 13171)
- **Ubigeo**: 140109

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 227
- Votos válidos: 204
- Participación: 75.92%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:40:05+00:00` | `2026-04-12 20:40:05 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:40:05+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:40:05+00:00` | `2026-04-12 20:40:05 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:15:23+00:00` | `2026-04-12 22:15:23 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:16:45+00:00` | `2026-04-12 22:16:45 (Lima)` |
| Última firma humana | `2026-04-13T03:19:25+00:00` | `2026-04-12 22:19:25 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.61 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:40:05 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:16:45 (Lima), es decir **1.61 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:40:02+00:00` | `2026-04-12 20:40:02 (Lima)` | -0.00h |
| 1 | MORALES MEZA emel FIR 07511673 sw 35d3658765eedd5b99da9ad313f0f7e35b46d6c2 | 07511673 | `2026-04-13T03:16:45+00:00` | `2026-04-12 22:16:45 (Lima)` | +1.61h |
| 2 | MONTOYA REYES maria Fernanda FIR 72731067 sw 27ad5a87f6cc68b31283c02c95ccc7c2d3c10c1e | 72731067 | `2026-04-13T03:16:59+00:00` | `2026-04-12 22:16:59 (Lima)` | +1.61h |
| 3 | MORE SENMACHE jose Oswaldo FIR 17445734 sw 4d03c7031c589957e26e5ea8c730315eaa748658 | 17445734 | `2026-04-13T03:17:11+00:00` | `2026-04-12 22:17:11 (Lima)` | +1.62h |
| 4 | MORENO MEJIA elizabeth Zully FIR 07853216 sw b9cebd4ab41d469f699fa4ff2105c442758b4521 | 07853216 | `2026-04-13T03:17:51+00:00` | `2026-04-12 22:17:51 (Lima)` | +1.63h |
| 5 | SOLIS GRANADOS gloria FIR 07341581 sw b88978d1c2441378d89b0c6c2dfe0516d98cfff9 | 07341581 | `2026-04-13T03:18:21+00:00` | `2026-04-12 22:18:21 (Lima)` | +1.64h |
| 6 | CAMPOMANES AYAMBO annatoli FIR 43044297 sw 43446f9efbc84e010d64f09c3c81a33310e948e9 | 43044297 | `2026-04-13T03:19:25+00:00` | `2026-04-12 22:19:25 (Lima)` | +1.66h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042990**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8e37f577ca3dab524c055b54d3aaf2d84fd85c7dc32fff4d091c998848536bed`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **6** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
