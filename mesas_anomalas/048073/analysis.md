# Mesa 048073 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.684430+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: BARRANCO
- **Local de votación**: IE 6051 MERCEDES INDACOCHEA (código 12821)
- **Ubigeo**: 140125

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 224
- Votos emitidos: 162
- Votos válidos: 152
- Participación: 72.321%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:45:13+00:00` | `2026-04-12 20:45:13 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:45:13+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:45:13+00:00` | `2026-04-12 20:45:13 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:56:29+00:00` | `2026-04-12 22:56:29 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:57:18+00:00` | `2026-04-12 22:57:18 (Lima)` |
| Última firma humana | `2026-04-13T03:57:54+00:00` | `2026-04-12 22:57:54 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.20 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:45:13 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:57:18 (Lima), es decir **2.20 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:45:11+00:00` | `2026-04-12 20:45:11 (Lima)` | -0.00h |
| 1 | ACEVEDO GARCIA maria De Los Angeles FIR 70923621 sw 044d527f89e2f6d7dd27cf29697a9c7e0cc30348 | 70923621 | `2026-04-13T03:57:18+00:00` | `2026-04-12 22:57:18 (Lima)` | +2.20h |
| 2 | ACOSTA VILLAVICENCIO katherine FIR 09729439 sw 42b17bbc492181b821cb91bb717a2e371229580b | 09729439 | `2026-04-13T03:57:41+00:00` | `2026-04-12 22:57:41 (Lima)` | +2.21h |
| 3 | AGUINAGA HEREDIA kelly Maribel FIR 48951430 sw 979b22f664ff8e234cc7a1ef4f90e14086a07ad6 | 48951430 | `2026-04-13T03:57:54+00:00` | `2026-04-12 22:57:54 (Lima)` | +2.21h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **048073**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e55d142641f925778ab02c089e13eb19e333575f97f04214393b3d2ddcdf1465`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
