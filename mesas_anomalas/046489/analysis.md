# Mesa 046489 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.033113+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUENTE PIEDRA
- **Local de votación**: IEP ALFRED NOBEL (código 3045)
- **Ubigeo**: 140119

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 245
- Votos válidos: 205
- Participación: 81.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:04:59+00:00` | `2026-04-12 22:04:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:04:59+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:04:59+00:00` | `2026-04-12 22:04:59 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:46:59+00:00` | `2026-04-13 09:46:59 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:47:27+00:00` | `2026-04-13 09:47:27 (Lima)` |
| Última firma humana | `2026-04-13T14:48:12+00:00` | `2026-04-13 09:48:12 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.71 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:04:59 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:47:27 (Lima), es decir **11.71 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:04:57+00:00` | `2026-04-12 22:04:57 (Lima)` | -0.00h |
| 1 | BELTRAN CASTILLO edynson FIR 43066346 sw c7954ceffe4e6aa14d8814fb30dbc1a62374684e | 43066346 | `2026-04-13T14:47:27+00:00` | `2026-04-13 09:47:27 (Lima)` | +11.71h |
| 2 | BECERRA ERAZO claudia Beatriz FIR 47007603 sw 5e40e57c80c45f78b1668a8c5f05130bc9509404 | 47007603 | `2026-04-13T14:47:39+00:00` | `2026-04-13 09:47:39 (Lima)` | +11.71h |
| 3 | CASTILLO CUEVA juan Roberto FIR 09943994 sw 7d15dfaa31a1734450fd32523318e671f814e3ae | 09943994 | `2026-04-13T14:47:52+00:00` | `2026-04-13 09:47:52 (Lima)` | +11.71h |
| 4 | SILUPU CALVO nataly Mercedes FIR 47296949 sw cffd9d107f3400153b9fdb6f6879b15ef318fa65 | 47296949 | `2026-04-13T14:48:12+00:00` | `2026-04-13 09:48:12 (Lima)` | +11.72h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046489**
2. Descargar el PDF del acta
3. Verificar SHA-256: `d0fc8cff7fea1bdffd9cb9877a3b7b7cb0ce9733e291626a5e48b3cece259bf6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
