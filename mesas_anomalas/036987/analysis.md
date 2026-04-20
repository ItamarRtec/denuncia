# Mesa 036987 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.484425+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IEP INNOVA SCHOOLS BERTELLO (código 54803)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 215
- Votos válidos: 198
- Participación: 71.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:13:56+00:00` | `2026-04-12 22:13:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:13:56+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:13:56+00:00` | `2026-04-12 22:13:56 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:07:11+00:00` | `2026-04-13 08:07:11 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:07:47+00:00` | `2026-04-13 08:07:47 (Lima)` |
| Última firma humana | `2026-04-13T13:08:44+00:00` | `2026-04-13 08:08:44 (Lima)` |

**Brecha primera firma humana vs publicación:** **+9.90 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:13:56 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:07:47 (Lima), es decir **9.90 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:13:54+00:00` | `2026-04-12 22:13:54 (Lima)` | -0.00h |
| 1 | OLIDEN TORRES beatriz Margarita FIR 09452201 sw 2ca62024bb9882f8760fa0a14ddf82ba30035763 | 09452201 | `2026-04-13T13:07:47+00:00` | `2026-04-13 08:07:47 (Lima)` | +9.90h |
| 2 | OLIVEROS ESPINOZA zaida Mirela FIR 07969316 sw 3ff076656be83ecd195ec299bb2454d3b1120ab4 | 07969316 | `2026-04-13T13:08:21+00:00` | `2026-04-13 08:08:21 (Lima)` | +9.91h |
| 3 | MUERAS GOMEZ wilmer David FIR 72440747 sw aa5e993e9c3d652938dde3f11b5bb0a9374aa972 | 72440747 | `2026-04-13T13:08:44+00:00` | `2026-04-13 08:08:44 (Lima)` | +9.91h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036987**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4a18728a3368198d15f166fe905c0cbc332844f37b2d181b716f86fbc74c0e21`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
