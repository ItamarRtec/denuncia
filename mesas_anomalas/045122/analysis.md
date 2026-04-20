# Mesa 045122 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.720790+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: IE 6050 EMBLEMATICA JUANA ALARCO DE DAMMERT (código 2988)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 198
- Votos válidos: 186
- Participación: 66.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T04:46:27+00:00` | `2026-04-12 23:46:27 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T04:46:27+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T04:46:27+00:00` | `2026-04-12 23:46:27 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T15:55:35+00:00` | `2026-04-13 10:55:35 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T15:55:51+00:00` | `2026-04-13 10:55:51 (Lima)` |
| Última firma humana | `2026-04-13T15:57:08+00:00` | `2026-04-13 10:57:08 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.16 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 23:46:27 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 10:55:51 (Lima), es decir **11.16 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T04:46:26+00:00` | `2026-04-12 23:46:26 (Lima)` | -0.00h |
| 1 | DIAZ VASQUEZ ulises Joel FIR 40267033 sw c7e24be0f1c6812da7fe62bd44d0ae159893d89e | 40267033 | `2026-04-13T15:55:51+00:00` | `2026-04-13 10:55:51 (Lima)` | +11.16h |
| 2 | ESPINOZA TOLEDO brayan Michael FIR 61833138 sw d6624df1cbeec1a0f934cfd3a4790340b62041c3 | 61833138 | `2026-04-13T15:56:12+00:00` | `2026-04-13 10:56:12 (Lima)` | +11.16h |
| 3 | DONAYRE CHANG marcela Emma FIR 09648836 sw 03ae31b4de73d50839b65b126d52ae27d1891489 | 09648836 | `2026-04-13T15:56:34+00:00` | `2026-04-13 10:56:34 (Lima)` | +11.17h |
| 4 | PORTILLA CASTELLANO fiorella FIR 44011107 sw c6f58c9f21c325a17f5ef807c493225861ee62df | 44011107 | `2026-04-13T15:57:08+00:00` | `2026-04-13 10:57:08 (Lima)` | +11.18h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045122**
2. Descargar el PDF del acta
3. Verificar SHA-256: `34ea6119743382bead46c5e5780065e4900d3b206c9b34f1b49bb08feb8b72fa`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
