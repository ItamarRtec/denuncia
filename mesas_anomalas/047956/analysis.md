# Mesa 047956 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.337999+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN ISIDRO
- **Local de votación**: ESTACIONAMIENTO PETROPERU (código 54844)
- **Ubigeo**: 140124

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 212
- Votos válidos: 202
- Participación: 70.903%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:36:46+00:00` | `2026-04-12 21:36:46 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:36:46+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:36:46+00:00` | `2026-04-12 21:36:46 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:47:42+00:00` | `2026-04-13 08:47:42 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:06:00+00:00` | `2026-04-13 09:06:00 (Lima)` |
| Última firma humana | `2026-04-13T14:11:52+00:00` | `2026-04-13 09:11:52 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.49 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:36:46 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:06:00 (Lima), es decir **11.49 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:32:11+00:00` | `2026-04-12 21:32:11 (Lima)` | -0.08h |
| 1 | TORRES SANTOLALLA jose Luis FIR 06767386 sw cbc7b582527ddc9f6e1b771c95eab095d6c7676d | 06767386 | `2026-04-13T14:06:00+00:00` | `2026-04-13 09:06:00 (Lima)` | +11.49h |
| 2 | TOYODA KANASHIRO ernesto FIR 09672559 sw 0f1fcea50b3022dff2e691618933e2b4fcb5bc80 | 09672559 | `2026-04-13T14:11:52+00:00` | `2026-04-13 09:11:52 (Lima)` | +11.59h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **047956**
2. Descargar el PDF del acta
3. Verificar SHA-256: `41cc9a35ff531c39446dc1ea4d1fa73f50bd5138a27e4a03759e73fa2e01e99e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
