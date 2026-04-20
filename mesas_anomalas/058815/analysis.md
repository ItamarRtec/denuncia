# Mesa 058815 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.534951+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN LUIS
- **Local de votación**: IE LOS EDUCADORES (código 3482)
- **Ubigeo**: 140138

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 295
- Votos emitidos: 222
- Votos válidos: 206
- Participación: 75.254%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:47:34+00:00` | `2026-04-12 20:47:34 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:47:34+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:47:34+00:00` | `2026-04-12 20:47:34 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:48:54+00:00` | `2026-04-12 22:48:54 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:49:23+00:00` | `2026-04-12 22:49:23 (Lima)` |
| Última firma humana | `2026-04-13T03:49:51+00:00` | `2026-04-12 22:49:51 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.03 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:47:34 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:49:23 (Lima), es decir **2.03 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:47:31+00:00` | `2026-04-12 20:47:31 (Lima)` | -0.00h |
| 1 | MERA CRUZ maria Justina FIR 08433235 sw cdc1b0df303421b5080ab9263173c8f04b6bb889 | 08433235 | `2026-04-13T03:49:23+00:00` | `2026-04-12 22:49:23 (Lima)` | +2.03h |
| 2 | MENDOZA GERVACIO angie FIR 70553411 sw 74bac925de05ad6fb93625723a1abd12b44a46c9 | 70553411 | `2026-04-13T03:49:36+00:00` | `2026-04-12 22:49:36 (Lima)` | +2.03h |
| 3 | MIGUEL DELGADO yaheli Estrella Celeste FIR 61043046 sw f0a3932ffa00fb1fba1e0bd35ed157ef44bf037b | 61043046 | `2026-04-13T03:49:51+00:00` | `2026-04-12 22:49:51 (Lima)` | +2.04h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **058815**
2. Descargar el PDF del acta
3. Verificar SHA-256: `ca8182c9caeab9ee549ac5604c3efa7e0508b4a69a94c4d5476c1455fba77e47`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
