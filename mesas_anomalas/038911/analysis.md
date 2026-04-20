# Mesa 038911 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.949520+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: BREÑA
- **Local de votación**: IE EMBLEMATICA MARIANO MELGAR (código 2752)
- **Ubigeo**: 140104

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 251
- Votos válidos: 225
- Participación: 83.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:52:36+00:00` | `2026-04-12 20:52:36 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:52:36+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:52:36+00:00` | `2026-04-12 20:52:36 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:17:32+00:00` | `2026-04-13 08:17:32 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:18:09+00:00` | `2026-04-13 08:18:09 (Lima)` |
| Última firma humana | `2026-04-13T13:18:38+00:00` | `2026-04-13 08:18:38 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.43 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:52:36 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:18:09 (Lima), es decir **11.43 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:52:34+00:00` | `2026-04-12 20:52:34 (Lima)` | -0.00h |
| 1 | OLIVARES ROJAS roberto Carlos FIR 44892645 sw 77a7c6b422b8815b44586946d72671a161184bb7 | 44892645 | `2026-04-13T13:18:09+00:00` | `2026-04-13 08:18:09 (Lima)` | +11.43h |
| 2 | NAVARRO CUETO cesar Jesus FIR 06686234 sw 2ed7a920eddd8502cd7f3af8d93af47dcd64e996 | 06686234 | `2026-04-13T13:18:27+00:00` | `2026-04-13 08:18:27 (Lima)` | +11.43h |
| 3 | OLIVAS VERGARA maria Guadalupe FIR 44890129 sw 452b42eb615b56c63ae9e8e24221cea7a563d415 | 44890129 | `2026-04-13T13:18:38+00:00` | `2026-04-13 08:18:38 (Lima)` | +11.43h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **038911**
2. Descargar el PDF del acta
3. Verificar SHA-256: `220615b32fd5679b3b12622393bf063dc43df06500b29d9c5943e34d3c0ad2f2`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
