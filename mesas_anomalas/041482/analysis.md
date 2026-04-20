# Mesa 041482 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.147809+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IEP INNOVA SCHOOLS SEDE RETABLO (código 54815)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 211
- Votos válidos: 184
- Participación: 70.569%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:04:02+00:00` | `2026-04-12 20:04:02 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:04:02+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:04:02+00:00` | `2026-04-12 20:04:02 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:32:35+00:00` | `2026-04-12 21:32:35 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:33:07+00:00` | `2026-04-12 21:33:07 (Lima)` |
| Última firma humana | `2026-04-13T02:33:51+00:00` | `2026-04-12 21:33:51 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.48 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:04:02 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:33:07 (Lima), es decir **1.48 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:04:00+00:00` | `2026-04-12 20:04:00 (Lima)` | -0.00h |
| 1 | TUPAYACHI YLLA nelly Milagros FIR 76324545 sw 41cc6c20364bf1f4ebe56eb33cc368890c556256 | 76324545 | `2026-04-13T02:33:07+00:00` | `2026-04-12 21:33:07 (Lima)` | +1.48h |
| 2 | TAPIA PEREZ walter Luis FIR 46892044 sw 19877f73cf6487ec495e6d4418db8f8dcc13345b | 46892044 | `2026-04-13T02:33:31+00:00` | `2026-04-12 21:33:31 (Lima)` | +1.49h |
| 3 | TELLO MORI deiby Jefferson FIR 72889644 sw 39e1c7ff18c0f5e4f0d68ee48c452da3a0229fa1 | 72889644 | `2026-04-13T02:33:51+00:00` | `2026-04-12 21:33:51 (Lima)` | +1.50h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041482**
2. Descargar el PDF del acta
3. Verificar SHA-256: `0833ea74214f89d420d4c0b7848d289d53196d6c71aa2f2547cbeb315713cc5c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
