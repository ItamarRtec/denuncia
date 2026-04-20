# Mesa 050313 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.846570+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: COLEGIO SACO OLIVEROS DE SAN MIGUEL (código 52595)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 222
- Votos válidos: 201
- Participación: 74.247%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:36:16+00:00` | `2026-04-12 21:36:16 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:36:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:36:16+00:00` | `2026-04-12 21:36:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:19:54+00:00` | `2026-04-13 08:19:54 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:20:28+00:00` | `2026-04-13 08:20:28 (Lima)` |
| Última firma humana | `2026-04-13T13:21:30+00:00` | `2026-04-13 08:21:30 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.74 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:36:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:20:28 (Lima), es decir **10.74 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:36:13+00:00` | `2026-04-12 21:36:13 (Lima)` | -0.00h |
| 1 | UZURIAGA JARA monica Isabel FIR 46302019 sw a4adae84503b7b6d6531b3e6a92cfae5e52931db | 46302019 | `2026-04-13T13:20:28+00:00` | `2026-04-13 08:20:28 (Lima)` | +10.74h |
| 2 | TUESTA RIVASPLATA karin FIR 09915527 sw 4c12c9be9dcf44c1601afb1aa305f022e8464152 | 09915527 | `2026-04-13T13:20:46+00:00` | `2026-04-13 08:20:46 (Lima)` | +10.74h |
| 3 | MENDOZA HIDALGO karina Silvanette FIR 10146196 sw f57b9a1df586d33071451a69b7fd83699439adbb | 10146196 | `2026-04-13T13:21:30+00:00` | `2026-04-13 08:21:30 (Lima)` | +10.75h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050313**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4c735bed3926eef1ee5d04a827478f32e4a01b08d3481a3a7416b6c3ce34b279`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
