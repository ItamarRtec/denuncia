# Mesa 061918 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.926669+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: UNIVERSIDAD SAN MARTIN DE PORRES (código 3595)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 238
- Votos válidos: 210
- Participación: 79.599%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:57:26+00:00` | `2026-04-12 21:57:26 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:57:26+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:57:26+00:00` | `2026-04-12 21:57:26 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:39:50+00:00` | `2026-04-13 08:39:50 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:40:08+00:00` | `2026-04-13 08:40:08 (Lima)` |
| Última firma humana | `2026-04-13T13:40:29+00:00` | `2026-04-13 08:40:29 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.71 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:57:26 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:40:08 (Lima), es decir **10.71 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:57:23+00:00` | `2026-04-12 21:57:23 (Lima)` | -0.00h |
| 1 | MURILLO QUISPE aureliano FIR 10043285 sw 813c960a2cec1b19ff4d98678f0c82f784d9da8b | 10043285 | `2026-04-13T13:40:08+00:00` | `2026-04-13 08:40:08 (Lima)` | +10.71h |
| 2 | MORENO ROMERO jaqueline Marivel FIR 09768244 sw 37655f5a21830199914a5934a2fa553a11a705e7 | 09768244 | `2026-04-13T13:40:19+00:00` | `2026-04-13 08:40:19 (Lima)` | +10.71h |
| 3 | NAJARRO VASQUEZ juan Victor FIR 75695097 sw f6a10b2c28f2ec87e345e87e58731f50881c4c2b | 75695097 | `2026-04-13T13:40:29+00:00` | `2026-04-13 08:40:29 (Lima)` | +10.72h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061918**
2. Descargar el PDF del acta
3. Verificar SHA-256: `fbaeb5dbfada003d487e9a2f964a77b4b202a279865c6325aef5ee3318cbd596`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
