# Mesa 051147 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.447884+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: POLIDEPORTIVO SAGITARIO (código 18054)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 285
- Votos válidos: 277
- Participación: 95.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:49:22+00:00` | `2026-04-12 20:49:22 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:49:22+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:49:22+00:00` | `2026-04-12 20:49:22 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:35:52+00:00` | `2026-04-13 08:35:52 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:36:51+00:00` | `2026-04-13 08:36:51 (Lima)` |
| Última firma humana | `2026-04-13T13:40:19+00:00` | `2026-04-13 08:40:19 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.79 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:49:22 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:36:51 (Lima), es decir **11.79 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:49:19+00:00` | `2026-04-12 20:49:19 (Lima)` | -0.00h |
| 1 | BARDALES GOICOCHEA ian Franco FIR 70253461 sw 8177394410b8d2c60b6a614cd5b1eaa73388fd85 | 70253461 | `2026-04-13T13:36:51+00:00` | `2026-04-13 08:36:51 (Lima)` | +11.79h |
| 2 | BONILLA FARFAN bruno FIR 76952903 sw 6167a369e0abb841939667a2c8a0fe75ae5194a0 | 76952903 | `2026-04-13T13:37:10+00:00` | `2026-04-13 08:37:10 (Lima)` | +11.80h |
| 3 | CABRERA URTEAGA debora Daniela FIR 70866060 sw 7eba25712f2f7aab111dbcfd1f8a45132cdb09d6 | 70866060 | `2026-04-13T13:37:36+00:00` | `2026-04-13 08:37:36 (Lima)` | +11.80h |
| 4 | AQUIJE SOTO ivan Antonio FIR 08505925 sw ad2f72d239b6cef4cee8c949380b5b3692bbfc17 | 08505925 | `2026-04-13T13:40:19+00:00` | `2026-04-13 08:40:19 (Lima)` | +11.85h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051147**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2db2f3da53546e710218b9aa25e473831f4acee7e2049bed73e1546651bd8bf2`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
