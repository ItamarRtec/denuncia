# Mesa 036889 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.042305+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IEP SACO OLIVEROS - CIPRESES ELIO (código 52460)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 226
- Votos válidos: 203
- Participación: 75.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T04:59:48+00:00` | `2026-04-12 23:59:48 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T04:59:48+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T04:59:48+00:00` | `2026-04-12 23:59:48 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:35:29+00:00` | `2026-04-13 07:35:29 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:35:48+00:00` | `2026-04-13 07:35:48 (Lima)` |
| Última firma humana | `2026-04-13T12:36:47+00:00` | `2026-04-13 07:36:47 (Lima)` |

**Brecha primera firma humana vs publicación:** **+7.60 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 23:59:48 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:35:48 (Lima), es decir **7.60 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T04:59:47+00:00` | `2026-04-12 23:59:47 (Lima)` | -0.00h |
| 1 | CANTORAL AMAU fabrizio Rafael FIR 71466671 sw cfc583dea29cfce0925edd02908a6a18cf8900ff | 71466671 | `2026-04-13T12:35:48+00:00` | `2026-04-13 07:35:48 (Lima)` | +7.60h |
| 2 | CASTRO ACUNA jean Pierre FIR 71732886 sw a2ba9767036a70663cd0e5e748738cc142bea0b1 | 71732886 | `2026-04-13T12:36:12+00:00` | `2026-04-13 07:36:12 (Lima)` | +7.61h |
| 3 | CASTILLO VARGAS julissa Jannet FIR 09957591 sw 1c8c5949d057eeb6140351d1c95a61d30f51c1d3 | 09957591 | `2026-04-13T12:36:47+00:00` | `2026-04-13 07:36:47 (Lima)` | +7.62h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036889**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3edc03920e7181b3a6a75d3835a3bacc79661f49b510de1879149a345789288f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
