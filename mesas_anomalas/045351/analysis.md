# Mesa 045351 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.781237+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: UNIVERSIDAD NACIONAL FEDERICO VILLARREAL SEDE LOCAL 05 (código 54289)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 279
- Votos válidos: 272
- Participación: 93.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:51:36+00:00` | `2026-04-12 19:51:36 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:51:36+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:51:36+00:00` | `2026-04-12 19:51:36 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:08:18+00:00` | `2026-04-12 21:08:18 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:08:40+00:00` | `2026-04-12 21:08:40 (Lima)` |
| Última firma humana | `2026-04-13T02:09:31+00:00` | `2026-04-12 21:09:31 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.28 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:51:36 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:08:40 (Lima), es decir **1.28 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:51:34+00:00` | `2026-04-12 19:51:34 (Lima)` | -0.00h |
| 1 | PINEDA ARBULU maria Del Pilar Lydia FIR 25717076 sw 24e6a5c2a429766821a684f5bc16281e17caffd1 | 25717076 | `2026-04-13T02:08:40+00:00` | `2026-04-12 21:08:40 (Lima)` | +1.28h |
| 2 | RIVEROS TEJADA alain Gonzalo FIR 41535976 sw a9ee29d448257ee769356bf13a8636693529f340 | 41535976 | `2026-04-13T02:08:57+00:00` | `2026-04-12 21:08:57 (Lima)` | +1.29h |
| 3 | SANCHEZ ALVAREZ melissa FIR 42165242 sw a36aa1c03ff5327d54c6af4ccd3e734d3e6bfd0b | 42165242 | `2026-04-13T02:09:09+00:00` | `2026-04-12 21:09:09 (Lima)` | +1.29h |
| 4 | CAIRO URBINA rosa Sarahi FIR 71693457 sw 5c86c1e910d31014f2c9135182fee4b53305df62 | 71693457 | `2026-04-13T02:09:31+00:00` | `2026-04-12 21:09:31 (Lima)` | +1.30h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045351**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c7add2acd86941fed0532a6ff10c0bfb2fde925f5afb2397767a0d5ed3995172`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
