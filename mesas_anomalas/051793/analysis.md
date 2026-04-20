# Mesa 051793 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.019375+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: IE NUESTRA SEÑORA DE LOURDES (código 3233)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 251
- Votos válidos: 231
- Participación: 83.946%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:22:45+00:00` | `2026-04-12 20:22:45 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:22:45+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:22:45+00:00` | `2026-04-12 20:22:45 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:16:42+00:00` | `2026-04-13 00:16:42 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:16:58+00:00` | `2026-04-13 00:16:58 (Lima)` |
| Última firma humana | `2026-04-13T05:17:23+00:00` | `2026-04-13 00:17:23 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.90 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:22:45 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:16:58 (Lima), es decir **3.90 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:22:43+00:00` | `2026-04-12 20:22:43 (Lima)` | -0.00h |
| 1 | RIEGA FALCONI luis Alberto FIR 44652584 sw 309b1f922d001c58c8491f95d692ae3d49cbc475 | 44652584 | `2026-04-13T05:16:58+00:00` | `2026-04-13 00:16:58 (Lima)` | +3.90h |
| 2 | REQUENA RAMIREZ elida Rosaura FIR 40419803 sw 8c66a5cff03c51c2b576ac3c0cd3763f13a8041b | 40419803 | `2026-04-13T05:17:11+00:00` | `2026-04-13 00:17:11 (Lima)` | +3.91h |
| 3 | REDUCIENDO MILLA alex Matias FIR 70091994 sw f37d38deda4e5f709775729db20573eae5499360 | 70091994 | `2026-04-13T05:17:23+00:00` | `2026-04-13 00:17:23 (Lima)` | +3.91h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051793**
2. Descargar el PDF del acta
3. Verificar SHA-256: `a6baabc94c79d2b69f078c8e05420e436989f378683194ecfa8bf0d7bef1cf49`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
