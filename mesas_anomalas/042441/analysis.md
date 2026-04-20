# Mesa 042441 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.519343+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: IEP INNOVA SCHOOLS - CHORRILLOS VILLA (código 54535)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 231
- Votos válidos: 200
- Participación: 77.258%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:46:39+00:00` | `2026-04-12 19:46:39 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:46:39+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:46:39+00:00` | `2026-04-12 19:46:39 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T01:03:07+00:00` | `2026-04-12 20:03:07 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T01:03:25+00:00` | `2026-04-12 20:03:25 (Lima)` |
| Última firma humana | `2026-04-13T01:04:07+00:00` | `2026-04-12 20:04:07 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.28 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:46:39 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 20:03:25 (Lima), es decir **0.28 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:46:38+00:00` | `2026-04-12 19:46:38 (Lima)` | -0.00h |
| 1 | HILARIO PINTO mariela Yessabel FIR 43868077 sw c968171f6185c3d1e1fba1ef3504ab7c59257fc0 | 43868077 | `2026-04-13T01:03:25+00:00` | `2026-04-12 20:03:25 (Lima)` | +0.28h |
| 2 | HUACARPUMA CASIMIRO edgar FIR 43599944 sw 6fbac9e3bf7d474075061b7e3aae55eb2d72cf0c | 43599944 | `2026-04-13T01:03:42+00:00` | `2026-04-12 20:03:42 (Lima)` | +0.28h |
| 3 | HUACCHA MESTANZA marleny FIR 48453838 sw 5c3683ca1cc29bacd245a239256cec7d45e8735d | 48453838 | `2026-04-13T01:04:07+00:00` | `2026-04-12 20:04:07 (Lima)` | +0.29h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042441**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2855be8262fed94ba1693b861c420b5c715acdfcac46e097de1f0d4e48e6635f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
