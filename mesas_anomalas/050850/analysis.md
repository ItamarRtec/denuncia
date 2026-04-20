# Mesa 050850 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.444502+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IEP COLEGIO MIXTO SANTA TERESITA (código 3213)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 249
- Votos válidos: 241
- Participación: 83.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:14:07+00:00` | `2026-04-12 20:14:07 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:14:07+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:14:07+00:00` | `2026-04-12 20:14:07 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:28:12+00:00` | `2026-04-12 22:28:12 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:29:32+00:00` | `2026-04-12 22:29:32 (Lima)` |
| Última firma humana | `2026-04-13T03:29:58+00:00` | `2026-04-12 22:29:58 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.26 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:14:07 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:29:32 (Lima), es decir **2.26 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:14:05+00:00` | `2026-04-12 20:14:05 (Lima)` | -0.00h |
| 1 | ARBURUA SALGADO orieta Rosario FIR 08626956 sw 0ba7a3dffdd76e3c3e578c601be771eeb6e4c616 | 08626956 | `2026-04-13T03:29:32+00:00` | `2026-04-12 22:29:32 (Lima)` | +2.26h |
| 2 | ARANA MORALES ellioth Damian FIR 44815147 sw 49d7f64eea392df2734045ced4a1b3660c839591 | 44815147 | `2026-04-13T03:29:46+00:00` | `2026-04-12 22:29:46 (Lima)` | +2.26h |
| 3 | ARANDA GIRALDO juan Carlos FIR 08834083 sw 65a6b9ed247edd4a8bef98d112487c52605d6b43 | 08834083 | `2026-04-13T03:29:58+00:00` | `2026-04-12 22:29:58 (Lima)` | +2.26h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050850**
2. Descargar el PDF del acta
3. Verificar SHA-256: `31f1138d83656d6319841aa5499531d5b1ad7fa1bf2126e2453b1d5330f4c289`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
