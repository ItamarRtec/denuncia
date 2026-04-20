# Mesa 053237 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.665962+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IEP MIGUEL GRAU INICIAL (código 52072)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 221
- Votos válidos: 184
- Participación: 73.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:53:47+00:00` | `2026-04-12 20:53:47 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:53:47+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:53:47+00:00` | `2026-04-12 20:53:47 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:41:08+00:00` | `2026-04-12 23:41:08 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:41:38+00:00` | `2026-04-12 23:41:38 (Lima)` |
| Última firma humana | `2026-04-13T04:42:21+00:00` | `2026-04-12 23:42:21 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.80 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:53:47 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:41:38 (Lima), es decir **2.80 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:53:45+00:00` | `2026-04-12 20:53:45 (Lima)` | -0.00h |
| 1 | LACHUMA TUESTA cesar Luis FIR 05377290 sw ca192c17c481a9224ba485a809a0f128bfb1a405 | 05377290 | `2026-04-13T04:41:38+00:00` | `2026-04-12 23:41:38 (Lima)` | +2.80h |
| 2 | MENDOZA RIVERA mathias Humberto FIR 76009952 sw e36dbdc47da13a93a0e8c13f3293ba74832d7157 | 76009952 | `2026-04-13T04:42:02+00:00` | `2026-04-12 23:42:02 (Lima)` | +2.80h |
| 3 | MIRANDA RODRIGUEZ roxana Salome FIR 10075143 sw 0b4728b594ffb597b19dea30709721045773b338 | 10075143 | `2026-04-13T04:42:21+00:00` | `2026-04-12 23:42:21 (Lima)` | +2.81h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **053237**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4fdd0517909f2bf1421fa3e435dc3b7e31a36c91ae1c74dfbedf5f63f81c19e6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
