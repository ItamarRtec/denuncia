# Mesa 043415 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.035212+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA MOLINA
- **Local de votación**: UNIVERSIDAD NACIONAL AGRARIA LA MOLINA (código 2926)
- **Ubigeo**: 140110

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 295
- Votos emitidos: 216
- Votos válidos: 206
- Participación: 73.22%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:40:37+00:00` | `2026-04-12 20:40:37 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:40:37+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:40:37+00:00` | `2026-04-12 20:40:37 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:08:41+00:00` | `2026-04-12 22:08:41 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:09:00+00:00` | `2026-04-12 22:09:00 (Lima)` |
| Última firma humana | `2026-04-13T03:10:07+00:00` | `2026-04-12 22:10:07 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.47 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:40:37 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:09:00 (Lima), es decir **1.47 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:40:35+00:00` | `2026-04-12 20:40:35 (Lima)` | -0.00h |
| 1 | VALDEIGLESIAS HERRERA karim FIR 09616589 sw 2d6d079bb3febd10823cbd87fd690269d41293f7 | 09616589 | `2026-04-13T03:09:00+00:00` | `2026-04-12 22:09:00 (Lima)` | +1.47h |
| 2 | VADILLO GALVEZ ricardo Zosimo FIR 07975303 sw 3e8471f53c69e2e7894b424451f6bb8b3123c7a7 | 07975303 | `2026-04-13T03:09:14+00:00` | `2026-04-12 22:09:14 (Lima)` | +1.48h |
| 3 | VALENZUELA CHADWICK DE JAGUANDE ana Maria Cecilia FIR 08249163 sw ebe3c9955dd9e3b44fb2a37f08aebf507c7b6153 | 08249163 | `2026-04-13T03:09:29+00:00` | `2026-04-12 22:09:29 (Lima)` | +1.48h |
| 4 | PEREZ SANCHEZ juana FIR 08956222 sw d6fcd3f7ea26ff543867888772e15155da37727d | 08956222 | `2026-04-13T03:09:52+00:00` | `2026-04-12 22:09:52 (Lima)` | +1.49h |
| 5 | CORDOVA LOPEZ linder Andres FIR 44258794 sw f61fc761f39fbd3e2afb73432889f2b74869a895 | 44258794 | `2026-04-13T03:10:07+00:00` | `2026-04-12 22:10:07 (Lima)` | +1.49h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **043415**
2. Descargar el PDF del acta
3. Verificar SHA-256: `cef0423c538617981f34fe624403566bdbf7a2fb4d7c73f6a56ea58c2019643f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
