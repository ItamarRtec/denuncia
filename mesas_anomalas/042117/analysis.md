# Mesa 042117 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.354285+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: IEI PARROQUIAL JESUS MAESTRO (código 12988)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 267
- Votos válidos: 239
- Participación: 89.298%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:43:54+00:00` | `2026-04-12 20:43:54 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:43:54+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:43:54+00:00` | `2026-04-12 20:43:54 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:33:16+00:00` | `2026-04-12 21:33:16 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:33:48+00:00` | `2026-04-12 21:33:48 (Lima)` |
| Última firma humana | `2026-04-13T02:34:09+00:00` | `2026-04-12 21:34:09 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.83 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:43:54 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:33:48 (Lima), es decir **0.83 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:43:52+00:00` | `2026-04-12 20:43:52 (Lima)` | -0.00h |
| 1 | BULNES PEREZ carlos Alberto FIR 73023741 sw 261f467509b2667955b1f00d91a568a0004903a6 | 73023741 | `2026-04-13T02:33:48+00:00` | `2026-04-12 21:33:48 (Lima)` | +0.83h |
| 2 | ALBUJAR SAAVEDRA jose Luis FIR 40404286 sw c298f8498bb8322d26a120f916214d1c1898aadf | 40404286 | `2026-04-13T02:33:58+00:00` | `2026-04-12 21:33:58 (Lima)` | +0.83h |
| 3 | ARIAS GONZALES franklin Christian FIR 42194447 sw eeeeaeedd786c89bc8640650005480521ad2cdcb | 42194447 | `2026-04-13T02:34:09+00:00` | `2026-04-12 21:34:09 (Lima)` | +0.84h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042117**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e9e3756077a8e7b4905c218d262754e4bcb17dc15235b93ab364a8f73d503d6d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
