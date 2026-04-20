# Mesa 055842 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.768877+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 637 VALLE SHAROM DE SJM (código 52092)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 242
- Votos válidos: 210
- Participación: 80.936%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:59:33+00:00` | `2026-04-12 21:59:33 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:14:14+00:00` | `2026-04-12 21:14:14 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:59:33+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:59:33+00:00` | `2026-04-12 21:59:33 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:03:10+00:00` | `2026-04-13 09:03:10 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:03:52+00:00` | `2026-04-13 09:03:52 (Lima)` |
| Última firma humana | `2026-04-13T14:04:28+00:00` | `2026-04-13 09:04:28 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.07 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:59:33 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:03:52 (Lima), es decir **11.07 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:14:12+00:00` | `2026-04-12 21:14:12 (Lima)` | -0.76h |
| 1 | PEREZ LUJAN victor Fernando FIR 74139245 sw ce39622ae9cf77629ccb24c9b8d4f841aadf6fc3 | 74139245 | `2026-04-13T14:03:52+00:00` | `2026-04-13 09:03:52 (Lima)` | +11.07h |
| 2 | PALACIOS FLORES elmer Daniel FIR 41218303 sw a3f454800235d2565682ce821ba7224a4ecebd7b | 41218303 | `2026-04-13T14:04:28+00:00` | `2026-04-13 09:04:28 (Lima)` | +11.08h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055842**
2. Descargar el PDF del acta
3. Verificar SHA-256: `73da2ecabde9a379a2d75453a8345b73f4341841a8142f7cc75cbe4beb43329f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
