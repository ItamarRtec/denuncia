# Mesa 062064 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.977944+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IEP SACO OLIVEROS HELICOIDAL (código 14114)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 293
- Votos emitidos: 238
- Votos válidos: 218
- Participación: 81.229%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:39:59+00:00` | `2026-04-12 22:39:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:39:59+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:39:59+00:00` | `2026-04-12 22:39:59 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:19:23+00:00` | `2026-04-13 09:19:23 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:19:56+00:00` | `2026-04-13 09:19:56 (Lima)` |
| Última firma humana | `2026-04-13T14:20:06+00:00` | `2026-04-13 09:20:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.67 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:39:59 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:19:56 (Lima), es decir **10.67 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:39:57+00:00` | `2026-04-12 22:39:57 (Lima)` | -0.00h |
| 1 | PALOMINO CHICCHON katherine Jhunnet FIR 70018693 sw 8da2f0144f0897856f15b5f370230ca19459ed0f | 70018693 | `2026-04-13T14:19:56+00:00` | `2026-04-13 09:19:56 (Lima)` | +10.67h |
| 2 | PANDURO LOPE dagni Yuli FIR 73054194 sw 6f90b00afc1c0d04cf2484f0fcb1349f3ad1df18 | 73054194 | `2026-04-13T14:20:06+00:00` | `2026-04-13 09:20:06 (Lima)` | +10.67h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **062064**
2. Descargar el PDF del acta
3. Verificar SHA-256: `a10be0b590899231ff616be81715201259386a3697d87b0451151a1e09c81fe7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
