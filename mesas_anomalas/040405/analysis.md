# Mesa 040405 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.802090+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: CEBE LUIS BRAILE (código 2826)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 252
- Votos válidos: 225
- Participación: 84.281%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:07:30+00:00` | `2026-04-12 20:07:30 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:07:30+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:07:30+00:00` | `2026-04-12 20:07:30 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:50:02+00:00` | `2026-04-12 21:50:02 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:50:19+00:00` | `2026-04-12 21:50:19 (Lima)` |
| Última firma humana | `2026-04-13T02:50:52+00:00` | `2026-04-12 21:50:52 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.71 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:07:30 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:50:19 (Lima), es decir **1.71 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:07:28+00:00` | `2026-04-12 20:07:28 (Lima)` | -0.00h |
| 1 | OBREGON ALBA maria Eugenia FIR 09975719 sw 8c44b3572f5f867adb8737d07e1c6c31b7ad3109 | 09975719 | `2026-04-13T02:50:19+00:00` | `2026-04-12 21:50:19 (Lima)` | +1.71h |
| 2 | PIMENTEL VARGAS nelson Nel FIR 42899608 sw ae8083f66be715a610d449ee60d9501924a5f73c | 42899608 | `2026-04-13T02:50:33+00:00` | `2026-04-12 21:50:33 (Lima)` | +1.72h |
| 3 | PAJUELO JARA angel Yvan FIR 08146687 sw b9ba92a4920d86b0241c9c6dbaa00513a1e6111b | 08146687 | `2026-04-13T02:50:52+00:00` | `2026-04-12 21:50:52 (Lima)` | +1.72h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **040405**
2. Descargar el PDF del acta
3. Verificar SHA-256: `faedddba7d1334fa8eca50f95f4bf29e152272d3339b27104b2474081c8a0788`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
