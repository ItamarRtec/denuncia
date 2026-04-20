# Mesa 041696 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.729848+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: IE 6090 JOSE OLAYA BALANDRA (código 2858)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 261
- Votos válidos: 236
- Participación: 87.291%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T07:08:50+00:00` | `2026-04-13 02:08:50 (Lima)` |
| `C` | Contabilizada | `2026-04-13T03:23:02+00:00` | `2026-04-12 22:23:02 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T07:08:50+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T07:08:50+00:00` | `2026-04-13 02:08:50 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T07:50:04+00:00` | `2026-04-13 02:50:04 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T07:50:20+00:00` | `2026-04-13 02:50:20 (Lima)` |
| Última firma humana | `2026-04-13T07:51:17+00:00` | `2026-04-13 02:51:17 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.69 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-13 02:08:50 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 02:50:20 (Lima), es decir **0.69 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:23:00+00:00` | `2026-04-12 22:23:00 (Lima)` | -3.76h |
| 1 | ZUZUNAGA RODRIGUEZ fiorela Christina FIR 73191910 sw c999531790ce17a01e9c56b12c718594707ae917 | 73191910 | `2026-04-13T07:50:20+00:00` | `2026-04-13 02:50:20 (Lima)` | +0.69h |
| 2 | ZAPATA MORENO luis Angel FIR 16677055 sw 29195f95f45a7373ae84e8055e23cd91686f33f9 | 16677055 | `2026-04-13T07:50:30+00:00` | `2026-04-13 02:50:30 (Lima)` | +0.69h |
| 3 | GUTIERREZ VEGA aracely Valeria FIR 60942286 sw 4c0836e209cec24881ce19471e7a51b5e24a408c | 60942286 | `2026-04-13T07:51:02+00:00` | `2026-04-13 02:51:02 (Lima)` | +0.70h |
| 4 | ESPINOZA SILVERA freddy FIR 80583121 sw f6758687b056cae7adeca4f7e7ccbf52596b1fec | 80583121 | `2026-04-13T07:51:17+00:00` | `2026-04-13 02:51:17 (Lima)` | +0.71h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041696**
2. Descargar el PDF del acta
3. Verificar SHA-256: `94bc6f32ee1711c2d93a74730c1269aacbeb0bed2b556c11d7e5dabe42cc82b8`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
