# Mesa 046202 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.396285+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUENTE PIEDRA
- **Local de votación**: IE 2081 PERU SUIZA (código 3027)
- **Ubigeo**: 140119

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 230
- Votos válidos: 205
- Participación: 76.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:23:02+00:00` | `2026-04-12 21:23:02 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:23:02+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:23:02+00:00` | `2026-04-12 21:23:02 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:58:06+00:00` | `2026-04-13 08:58:06 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:58:30+00:00` | `2026-04-13 08:58:30 (Lima)` |
| Última firma humana | `2026-04-13T13:59:15+00:00` | `2026-04-13 08:59:15 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.59 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:23:02 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:58:30 (Lima), es decir **11.59 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:22:59+00:00` | `2026-04-12 21:22:59 (Lima)` | -0.00h |
| 1 | ESPINOZA GARCIA jeniffer Soledad FIR 46190168 sw fc641ca88bbc4bba3929ca665a9c0253fc39ae2f | 46190168 | `2026-04-13T13:58:30+00:00` | `2026-04-13 08:58:30 (Lima)` | +11.59h |
| 2 | ERAZO ROJAS pablo Fortunato FIR 10162898 sw 648b43d8ca632129e74564ed93bbb4fcd8b7c7dc | 10162898 | `2026-04-13T13:59:01+00:00` | `2026-04-13 08:59:01 (Lima)` | +11.60h |
| 3 | DOMINGUEZ ANCHELIA brando Taylor FIR 75361848 sw 9ab3b095051e4302c7e4e382b1c89d760f3554a8 | 75361848 | `2026-04-13T13:59:15+00:00` | `2026-04-13 08:59:15 (Lima)` | +11.60h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046202**
2. Descargar el PDF del acta
3. Verificar SHA-256: `1b6decb80334c151f6d5b1aa5177c102d0ab5a30b55cdd29a75f143ea1ba2957`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
