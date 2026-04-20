# Mesa 036068 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.096681+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE 1001 JOSE JIMENEZ BORJA (código 2642)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 236
- Votos válidos: 213
- Participación: 78.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:33:47+00:00` | `2026-04-12 20:33:47 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:33:47+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:33:47+00:00` | `2026-04-12 20:33:47 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:53:53+00:00` | `2026-04-13 07:53:53 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:54:08+00:00` | `2026-04-13 07:54:08 (Lima)` |
| Última firma humana | `2026-04-13T12:55:06+00:00` | `2026-04-13 07:55:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.34 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:33:47 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:54:08 (Lima), es decir **11.34 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:33:45+00:00` | `2026-04-12 20:33:45 (Lima)` | -0.00h |
| 1 | CHIRINOS MOGROVEJO maria Azucena FIR 70117700 sw e5809b8c4af5802930bbdb8af9df81b2d42a81e0 | 70117700 | `2026-04-13T12:54:08+00:00` | `2026-04-13 07:54:08 (Lima)` | +11.34h |
| 2 | CASTILLA KROSS karina Monica FIR 09837570 sw 2998f4fc6654a47b3e3b13c1bcf522b1de5c615d | 09837570 | `2026-04-13T12:54:32+00:00` | `2026-04-13 07:54:32 (Lima)` | +11.35h |
| 3 | CHAMPI SERNADES jhon Lenon FIR 71752697 sw cd83717d68e6cf8730bc0c21d36a0f586170b951 | 71752697 | `2026-04-13T12:54:52+00:00` | `2026-04-13 07:54:52 (Lima)` | +11.35h |
| 4 | HUAMAN HUAMAN anthony Williams FIR 47342233 sw 2736dff992f4bc7079871b02b79b9c5de0b6ac7c | 47342233 | `2026-04-13T12:55:06+00:00` | `2026-04-13 07:55:06 (Lima)` | +11.36h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036068**
2. Descargar el PDF del acta
3. Verificar SHA-256: `17a6c5134881515c30f52249f3295438aa264a3cf9d6be613af463c273bf9e1e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
