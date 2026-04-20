# Mesa 041886 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.238917+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: IE 7076 BRISAS DE VILLA (código 2871)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 228
- Votos válidos: 195
- Participación: 76.254%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:23:02+00:00` | `2026-04-12 21:23:02 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:23:02+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:23:02+00:00` | `2026-04-12 21:23:02 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:51:59+00:00` | `2026-04-13 08:51:59 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:53:01+00:00` | `2026-04-13 08:53:01 (Lima)` |
| Última firma humana | `2026-04-13T13:53:17+00:00` | `2026-04-13 08:53:17 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.50 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:23:02 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:53:01 (Lima), es decir **11.50 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:22:59+00:00` | `2026-04-12 21:22:59 (Lima)` | -0.00h |
| 1 | CESAR RAMOS david Augusto FIR 41348350 sw 27954627ee1cad8b29bdaab9c7ed22a1a7684e1c | 41348350 | `2026-04-13T13:53:01+00:00` | `2026-04-13 08:53:01 (Lima)` | +11.50h |
| 2 | CASTRO CORCUERA loretta Liliana Ynes FIR 07028153 sw da0f378c6a98fa576d948ff3c2cc3df8d7a0ea92 | 07028153 | `2026-04-13T13:53:17+00:00` | `2026-04-13 08:53:17 (Lima)` | +11.50h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041886**
2. Descargar el PDF del acta
3. Verificar SHA-256: `a719fdddad60989e2c8932232ce8633e38dff246152f84148d4cd3eb96edffd1`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
