# Mesa 055881 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.700818+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 7070 DRA MARIA REICHE GROSSE NEUMAN (código 53231)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 241
- Votos válidos: 209
- Participación: 80.602%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:59:30+00:00` | `2026-04-12 21:59:30 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:59:30+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:59:30+00:00` | `2026-04-12 21:59:30 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:02:19+00:00` | `2026-04-13 08:02:19 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:02:44+00:00` | `2026-04-13 08:02:44 (Lima)` |
| Última firma humana | `2026-04-13T13:03:07+00:00` | `2026-04-13 08:03:07 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.05 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:59:30 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:02:44 (Lima), es decir **10.05 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:58:08+00:00` | `2026-04-12 21:58:08 (Lima)` | -0.02h |
| 1 | ARRATEA LIBERATO luz Nallely FIR 71077019 sw a2a491496c092bc52d5b3f1f72fa1be2975767c6 | 71077019 | `2026-04-13T13:02:44+00:00` | `2026-04-13 08:02:44 (Lima)` | +10.05h |
| 2 | ANDIA CORIHUAMAN william FIR 48126121 sw 72594027bcaa9474f639d111f984cdc2c552091b | 48126121 | `2026-04-13T13:02:56+00:00` | `2026-04-13 08:02:56 (Lima)` | +10.06h |
| 3 | BARANDIARAN VILLAVERDE karla Pierina FIR 47511935 sw fd703843cc232aa9c833bfd67e3222f0a2b24fee | 47511935 | `2026-04-13T13:03:07+00:00` | `2026-04-13 08:03:07 (Lima)` | +10.06h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055881**
2. Descargar el PDF del acta
3. Verificar SHA-256: `9848bd9c37da9640a5fc980ff21b66c86b24567eef75e106274ddd4193c6d07e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
