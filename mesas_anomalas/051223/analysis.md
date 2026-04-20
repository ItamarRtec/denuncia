# Mesa 051223 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.608360+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: ESTACIONAMIENTO 1 - UNIVERSIDAD DE LIMA (código 35747)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 218
- Votos válidos: 201
- Participación: 72.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:01:54+00:00` | `2026-04-12 21:01:54 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:01:54+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:01:54+00:00` | `2026-04-12 21:01:54 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:52:32+00:00` | `2026-04-13 07:52:32 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:52:51+00:00` | `2026-04-13 07:52:51 (Lima)` |
| Última firma humana | `2026-04-13T12:53:24+00:00` | `2026-04-13 07:53:24 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.85 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:01:54 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:52:51 (Lima), es decir **10.85 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:01:49+00:00` | `2026-04-12 21:01:49 (Lima)` | -0.00h |
| 1 | FREYRE ARMESTAR luis Augusto FIR 10551070 sw d0da83d80e20436d45ee0776990757d600505008 | 10551070 | `2026-04-13T12:52:51+00:00` | `2026-04-13 07:52:51 (Lima)` | +10.85h |
| 2 | GALVEZ RODRIGUEZ lewis Benjamin FIR 10809388 sw 2bc56364bc0d72e9029a3ebebf54156eb5732aac | 10809388 | `2026-04-13T12:53:15+00:00` | `2026-04-13 07:53:15 (Lima)` | +10.86h |
| 3 | FLORES EZETA carlos Manuel FIR 10555110 sw d6a87aa45b3ec974bdd87c94d3935685acd0da02 | 10555110 | `2026-04-13T12:53:24+00:00` | `2026-04-13 07:53:24 (Lima)` | +10.86h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051223**
2. Descargar el PDF del acta
3. Verificar SHA-256: `fab7a46db7d917531e55b7edb63f32252dc65b309cac2caf1d02d0a9c1f18a6b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
