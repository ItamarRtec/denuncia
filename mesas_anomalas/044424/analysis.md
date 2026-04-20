# Mesa 044424 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.386679+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LURIGANCHO
- **Local de votación**: IEP FRANCOIS VIETE (código 13462)
- **Ubigeo**: 140112

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 223
- Votos válidos: 192
- Participación: 74.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:57:35+00:00` | `2026-04-12 19:57:35 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:57:35+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:57:35+00:00` | `2026-04-12 19:57:35 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:50:00+00:00` | `2026-04-12 21:50:00 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:50:10+00:00` | `2026-04-12 21:50:10 (Lima)` |
| Última firma humana | `2026-04-13T02:50:31+00:00` | `2026-04-12 21:50:31 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.88 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:57:35 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:50:10 (Lima), es decir **1.88 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:57:33+00:00` | `2026-04-12 19:57:33 (Lima)` | -0.00h |
| 1 | BARRANTES CABANILLAS gladys FIR 42410555 sw 6ef2f99226ed201729ba404334f9a23e68d9dcae | 42410555 | `2026-04-13T02:50:10+00:00` | `2026-04-12 21:50:10 (Lima)` | +1.88h |
| 2 | CAJALEON CALHUA lady Cristina FIR 70626705 sw 8c68c8a5fcf426a7f5c737813942a39ce3568d34 | 70626705 | `2026-04-13T02:50:21+00:00` | `2026-04-12 21:50:21 (Lima)` | +1.88h |
| 3 | AREVALO RUBIO kiara Dayanna FIR 71173295 sw cefb4db143755f5ee606b9e24a21d7ddc1e31474 | 71173295 | `2026-04-13T02:50:31+00:00` | `2026-04-12 21:50:31 (Lima)` | +1.88h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **044424**
2. Descargar el PDF del acta
3. Verificar SHA-256: `cc432220f1b5fd1f7cc58ceb19b4082df7dbfabba17c786e1056411fe3762507`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
