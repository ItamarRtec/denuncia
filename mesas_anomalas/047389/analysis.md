# Mesa 047389 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.448107+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: RÍMAC
- **Local de votación**: UNIVERSIDAD NACIONAL DE INGENIERIA (código 3068)
- **Ubigeo**: 140122

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 209
- Votos válidos: 180
- Participación: 69.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:32:20+00:00` | `2026-04-12 20:32:20 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:32:20+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:32:20+00:00` | `2026-04-12 20:32:20 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:10:30+00:00` | `2026-04-12 21:10:30 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:11:20+00:00` | `2026-04-12 21:11:20 (Lima)` |
| Última firma humana | `2026-04-13T02:13:03+00:00` | `2026-04-12 21:13:03 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.65 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:32:20 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:11:20 (Lima), es decir **0.65 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:32:17+00:00` | `2026-04-12 20:32:17 (Lima)` | -0.00h |
| 1 | ARRIETA SALAS manuel Jesus FIR 71427247 sw ce23a4f146725dc48b3eb8bf2cf73d43d91566f4 | 71427247 | `2026-04-13T02:11:20+00:00` | `2026-04-12 21:11:20 (Lima)` | +0.65h |
| 2 | ARIAS VIGILIO percy David FIR 80116171 sw cb169887f8c43a4642cb10c6c0a1fce641134901 | 80116171 | `2026-04-13T02:11:46+00:00` | `2026-04-12 21:11:46 (Lima)` | +0.66h |
| 3 | ASTETE CORDOVA mario FIR 08155959 sw 447668b430acca986dcb7913b41c66e0a47067df | 08155959 | `2026-04-13T02:12:03+00:00` | `2026-04-12 21:12:03 (Lima)` | +0.66h |
| 4 | HUANCA PAASACA nancy Veronica FIR 44946596 sw 4eadeb8d6d192215232e97a6fe4d3cae0270e551 | 44946596 | `2026-04-13T02:12:40+00:00` | `2026-04-12 21:12:40 (Lima)` | +0.67h |
| 5 | CANALES FLORES DE BRETONECHE nadia Elizabeth FIR 08172402 sw aa64f088c98e1bd307f31bc05cc237a288079b40 | 08172402 | `2026-04-13T02:13:03+00:00` | `2026-04-12 21:13:03 (Lima)` | +0.68h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **047389**
2. Descargar el PDF del acta
3. Verificar SHA-256: `68b8403bdb87dcfad2010c029013de4f816c99c109097377250f76e857c0ddfe`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
