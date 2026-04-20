# Mesa 042344 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.293678+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: CEP SAN ALFONSO MARIA (código 51797)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 247
- Votos válidos: 221
- Participación: 82.609%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:09:16+00:00` | `2026-04-12 20:09:16 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:09:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:09:16+00:00` | `2026-04-12 20:09:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:14:37+00:00` | `2026-04-12 21:14:37 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:14:58+00:00` | `2026-04-12 21:14:58 (Lima)` |
| Última firma humana | `2026-04-13T02:15:33+00:00` | `2026-04-12 21:15:33 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.09 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:09:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:14:58 (Lima), es decir **1.09 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:09:14+00:00` | `2026-04-12 20:09:14 (Lima)` | -0.00h |
| 1 | VILLAR VALERA yeimy Anderson FIR 77218930 sw 6def0a3063bdfe24cbd3e38c64aee45d11a8f515 | 77218930 | `2026-04-13T02:14:58+00:00` | `2026-04-12 21:14:58 (Lima)` | +1.09h |
| 2 | TENORIO VILLAVICENCIO miguel Angel FIR 22308013 sw 37a7a1e7a13633f57c93f687888a657bb23643c6 | 22308013 | `2026-04-13T02:15:18+00:00` | `2026-04-12 21:15:18 (Lima)` | +1.10h |
| 3 | VILLALOBOS TORRES juvixa Maricela FIR 76301299 sw 8db729954f73d3b87db6f1fe7b6fa18130edddbb | 76301299 | `2026-04-13T02:15:33+00:00` | `2026-04-12 21:15:33 (Lima)` | +1.10h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042344**
2. Descargar el PDF del acta
3. Verificar SHA-256: `9316c3adea3605d30c2b300f08d01df5f57e47a4879d8ca66c1d84ebc54f7773`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
