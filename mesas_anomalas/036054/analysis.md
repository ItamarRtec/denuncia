# Mesa 036054 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.837060+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE 0035 NUESTRA SEÑORA DE LA VISITACION (código 2640)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 250
- Votos válidos: 221
- Participación: 83.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:32:29+00:00` | `2026-04-12 20:32:29 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:32:29+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:32:29+00:00` | `2026-04-12 20:32:29 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:39:07+00:00` | `2026-04-13 07:39:07 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:39:50+00:00` | `2026-04-13 07:39:50 (Lima)` |
| Última firma humana | `2026-04-13T12:40:28+00:00` | `2026-04-13 07:40:28 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.12 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:32:29 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:39:50 (Lima), es decir **11.12 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:32:26+00:00` | `2026-04-12 20:32:26 (Lima)` | -0.00h |
| 1 | SILVA MEDRANO dayana Estefany FIR 61252616 sw 428a90531f07de682d28d18217d1fb515fdcc9ea | 61252616 | `2026-04-13T12:39:50+00:00` | `2026-04-13 07:39:50 (Lima)` | +11.12h |
| 2 | SOTOMAYOR MONTOYA german FIR 15365410 sw 1b1f11f4f188560c461f622dd21d9260f142b2c3 | 15365410 | `2026-04-13T12:40:06+00:00` | `2026-04-13 07:40:06 (Lima)` | +11.13h |
| 3 | TAFUR VASQUEZ jessica Maria FIR 46824419 sw de15d6b2eeee65b528dedb8042c15a5565d45d7b | 46824419 | `2026-04-13T12:40:28+00:00` | `2026-04-13 07:40:28 (Lima)` | +11.13h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036054**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8919c827f80c1feb593f4de02c98bfcbffcf3365c405349e2fb3afe8f222262c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
