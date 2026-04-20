# Mesa 046006 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.826621+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUEBLO LIBRE
- **Local de votación**: IE 04 NIÑO JESUS DE PRAGA (código 50932)
- **Ubigeo**: 140117

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 234
- Votos válidos: 215
- Participación: 78.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:13:07+00:00` | `2026-04-12 21:13:07 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:13:07+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:13:07+00:00` | `2026-04-12 21:13:07 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:28:30+00:00` | `2026-04-13 07:28:30 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:28:45+00:00` | `2026-04-13 07:28:45 (Lima)` |
| Última firma humana | `2026-04-13T12:29:17+00:00` | `2026-04-13 07:29:17 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.26 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:13:07 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:28:45 (Lima), es decir **10.26 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:13:05+00:00` | `2026-04-12 21:13:05 (Lima)` | -0.00h |
| 1 | DE LOS RIOS CASTRO jessica FIR 40416011 sw 89bf15fff28c70564280699cccc62bd680676240 | 40416011 | `2026-04-13T12:28:45+00:00` | `2026-04-13 07:28:45 (Lima)` | +10.26h |
| 2 | HUAQUISTO JULCA DE NAVARRO giovanna FIR 40160215 sw 842176229b801dd3a5c5f33a6b9285f7ce765c89 | 40160215 | `2026-04-13T12:29:17+00:00` | `2026-04-13 07:29:17 (Lima)` | +10.27h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046006**
2. Descargar el PDF del acta
3. Verificar SHA-256: `ef941f0710177f945bec8b31f1dbf18eeec14aae68f3908f1ff5ef87eb5363d7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
