# Mesa 040268 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.737432+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IE 3060 ALFONSO UGARTE VERNAL (código 2808)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 245
- Votos válidos: 226
- Participación: 81.94%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:55:30+00:00` | `2026-04-12 19:55:30 (Lima)` |
| `C` | Contabilizada | `2026-04-13T00:54:07+00:00` | `2026-04-12 19:54:07 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:55:30+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:55:30+00:00` | `2026-04-12 19:55:30 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:18:49+00:00` | `2026-04-12 21:18:49 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:19:06+00:00` | `2026-04-12 21:19:06 (Lima)` |
| Última firma humana | `2026-04-13T02:19:53+00:00` | `2026-04-12 21:19:53 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.39 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:55:30 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:19:06 (Lima), es decir **1.39 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:54:05+00:00` | `2026-04-12 19:54:05 (Lima)` | -0.02h |
| 1 | LUCERO FLORES victor Felipe FIR 46021259 sw be8fbf3642dccb994a905ffd8be1a11ee1bc7ae5 | 46021259 | `2026-04-13T02:19:06+00:00` | `2026-04-12 21:19:06 (Lima)` | +1.39h |
| 2 | MALDONADO CAICEDO jorge Joston FIR 06012372 sw 815eca5a587f302a64df299b0f39eec31b7debee | 06012372 | `2026-04-13T02:19:37+00:00` | `2026-04-12 21:19:37 (Lima)` | +1.40h |
| 3 | LEZAMETA MALPARTIDA florenzo FIR 06927517 sw 55039073e6e4ee577f9b116350c38d16b8033b1a | 06927517 | `2026-04-13T02:19:53+00:00` | `2026-04-12 21:19:53 (Lima)` | +1.41h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **040268**
2. Descargar el PDF del acta
3. Verificar SHA-256: `0b09b0cef8a7a263f201afb863d45497f6957009644f65fd82e9bc6567ec35dc`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
