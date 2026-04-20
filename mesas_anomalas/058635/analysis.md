# Mesa 058635 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.968528+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IEP INNOVA SCHOOLS SJL ARABISCOS (código 54810)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 267
- Votos válidos: 244
- Participación: 89.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:18:56+00:00` | `2026-04-12 21:18:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:18:56+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:18:56+00:00` | `2026-04-12 21:18:56 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:25:12+00:00` | `2026-04-13 08:25:12 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:25:46+00:00` | `2026-04-13 08:25:46 (Lima)` |
| Última firma humana | `2026-04-13T13:25:46+00:00` | `2026-04-13 08:25:46 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.11 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:18:56 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:25:46 (Lima), es decir **11.11 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:17:39+00:00` | `2026-04-12 21:17:39 (Lima)` | -0.02h |
| 1 | MUNDACA FELIX mirko Mauricio FIR 77164276 sw d3bffe7a312874f9390c8d099cdb74a4d10eaef7 | 77164276 | `2026-04-13T13:25:46+00:00` | `2026-04-13 08:25:46 (Lima)` | +11.11h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **058635**
2. Descargar el PDF del acta
3. Verificar SHA-256: `f101049ca416ddedc39a0c3d217e68eff852f04fa7f6e281efa723f0724ddbfb`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **1** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
