# Mesa 051375 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.708774+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IEP INNOVA SCHOOLS SURCO - AMBROSIO (código 52886)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 215
- Votos válidos: 197
- Participación: 71.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T08:48:17+00:00` | `2026-04-13 03:48:17 (Lima)` |
| `C` | Contabilizada | `2026-04-13T01:16:17+00:00` | `2026-04-12 20:16:17 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T08:48:17+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T08:48:17+00:00` | `2026-04-13 03:48:17 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:48:44+00:00` | `2026-04-13 07:48:44 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:49:10+00:00` | `2026-04-13 07:49:10 (Lima)` |
| Última firma humana | `2026-04-13T12:50:04+00:00` | `2026-04-13 07:50:04 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.01 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-13 03:48:17 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:49:10 (Lima), es decir **4.01 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:16:15+00:00` | `2026-04-12 20:16:15 (Lima)` | -7.53h |
| 1 | DE LA TORRE CALLE ada Luisa FIR 22067657 sw c9229b85cc1a7280d2483a2a81657ad02bde3215 | 22067657 | `2026-04-13T12:49:10+00:00` | `2026-04-13 07:49:10 (Lima)` | +4.01h |
| 2 | DIAZ GARCIA marco Antonio FIR 42479673 sw 7a22ca3aee2fde89b05c275bf785d13c5ce17a04 | 42479673 | `2026-04-13T12:49:28+00:00` | `2026-04-13 07:49:28 (Lima)` | +4.02h |
| 3 | DE LA CRUZ CHARUN karina Lucia FIR 42146910 sw 1097f7d336d1d0feb9835af6b7a6ca21b7103f2d | 42146910 | `2026-04-13T12:49:42+00:00` | `2026-04-13 07:49:42 (Lima)` | +4.02h |
| 4 | DIAZ GONZALES luis Alberto FIR 10022775 sw a0c8de0031f92dc685133bdba728b41dd09c90d2 | 10022775 | `2026-04-13T12:50:04+00:00` | `2026-04-13 07:50:04 (Lima)` | +4.03h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051375**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3633c8076d8d4108aced0579aaef1263a2c1a1cfca737399166057b52328e693`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
