# Mesa 050019 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.801159+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: IE 1086 JESUS REDENTOR (código 3172)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 239
- Votos válidos: 231
- Participación: 79.933%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:48:56+00:00` | `2026-04-12 20:48:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:48:56+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:48:56+00:00` | `2026-04-12 20:48:56 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:34:06+00:00` | `2026-04-12 22:34:06 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:34:29+00:00` | `2026-04-12 22:34:29 (Lima)` |
| Última firma humana | `2026-04-13T03:34:39+00:00` | `2026-04-12 22:34:39 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.76 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:48:56 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:34:29 (Lima), es decir **1.76 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:48:54+00:00` | `2026-04-12 20:48:54 (Lima)` | -0.00h |
| 1 | CALERO TUESTA jaime Javier FIR 46606138 sw ace792a2945427be81ac38318e60b29a40ba33c3 | 46606138 | `2026-04-13T03:34:29+00:00` | `2026-04-12 22:34:29 (Lima)` | +1.76h |
| 2 | CASAVERDE LULLI lucia Patricia FIR 09279765 sw ed07dd000093b6e46ea09551dd643deed7d35078 | 09279765 | `2026-04-13T03:34:39+00:00` | `2026-04-12 22:34:39 (Lima)` | +1.76h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050019**
2. Descargar el PDF del acta
3. Verificar SHA-256: `927167ad1113717b0439e6245f61e42dc457e2bd2378446adac3885853df2798`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
