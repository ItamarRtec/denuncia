# Mesa 049997 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.290780+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: IEP SANTO DOMINGO EL APOSTOL (código 3168)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 298
- Votos emitidos: 223
- Votos válidos: 202
- Participación: 74.832%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:58:02+00:00` | `2026-04-12 19:58:02 (Lima)` |
| `C` | Contabilizada | `2026-04-13T00:54:23+00:00` | `2026-04-12 19:54:23 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:58:02+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:58:02+00:00` | `2026-04-12 19:58:02 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:28:42+00:00` | `2026-04-12 22:28:42 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:28:58+00:00` | `2026-04-12 22:28:58 (Lima)` |
| Última firma humana | `2026-04-13T03:29:26+00:00` | `2026-04-12 22:29:26 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.52 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:58:02 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:28:58 (Lima), es decir **2.52 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:54:21+00:00` | `2026-04-12 19:54:21 (Lima)` | -0.06h |
| 1 | TAMARIZ MALLQUI luis Enrique FIR 43596246 sw 44c26816a908d80482d2dbed26f19a2bbe87c643 | 43596246 | `2026-04-13T03:28:58+00:00` | `2026-04-12 22:28:58 (Lima)` | +2.52h |
| 2 | SORIA ROMERO evelyn Vanessa FIR 41909081 sw bee5dae43d3138f28c4ad31e9d39e97dd2bb56d8 | 41909081 | `2026-04-13T03:29:12+00:00` | `2026-04-12 22:29:12 (Lima)` | +2.52h |
| 3 | TANGHERLINI GALLO dora Manuela Adelina FIR 09859185 sw 2fd701ff31a9c5b29a61c4b87be8fcea9b9f30dd | 09859185 | `2026-04-13T03:29:26+00:00` | `2026-04-12 22:29:26 (Lima)` | +2.52h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **049997**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5fbd7facf7b934f5c3141bb77e25348fe3ed58da8d8ed43b62a87b970e93dccd`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
