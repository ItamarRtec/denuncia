# Mesa 061822 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.938562+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IEP ALFONSO UGARTE (código 3592)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 260
- Votos válidos: 231
- Participación: 86.957%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:17:18+00:00` | `2026-04-12 21:17:18 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:17:18+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:17:18+00:00` | `2026-04-12 21:17:18 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:27:53+00:00` | `2026-04-12 22:27:53 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:28:18+00:00` | `2026-04-12 22:28:18 (Lima)` |
| Última firma humana | `2026-04-13T03:29:13+00:00` | `2026-04-12 22:29:13 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.18 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:17:18 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:28:18 (Lima), es decir **1.18 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:17:15+00:00` | `2026-04-12 21:17:15 (Lima)` | -0.00h |
| 1 | AMANCAY TORRES judith FIR 45314587 sw d32f46d5e8ac43e2248ff03c59070becfb30f11a | 45314587 | `2026-04-13T03:28:18+00:00` | `2026-04-12 22:28:18 (Lima)` | +1.18h |
| 2 | AMBROCIO ROSALES sonia Maribel FIR 43375374 sw 6aaba54b65ccc02b40e52b69cc9b2c40290ec555 | 43375374 | `2026-04-13T03:28:43+00:00` | `2026-04-12 22:28:43 (Lima)` | +1.19h |
| 3 | ALVAREZ TACUCHE erickson FIR 46075650 sw c13bef0e9275fb49ebeba8b45eeb441681400f87 | 46075650 | `2026-04-13T03:29:13+00:00` | `2026-04-12 22:29:13 (Lima)` | +1.20h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061822**
2. Descargar el PDF del acta
3. Verificar SHA-256: `88e06a122fec27cd86b4ed53c2808a51edf4fcd3636870f344f0d29fda04be19`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
