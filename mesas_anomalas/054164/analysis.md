# Mesa 054164 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.811494+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: INDEPENDENCIA
- **Local de votación**: IEI 0386 VICTOR RAUL HAYA DE LA TORRE (código 51331)
- **Ubigeo**: 140134

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 240
- Votos válidos: 204
- Participación: 80.268%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:49:16+00:00` | `2026-04-12 21:49:16 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:49:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:49:16+00:00` | `2026-04-12 21:49:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:20:28+00:00` | `2026-04-13 09:20:28 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:26:26+00:00` | `2026-04-13 09:26:26 (Lima)` |
| Última firma humana | `2026-04-13T14:31:21+00:00` | `2026-04-13 09:31:21 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.62 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:49:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:26:26 (Lima), es decir **11.62 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:49:13+00:00` | `2026-04-12 21:49:13 (Lima)` | -0.00h |
| 1 | SANCHEZ DIESTRA maryuri FIR 73495166 sw 6585657167fa7d4aec52f2f9bd32f196152595f6 | 73495166 | `2026-04-13T14:26:26+00:00` | `2026-04-13 09:26:26 (Lima)` | +11.62h |
| 2 | SANCHEZ MEZA antoni Piero FIR 72788661 sw 3692692bb2d164f549c03d92581ebd5b2f83502a | 72788661 | `2026-04-13T14:28:48+00:00` | `2026-04-13 09:28:48 (Lima)` | +11.66h |
| 3 | RAMIREZ VALIENTE jose Luis FIR 75255749 sw 253bc223aeee50dd9edeb98c9226535fc5c7e231 | 75255749 | `2026-04-13T14:30:22+00:00` | `2026-04-13 09:30:22 (Lima)` | +11.69h |
| 4 | MENDOZA COLAN miguel Angel FIR 42240514 sw f60e62ae5f14729c74fc7e334d6cdc53b1492952 | 42240514 | `2026-04-13T14:31:21+00:00` | `2026-04-13 09:31:21 (Lima)` | +11.70h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054164**
2. Descargar el PDF del acta
3. Verificar SHA-256: `ef5b6dcfd247cd234bcfcaef6706db0a11e6140706431dda0aab0f629303c0ca`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
