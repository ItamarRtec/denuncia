# Mesa 061587 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.364134+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IE 106 ABRAHAM VALDELOMAR (código 3579)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 268
- Votos válidos: 241
- Participación: 89.632%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:38:04+00:00` | `2026-04-12 20:38:04 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:38:04+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:38:04+00:00` | `2026-04-12 20:38:04 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:09:37+00:00` | `2026-04-13 08:09:37 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:10:27+00:00` | `2026-04-13 08:10:27 (Lima)` |
| Última firma humana | `2026-04-13T13:10:51+00:00` | `2026-04-13 08:10:51 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.54 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:38:04 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:10:27 (Lima), es decir **11.54 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:38:02+00:00` | `2026-04-12 20:38:02 (Lima)` | -0.00h |
| 1 | DE LA CRUZ KELWAY valerio Nicolas FIR 77017277 sw a9702c2e61d773084f47e2ead8949d4836ff5a6d | 77017277 | `2026-04-13T13:10:27+00:00` | `2026-04-13 08:10:27 (Lima)` | +11.54h |
| 2 | ESPINOZA BARRIENTOS sonia Isabel FIR 07105839 sw 7347a872ef1753bf55fd4751267c23855dac4515 | 07105839 | `2026-04-13T13:10:39+00:00` | `2026-04-13 08:10:39 (Lima)` | +11.54h |
| 3 | ENRRIQUES OLARTE maruja FIR 44056687 sw 0f641e2eb48bf20b1dd8ab88849800bde3dd1a66 | 44056687 | `2026-04-13T13:10:51+00:00` | `2026-04-13 08:10:51 (Lima)` | +11.55h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061587**
2. Descargar el PDF del acta
3. Verificar SHA-256: `80dbb61b423bf69116641ca744b029192840ab7dc6c8b50867d5f90993a4dcb3`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
