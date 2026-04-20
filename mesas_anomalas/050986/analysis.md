# Mesa 050986 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.766124+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: UNIVERSIDAD RICARDO PALMA (código 3221)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 298
- Votos emitidos: 215
- Votos válidos: 201
- Participación: 72.148%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:57:33+00:00` | `2026-04-12 21:57:33 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:57:33+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:57:33+00:00` | `2026-04-12 21:57:33 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:03:26+00:00` | `2026-04-13 00:03:26 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:03:59+00:00` | `2026-04-13 00:03:59 (Lima)` |
| Última firma humana | `2026-04-13T05:04:56+00:00` | `2026-04-13 00:04:56 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.11 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:57:33 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:03:59 (Lima), es decir **2.11 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:53:44+00:00` | `2026-04-12 21:53:44 (Lima)` | -0.06h |
| 1 | CORONEL DAVILA maria Ustebertha FIR 09548101 sw 3bb4f2c6219c1b9e1a8bab7015746e7a3e20b460 | 09548101 | `2026-04-13T05:03:59+00:00` | `2026-04-13 00:03:59 (Lima)` | +2.11h |
| 2 | CORNEJO VALENTIN gabriel Antonio FIR 70136990 sw 26c2f6ffc59c8d79855380cb8c0a4cd5092c0459 | 70136990 | `2026-04-13T05:04:17+00:00` | `2026-04-13 00:04:17 (Lima)` | +2.11h |
| 3 | CRUZ GIRON arian Paolo FIR 60939406 sw b2f8754007a3495e8aa9a14136452e85bc117ba7 | 60939406 | `2026-04-13T05:04:33+00:00` | `2026-04-13 00:04:33 (Lima)` | +2.12h |
| 4 | FLOREZ CHACCARA bethsy Virginia FIR 77058727 sw 03cf4189f803614d413c4a293fa4dd693f7f19b0 | 77058727 | `2026-04-13T05:04:56+00:00` | `2026-04-13 00:04:56 (Lima)` | +2.12h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050986**
2. Descargar el PDF del acta
3. Verificar SHA-256: `84bc7c765db69c7322a795d90b88dac52658290350b50d26d212f46b910a6ec2`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
