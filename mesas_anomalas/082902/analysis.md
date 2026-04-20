# Mesa 082902 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.128985+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: LA PERLA
- **Local de votación**: IE JOSE OLAYA BALANDRA (código 4853)
- **Ubigeo**: 240105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 256
- Votos emitidos: 189
- Votos válidos: 163
- Participación: 73.828%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:00:31+00:00` | `2026-04-12 20:00:31 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:00:31+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:00:31+00:00` | `2026-04-12 20:00:31 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:28:54+00:00` | `2026-04-12 22:28:54 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:29:10+00:00` | `2026-04-12 22:29:10 (Lima)` |
| Última firma humana | `2026-04-13T03:29:41+00:00` | `2026-04-12 22:29:41 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.48 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:00:31 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:29:10 (Lima), es decir **2.48 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:00:29+00:00` | `2026-04-12 20:00:29 (Lima)` | -0.00h |
| 1 | ARTEAGA AGUIRRE nicol Darlyn FIR 75152360 sw b1b9a671e249cf3f14b909bbd324a4afac9c54b6 | 75152360 | `2026-04-13T03:29:10+00:00` | `2026-04-12 22:29:10 (Lima)` | +2.48h |
| 2 | ANDRADE POLAR johvany Narciso FIR 25660990 sw cb424b91514fb3863eab28423f89b9195262256f | 25660990 | `2026-04-13T03:29:32+00:00` | `2026-04-12 22:29:32 (Lima)` | +2.48h |
| 3 | ALBURQUEQUE LADINES raul Humberto FIR 25704808 sw 6e8e20e8c1e389ab33678ebad93db3ea1d6b5242 | 25704808 | `2026-04-13T03:29:41+00:00` | `2026-04-12 22:29:41 (Lima)` | +2.49h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082902**
2. Descargar el PDF del acta
3. Verificar SHA-256: `11dca254b0920836fa68c29b779ee842c078a768edb97eea4eda00a59e8779bc`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
