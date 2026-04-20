# Mesa 082561 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.053646+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: BELLAVISTA
- **Local de votación**: IEP CALLAO (código 5081)
- **Ubigeo**: 240102

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 206
- Votos válidos: 175
- Participación: 68.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:42:57+00:00` | `2026-04-12 20:42:57 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:42:57+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:42:57+00:00` | `2026-04-12 20:42:57 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:06:21+00:00` | `2026-04-13 08:06:21 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:10:33+00:00` | `2026-04-13 08:10:33 (Lima)` |
| Última firma humana | `2026-04-13T13:16:00+00:00` | `2026-04-13 08:16:00 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.46 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:42:57 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:10:33 (Lima), es decir **11.46 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:42:55+00:00` | `2026-04-12 20:42:55 (Lima)` | -0.00h |
| 1 | MORAN CARHUATOCTO lourdes Elizabeth FIR 10628350 sw 45b3ae753b144c18d1331fcd22a9cf240057711d | 10628350 | `2026-04-13T13:10:33+00:00` | `2026-04-13 08:10:33 (Lima)` | +11.46h |
| 2 | MORALES SIPION tania Sharol FIR 09748825 sw 051ecf13923cff7bacdcedca1b22ad5957ae776c | 09748825 | `2026-04-13T13:13:12+00:00` | `2026-04-13 08:13:12 (Lima)` | +11.50h |
| 3 | MOLINA BENAVENTE banesa Elizabel FIR 43543354 sw e14a128ac4b4b3be7742d5a4129cd3f704bb7266 | 43543354 | `2026-04-13T13:16:00+00:00` | `2026-04-13 08:16:00 (Lima)` | +11.55h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082561**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4edd1798153228cc6f45cf717c1c9e5a01f6e70b36a698bb84ad0e175d825c0b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
