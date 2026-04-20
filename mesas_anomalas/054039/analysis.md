# Mesa 054039 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.488984+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: INDEPENDENCIA
- **Local de votación**: IE 3056 GRAN BRETAÑA (código 13120)
- **Ubigeo**: 140134

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 252
- Votos válidos: 223
- Participación: 84.281%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:14:08+00:00` | `2026-04-12 21:14:08 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:14:08+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:14:08+00:00` | `2026-04-12 21:14:08 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:59:21+00:00` | `2026-04-12 23:59:21 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:03:21+00:00` | `2026-04-13 00:03:21 (Lima)` |
| Última firma humana | `2026-04-13T05:04:46+00:00` | `2026-04-13 00:04:46 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.82 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:14:08 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:03:21 (Lima), es decir **2.82 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:14:04+00:00` | `2026-04-12 21:14:04 (Lima)` | -0.00h |
| 1 | BENAVIDES AMPUERO christian Paul FIR 07536101 sw f47aaca2fbe23490fc15a6e8e6ceebfadba7921e | 07536101 | `2026-04-13T05:03:21+00:00` | `2026-04-13 00:03:21 (Lima)` | +2.82h |
| 2 | CARBAJAL CRISOSTOMO cirila FIR 09521396 sw 0bb196487f9a26e02ce7bf62ca9f5f8e3d5044ac | 09521396 | `2026-04-13T05:04:32+00:00` | `2026-04-13 00:04:32 (Lima)` | +2.84h |
| 3 | CAPILLO HANCCO jorge Armando FIR 43309311 sw 4fb89fade1960e4cf329becc19fe79b7fbbac864 | 43309311 | `2026-04-13T05:04:46+00:00` | `2026-04-13 00:04:46 (Lima)` | +2.84h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054039**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e19bc073578298a9b6f09c6f439606a8c77691e70b732f1bda291e0f2cce09c1`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
