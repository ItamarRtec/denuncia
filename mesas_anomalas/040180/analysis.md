# Mesa 040180 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.644727+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IE 2097 (código 2802)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 245
- Votos válidos: 203
- Participación: 81.94%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:00:37+00:00` | `2026-04-12 21:00:37 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:00:37+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:00:37+00:00` | `2026-04-12 21:00:37 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:56:29+00:00` | `2026-04-12 22:56:29 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:56:57+00:00` | `2026-04-12 22:56:57 (Lima)` |
| Última firma humana | `2026-04-13T03:57:18+00:00` | `2026-04-12 22:57:18 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.94 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:00:37 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:56:57 (Lima), es decir **1.94 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:00:32+00:00` | `2026-04-12 21:00:32 (Lima)` | -0.00h |
| 1 | PASTRANA CARDENAS levith Yemir FIR 70168330 sw 371b02c1d59208f8bca7d6345053d6158062fce4 | 70168330 | `2026-04-13T03:56:57+00:00` | `2026-04-12 22:56:57 (Lima)` | +1.94h |
| 2 | PEREZ PAREDES walter Santos FIR 44441940 sw a886e37f025889f4ff0fe454dbd5172bddf76106 | 44441940 | `2026-04-13T03:57:06+00:00` | `2026-04-12 22:57:06 (Lima)` | +1.94h |
| 3 | PRADO ASTOCONDOR ines Consuelo FIR 08095219 sw ac43a0dcf2ee1dac2a4a84e344b16768c23eb0a7 | 08095219 | `2026-04-13T03:57:18+00:00` | `2026-04-12 22:57:18 (Lima)` | +1.94h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **040180**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2923b4b80bb610a57d4e56f47c06c290aa19cbecf8655c3dd08b9603b615ad06`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
