# Mesa 040422 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.303777+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IE FE Y ALEGRIA 10 (código 2828)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 252
- Votos válidos: 220
- Participación: 84.281%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:26:16+00:00` | `2026-04-12 21:26:16 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:16:56+00:00` | `2026-04-12 21:16:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:26:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:26:16+00:00` | `2026-04-12 21:26:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T11:39:27+00:00` | `2026-04-13 06:39:27 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T11:39:53+00:00` | `2026-04-13 06:39:53 (Lima)` |
| Última firma humana | `2026-04-13T11:42:52+00:00` | `2026-04-13 06:42:52 (Lima)` |

**Brecha primera firma humana vs publicación:** **+9.23 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:26:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 06:39:53 (Lima), es decir **9.23 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:16:54+00:00` | `2026-04-12 21:16:54 (Lima)` | -0.16h |
| 1 | HUAYNATE VALLEJO norma Mariela FIR 43274045 sw f16be60a45761d2a7a71d4303179fe03d761206b | 43274045 | `2026-04-13T11:39:53+00:00` | `2026-04-13 06:39:53 (Lima)` | +9.23h |
| 2 | HUAMAN TTITO maria Purificada FIR 10392037 sw 7811f4a7ede8e8d6a030e55334f90ef15b0e01c8 | 10392037 | `2026-04-13T11:42:37+00:00` | `2026-04-13 06:42:37 (Lima)` | +9.27h |
| 3 | HUAMAN GUZMAN dante Isaias FIR 09980467 sw d836c6557f82cc648f0bc9445b6368e870125a82 | 09980467 | `2026-04-13T11:42:52+00:00` | `2026-04-13 06:42:52 (Lima)` | +9.28h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **040422**
2. Descargar el PDF del acta
3. Verificar SHA-256: `10414240ca171e4bf992a8cc2fb35ada1b66ed8dc19a83615688369a1a258fd2`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
