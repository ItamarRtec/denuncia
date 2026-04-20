# Mesa 042081 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.010040+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: IE 7077 LOS REYES ROJOS (código 12980)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 250
- Votos válidos: 212
- Participación: 83.612%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:29:04+00:00` | `2026-04-12 20:29:04 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:29:04+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:29:04+00:00` | `2026-04-12 20:29:04 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:47:58+00:00` | `2026-04-12 21:47:58 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:48:44+00:00` | `2026-04-12 21:48:44 (Lima)` |
| Última firma humana | `2026-04-13T02:48:57+00:00` | `2026-04-12 21:48:57 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.33 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:29:04 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:48:44 (Lima), es decir **1.33 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:29:02+00:00` | `2026-04-12 20:29:02 (Lima)` | -0.00h |
| 1 | BRAVO QUISPE feliciano FIR 41699123 sw 45ac81704166d9a9fbb304a4b9afb535d513fd7b | 41699123 | `2026-04-13T02:48:44+00:00` | `2026-04-12 21:48:44 (Lima)` | +1.33h |
| 2 | BLAS SUAREZ aileen Xiomara FIR 61217168 sw 0d33d41adcb4af21c03bc71ee82c30c06e3b0810 | 61217168 | `2026-04-13T02:48:57+00:00` | `2026-04-12 21:48:57 (Lima)` | +1.33h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042081**
2. Descargar el PDF del acta
3. Verificar SHA-256: `efda7504e052d465499dc4aa4aad4184ced8574756de0bc07cf62d8f77c27e9b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
