# Mesa 045013 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.249279+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: CEBE 4 MIRAFLORES (código 2979)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 224
- Votos válidos: 214
- Participación: 74.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:07:47+00:00` | `2026-04-12 21:07:47 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:07:47+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:07:47+00:00` | `2026-04-12 21:07:47 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:11:46+00:00` | `2026-04-12 23:11:46 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:12:42+00:00` | `2026-04-12 23:12:42 (Lima)` |
| Última firma humana | `2026-04-13T04:13:27+00:00` | `2026-04-12 23:13:27 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.08 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:07:47 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:12:42 (Lima), es decir **2.08 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:07:45+00:00` | `2026-04-12 21:07:45 (Lima)` | -0.00h |
| 1 | BORLETTI DEL SOLAR ezio FIR 46800205 sw 9b8081082c9b5906bfe862353b908356a2d59d1f | 46800205 | `2026-04-13T04:12:42+00:00` | `2026-04-12 23:12:42 (Lima)` | +2.08h |
| 2 | BYRNE MANSILLA carlos Dante FIR 07803350 sw aaa69163c6e7dbb6a19114b9226f13676be64633 | 07803350 | `2026-04-13T04:13:01+00:00` | `2026-04-12 23:13:01 (Lima)` | +2.09h |
| 3 | DIAZ MEDINA paola Elizabeth FIR 43213897 sw a7962aae61990c6b35b1445cd23c8be403702db1 | 43213897 | `2026-04-13T04:13:27+00:00` | `2026-04-12 23:13:27 (Lima)` | +2.09h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045013**
2. Descargar el PDF del acta
3. Verificar SHA-256: `a78ef57f0980a42beed7f5e7081d2911f3b6b7fe487bfa20262c78b2ec36736c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
