# Mesa 047921 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.161264+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN ISIDRO
- **Local de votación**: ESTACIONAMIENTO PETROPERU (código 54844)
- **Ubigeo**: 140124

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 190
- Votos válidos: 185
- Participación: 63.545%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:23:23+00:00` | `2026-04-12 21:23:23 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:23:23+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:23:23+00:00` | `2026-04-12 21:23:23 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:58:30+00:00` | `2026-04-13 07:58:30 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:12:16+00:00` | `2026-04-13 08:12:16 (Lima)` |
| Última firma humana | `2026-04-13T13:20:22+00:00` | `2026-04-13 08:20:22 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.81 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:23:23 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:12:16 (Lima), es decir **10.81 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:22:14+00:00` | `2026-04-12 21:22:14 (Lima)` | -0.02h |
| 1 | CUENTAS BARRIGA hjalmar FIR 29641317 sw a86197f27c8e5e8c65c0d715542adf8fd6461980 | 29641317 | `2026-04-13T13:12:16+00:00` | `2026-04-13 08:12:16 (Lima)` | +10.81h |
| 2 | DE LAS CASAS DENEGRI diego Mauricio FIR 44122464 sw 149f44a5a4ac77e640ab1881632e23cd33065357 | 44122464 | `2026-04-13T13:18:25+00:00` | `2026-04-13 08:18:25 (Lima)` | +10.92h |
| 3 | DE AUBEYZON GARGUREVICH martin Jose FIR 43308506 sw f79b544607bd5b883a70f007fa33397151c06654 | 43308506 | `2026-04-13T13:20:22+00:00` | `2026-04-13 08:20:22 (Lima)` | +10.95h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **047921**
2. Descargar el PDF del acta
3. Verificar SHA-256: `11c82169ab64b75a44ce822c8fadb240b1b06df84004fc0e5fba8dad9aec852b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
