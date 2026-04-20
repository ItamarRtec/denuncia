# Mesa 045749 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.639190+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PACHACÁMAC
- **Local de votación**: IE 7258 (código 54002)
- **Ubigeo**: 140116

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 230
- Votos emitidos: 168
- Votos válidos: 147
- Participación: 73.043%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:44:03+00:00` | `2026-04-12 21:44:03 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:44:03+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:44:03+00:00` | `2026-04-12 21:44:03 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:01:14+00:00` | `2026-04-13 09:01:14 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:01:31+00:00` | `2026-04-13 09:01:31 (Lima)` |
| Última firma humana | `2026-04-13T14:02:29+00:00` | `2026-04-13 09:02:29 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.29 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:44:03 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:01:31 (Lima), es decir **11.29 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:43:59+00:00` | `2026-04-12 21:43:59 (Lima)` | -0.00h |
| 1 | ARANA ESPINOZA maria Antonieta FIR 07267442 sw ab1da0552f1028ad7a094ea87f8af8dd283b7642 | 07267442 | `2026-04-13T14:01:31+00:00` | `2026-04-13 09:01:31 (Lima)` | +11.29h |
| 2 | ALBITES MINAYA efrain FIR 33257529 sw e2e4666f6fa84c34b5176f22d74bf0288f6d6003 | 33257529 | `2026-04-13T14:01:44+00:00` | `2026-04-13 09:01:44 (Lima)` | +11.29h |
| 3 | ANTONIO UNOCC honorato FIR 23462156 sw f755b6c5afecf2ccf81769fdfb3abafab2b53ae5 | 23462156 | `2026-04-13T14:02:04+00:00` | `2026-04-13 09:02:04 (Lima)` | +11.30h |
| 4 | GALVAN JAUREGUI rigoberta FIR 40908215 sw 219a041d62a1272c32af994a5f85462547a3a32a | 40908215 | `2026-04-13T14:02:29+00:00` | `2026-04-13 09:02:29 (Lima)` | +11.31h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045749**
2. Descargar el PDF del acta
3. Verificar SHA-256: `299d12997046b0d512bafa01108c316861e591bc1df0a362bbf5abf8993a11ba`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
