# Mesa 046306 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.333924+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUENTE PIEDRA
- **Local de votación**: IE 3088 VISTA ALEGRE (código 3031)
- **Ubigeo**: 140119

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 246
- Votos válidos: 193
- Participación: 82.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:42:38+00:00` | `2026-04-12 22:42:38 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:42:38+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:42:38+00:00` | `2026-04-12 22:42:38 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:47:05+00:00` | `2026-04-13 08:47:05 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:48:45+00:00` | `2026-04-13 08:48:45 (Lima)` |
| Última firma humana | `2026-04-13T13:49:08+00:00` | `2026-04-13 08:49:08 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.10 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:42:38 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:48:45 (Lima), es decir **10.10 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:42:37+00:00` | `2026-04-12 22:42:37 (Lima)` | -0.00h |
| 1 | PALOMINO ARBIETO ana Paula FIR 73503718 sw 5bb52a5a368635f798045726dcb1e7b107bc33c1 | 73503718 | `2026-04-13T13:48:45+00:00` | `2026-04-13 08:48:45 (Lima)` | +10.10h |
| 2 | PALOMINO LAURENTE carlos Erasmo FIR 10776787 sw 5dbcd0e161eeecf44b88d81f42ed31c8fbe61925 | 10776787 | `2026-04-13T13:48:58+00:00` | `2026-04-13 08:48:58 (Lima)` | +10.11h |
| 3 | PAREDES JULCA catherine Rocio FIR 70513519 sw fd87759f6910b04ea08f48712e551b9f9ce2cd39 | 70513519 | `2026-04-13T13:49:08+00:00` | `2026-04-13 08:49:08 (Lima)` | +10.11h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046306**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c9eef93ac98a41b6486fa58e36f8cdb1d7677bd60b4afe796c484bc2c43f8111`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
