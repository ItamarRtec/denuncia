# Mesa 047863 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.190824+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN ISIDRO
- **Local de votación**: IE EMBLEMATICA ALFONSO UGARTE - ESTADIO (código 53857)
- **Ubigeo**: 140124

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 297
- Votos emitidos: 202
- Votos válidos: 192
- Participación: 68.013%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:36:47+00:00` | `2026-04-12 20:36:47 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:36:47+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:36:47+00:00` | `2026-04-12 20:36:47 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:13:43+00:00` | `2026-04-12 22:13:43 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:13:59+00:00` | `2026-04-12 22:13:59 (Lima)` |
| Última firma humana | `2026-04-13T03:15:01+00:00` | `2026-04-12 22:15:01 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.62 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:36:47 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:13:59 (Lima), es decir **1.62 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:36:45+00:00` | `2026-04-12 20:36:45 (Lima)` | -0.00h |
| 1 | FLORES MARTICORENA amanda Belinda FIR 10542179 sw 83a1341805cc7997091809fc36642b5a8946d2c4 | 10542179 | `2026-04-13T03:13:59+00:00` | `2026-04-12 22:13:59 (Lima)` | +1.62h |
| 2 | FERNANDEZ JERI oscar Edgard FIR 08261756 sw febe60738e1a4d12a501e3a1b0c9e47e98a376ee | 08261756 | `2026-04-13T03:14:11+00:00` | `2026-04-12 22:14:11 (Lima)` | +1.62h |
| 3 | FERNANDEZ REYES francis Angel De Jesus FIR 60825342 sw ddaba41a9dd84751b84581deab7e6233ed3b3729 | 60825342 | `2026-04-13T03:14:23+00:00` | `2026-04-12 22:14:23 (Lima)` | +1.63h |
| 4 | AYLLON BRAVO dylan Frank Cesar FIR 70620832 sw 5d96858a4fb8b682528037953d5ab7e9fc5b6ea3 | 70620832 | `2026-04-13T03:14:49+00:00` | `2026-04-12 22:14:49 (Lima)` | +1.63h |
| 5 | FLORES CORTEZ juan Armando FIR 08261823 sw 0e6033f806cb749d6fc61cf47dd264235218423a | 08261823 | `2026-04-13T03:15:01+00:00` | `2026-04-12 22:15:01 (Lima)` | +1.64h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **047863**
2. Descargar el PDF del acta
3. Verificar SHA-256: `aaa05ce44a23a68253bd9ef96d2e09c69c893f92ee078e60dcad9654d73b377c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
