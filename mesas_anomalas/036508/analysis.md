# Mesa 036508 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.959267+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE SIMON BOLIVAR (código 4944)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 254
- Votos válidos: 236
- Participación: 84.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:48:03+00:00` | `2026-04-12 21:48:03 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:48:03+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:48:03+00:00` | `2026-04-12 21:48:03 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:04:30+00:00` | `2026-04-13 08:04:30 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:04:51+00:00` | `2026-04-13 08:04:51 (Lima)` |
| Última firma humana | `2026-04-13T13:05:55+00:00` | `2026-04-13 08:05:55 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.28 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:48:03 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:04:51 (Lima), es decir **10.28 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:47:36+00:00` | `2026-04-12 21:47:36 (Lima)` | -0.01h |
| 1 | MALLA GUTIERREZ aldo Dante FIR 06281855 sw e825df7de72c077d0db7b903b1472c8382600ad8 | 06281855 | `2026-04-13T13:04:51+00:00` | `2026-04-13 08:04:51 (Lima)` | +10.28h |
| 2 | LLANQUE SANCHO hector Manuel FIR 09431859 sw c0d330f368c93f80e8180ebd767191ea8d2dcde7 | 09431859 | `2026-04-13T13:05:21+00:00` | `2026-04-13 08:05:21 (Lima)` | +10.29h |
| 3 | MEDINA FIGUEREDO DE ABANTO blanca Karina FIR 09927654 sw cc9b929a100599a16d45163c74868b2f1c6cd8b9 | 09927654 | `2026-04-13T13:05:55+00:00` | `2026-04-13 08:05:55 (Lima)` | +10.30h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036508**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e669a9b78fc12adac2ef9614f8095f3c29945739ec8be24549af70d86210376b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
