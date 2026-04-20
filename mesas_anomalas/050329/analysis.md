# Mesa 050329 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.351633+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: IE LICEO NAVAL CONTALMIRANTE MONTERO (código 54585)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 210
- Votos válidos: 194
- Participación: 70.234%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:59:01+00:00` | `2026-04-12 20:59:01 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:59:01+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:59:01+00:00` | `2026-04-12 20:59:01 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:41:18+00:00` | `2026-04-13 00:41:18 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:41:49+00:00` | `2026-04-13 00:41:49 (Lima)` |
| Última firma humana | `2026-04-13T05:42:41+00:00` | `2026-04-13 00:42:41 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.71 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:59:01 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:41:49 (Lima), es decir **3.71 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:58:58+00:00` | `2026-04-12 20:58:58 (Lima)` | -0.00h |
| 1 | ALVARADO GUTIERREZ violeta Ginette FIR 09644089 sw af81e1f2b81f7eec10b6b13ba5c060288fae6680 | 09644089 | `2026-04-13T05:41:49+00:00` | `2026-04-13 00:41:49 (Lima)` | +3.71h |
| 2 | ALVARADO RENGIFO carlos FIR 70693782 sw 4c7f638653d205d9ea8e33370ee1d64284d8426f | 70693782 | `2026-04-13T05:42:01+00:00` | `2026-04-13 00:42:01 (Lima)` | +3.72h |
| 3 | ALDAVE AYALA jacqueline Milagros FIR 40392054 sw 3cdb5a3b0791413e23528ef33a48f79d4fc1b1ea | 40392054 | `2026-04-13T05:42:16+00:00` | `2026-04-13 00:42:16 (Lima)` | +3.72h |
| 4 | FREGEIRO MALCA maruccia Giuliana FIR 40860594 sw 53a3718d69b3ea95ebf3acfc30054c4d140d7f34 | 40860594 | `2026-04-13T05:42:41+00:00` | `2026-04-13 00:42:41 (Lima)` | +3.73h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050329**
2. Descargar el PDF del acta
3. Verificar SHA-256: `21ba5c8d50003e86e9ddaa2b8a6782cabb5edad15e396e827cdbe0a379319126`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
