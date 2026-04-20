# Mesa 036253 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.485775+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE 1168 HEROES DEL CENEPA (código 2658)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 230
- Votos válidos: 207
- Participación: 76.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:47:51+00:00` | `2026-04-12 20:47:51 (Lima)` |
| `C` | Contabilizada | `2026-04-13T01:16:10+00:00` | `2026-04-12 20:16:10 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:47:51+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:47:51+00:00` | `2026-04-12 20:47:51 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T11:13:31+00:00` | `2026-04-13 06:13:31 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T11:13:43+00:00` | `2026-04-13 06:13:43 (Lima)` |
| Última firma humana | `2026-04-13T11:14:05+00:00` | `2026-04-13 06:14:05 (Lima)` |

**Brecha primera firma humana vs publicación:** **+9.43 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:47:51 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 06:13:43 (Lima), es decir **9.43 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:16:08+00:00` | `2026-04-12 20:16:08 (Lima)` | -0.53h |
| 1 | TUESTA SANTISTEBAN sandra Nicoll FIR 60736862 sw b68307a1949a75edcdcc38abd9dbbd22199a9103 | 60736862 | `2026-04-13T11:13:43+00:00` | `2026-04-13 06:13:43 (Lima)` | +9.43h |
| 2 | VEGA ABANTO carlos Enrique FIR 08128318 sw 7b386e7c92df3ac55e8047d686312ba8a05798ec | 08128318 | `2026-04-13T11:13:54+00:00` | `2026-04-13 06:13:54 (Lima)` | +9.43h |
| 3 | TORRES HILARIO rigoberto FIR 09576558 sw 4a6c5d6222a10db1cf9024780cc086a91757ac64 | 09576558 | `2026-04-13T11:14:05+00:00` | `2026-04-13 06:14:05 (Lima)` | +9.44h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036253**
2. Descargar el PDF del acta
3. Verificar SHA-256: `89fd4dfe2ffc32edfe02f7ef0aa228c1bdf59687f9dafd815e9e50d0ffc8277e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
