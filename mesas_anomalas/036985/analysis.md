# Mesa 036985 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.873576+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IEP INNOVA SCHOOLS BERTELLO (código 54803)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 220
- Votos válidos: 199
- Participación: 73.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:21:45+00:00` | `2026-04-12 22:21:45 (Lima)` |
| `C` | Contabilizada | `2026-04-13T03:18:03+00:00` | `2026-04-12 22:18:03 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:21:45+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:21:45+00:00` | `2026-04-12 22:21:45 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:30:32+00:00` | `2026-04-13 09:30:32 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:30:54+00:00` | `2026-04-13 09:30:54 (Lima)` |
| Última firma humana | `2026-04-13T14:31:46+00:00` | `2026-04-13 09:31:46 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.15 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:21:45 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:30:54 (Lima), es decir **11.15 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:18:02+00:00` | `2026-04-12 22:18:02 (Lima)` | -0.06h |
| 1 | MARALLANO FERNANDEZ DAVILA fatima Mia FIR 47556356 sw 7c269c87c23c86d3051bc66b9460bd48560edb07 | 47556356 | `2026-04-13T14:30:54+00:00` | `2026-04-13 09:30:54 (Lima)` | +11.15h |
| 2 | MENDIOLAZA MOROTE marco Antonio FIR 09335968 sw 7032ef7b9124e37527f7ba92d3670c81bb089eb7 | 09335968 | `2026-04-13T14:31:23+00:00` | `2026-04-13 09:31:23 (Lima)` | +11.16h |
| 3 | MARTINEZ PAZ elvira Monica FIR 09430351 sw 357d32b4d89478e07c46498c7bbffbc9afddbcb5 | 09430351 | `2026-04-13T14:31:46+00:00` | `2026-04-13 09:31:46 (Lima)` | +11.17h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036985**
2. Descargar el PDF del acta
3. Verificar SHA-256: `b60fcdb4c05b8247e283cddd93a5949c12f5e1ab4209658390b011edc907ffe0`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
