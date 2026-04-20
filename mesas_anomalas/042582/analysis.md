# Mesa 042582 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.273574+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA VICTORIA
- **Local de votación**: IE 1105 LA SAGRADA FAMILIA (código 2882)
- **Ubigeo**: 140109

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 236
- Votos válidos: 204
- Participación: 78.93%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:03:24+00:00` | `2026-04-12 20:03:24 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:03:24+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:03:24+00:00` | `2026-04-12 20:03:24 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T01:41:11+00:00` | `2026-04-12 20:41:11 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T01:41:39+00:00` | `2026-04-12 20:41:39 (Lima)` |
| Última firma humana | `2026-04-13T01:42:36+00:00` | `2026-04-12 20:42:36 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.64 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:03:24 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 20:41:39 (Lima), es decir **0.64 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:03:23+00:00` | `2026-04-12 20:03:23 (Lima)` | -0.00h |
| 1 | HUAMANI BERROCAL humberto FIR 07399796 sw 8125e5f1407fd6d54046b6352b079641d2a47e62 | 07399796 | `2026-04-13T01:41:39+00:00` | `2026-04-12 20:41:39 (Lima)` | +0.64h |
| 2 | INFANTE MAZA jose Humberto FIR 46709527 sw 8c59364d713649e0b52ca02e9f636ef423b65c05 | 46709527 | `2026-04-13T01:41:50+00:00` | `2026-04-12 20:41:50 (Lima)` | +0.64h |
| 3 | HUINCHO CHILLCCE edith Yonayda FIR 42542163 sw 54530a908d4c16d91ae4a3d547475421829e118c | 42542163 | `2026-04-13T01:42:01+00:00` | `2026-04-12 20:42:01 (Lima)` | +0.64h |
| 4 | HOLGUIN CHAVEZ carlos Enrique FIR 07302575 sw 5b4e16d7a3f0bc099f768a30ee2daa747f30e801 | 07302575 | `2026-04-13T01:42:36+00:00` | `2026-04-12 20:42:36 (Lima)` | +0.65h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042582**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e73aa7a3d8bc0830f6c03d8ea6357c0ba2c2b58393921fa63ac9e02e663c1f89`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
