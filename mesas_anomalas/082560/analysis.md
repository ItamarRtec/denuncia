# Mesa 082560 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.895865+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: BELLAVISTA
- **Local de votación**: IEP CALLAO (código 5081)
- **Ubigeo**: 240102

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 221
- Votos válidos: 184
- Participación: 73.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:41:07+00:00` | `2026-04-12 20:41:07 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:41:07+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:41:07+00:00` | `2026-04-12 20:41:07 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:19:25+00:00` | `2026-04-13 08:19:25 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:19:54+00:00` | `2026-04-13 08:19:54 (Lima)` |
| Última firma humana | `2026-04-13T13:21:20+00:00` | `2026-04-13 08:21:20 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.65 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:41:07 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:19:54 (Lima), es decir **11.65 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:41:05+00:00` | `2026-04-12 20:41:05 (Lima)` | -0.00h |
| 1 | MATTOS VALLADARES miguel Angel FIR 25610316 sw 99f1b66cafc9b598e2805cf77ebfe1a6db535746 | 25610316 | `2026-04-13T13:19:54+00:00` | `2026-04-13 08:19:54 (Lima)` | +11.65h |
| 2 | MANRIQUE FLORES jorge Rodrigo FIR 72949525 sw a8288be866cb41dc0fb084a2d7b8973ed9030280 | 72949525 | `2026-04-13T13:20:08+00:00` | `2026-04-13 08:20:08 (Lima)` | +11.65h |
| 3 | MALPARTIDA ARANGO brian David FIR 72266539 sw 46f04383020fd0848e156812c0e516406a8e2548 | 72266539 | `2026-04-13T13:20:23+00:00` | `2026-04-13 08:20:23 (Lima)` | +11.65h |
| 4 | ESPINOZA PAZOS xiomi Yuliana FIR 75346806 sw ee9fedd7ad328fc27800a96b143ea06878cdc26f | 75346806 | `2026-04-13T13:21:20+00:00` | `2026-04-13 08:21:20 (Lima)` | +11.67h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082560**
2. Descargar el PDF del acta
3. Verificar SHA-256: `853759d798ae34ca77f2e88bb523f42ba3325edc29652cc4c7c1707a9ee4703e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
