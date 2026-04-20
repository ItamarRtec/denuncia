# Mesa 036165 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.092591+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE 1146 REPUBLICA DE PARAGUAY (código 2651)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 225
- Votos válidos: 197
- Participación: 75.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:33:34+00:00` | `2026-04-12 20:33:34 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:33:34+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:33:34+00:00` | `2026-04-12 20:33:34 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:09:01+00:00` | `2026-04-12 23:09:01 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:09:27+00:00` | `2026-04-12 23:09:27 (Lima)` |
| Última firma humana | `2026-04-13T04:10:00+00:00` | `2026-04-12 23:10:00 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.60 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:33:34 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:09:27 (Lima), es decir **2.60 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:33:32+00:00` | `2026-04-12 20:33:32 (Lima)` | -0.00h |
| 1 | BRAVO RODRIGUEZ ingrid Raquel FIR 10661915 sw 83d04821d983fef0931e431f6893a4504a14ed4f | 10661915 | `2026-04-13T04:09:27+00:00` | `2026-04-12 23:09:27 (Lima)` | +2.60h |
| 2 | CAMAYO APARCO brayan Augusto FIR 75142290 sw 85070d295f7de5b37f3debe8b6eaf8bd83461bd9 | 75142290 | `2026-04-13T04:09:47+00:00` | `2026-04-12 23:09:47 (Lima)` | +2.60h |
| 3 | CALERO RUIZ victor Manuel FIR 42942604 sw 18e7f75a85448f16f923232ab5c338c688f31eb1 | 42942604 | `2026-04-13T04:10:00+00:00` | `2026-04-12 23:10:00 (Lima)` | +2.61h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036165**
2. Descargar el PDF del acta
3. Verificar SHA-256: `395196f4d5ee027e07e9a62400b09deea0078bd89f4e7ea142f24d6ccb524b1f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
