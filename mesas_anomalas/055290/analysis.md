# Mesa 055290 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.686844+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE DE ACCION CONJUNTA PADRE ILUMINATO (código 3375)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 234
- Votos válidos: 202
- Participación: 78.261%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:22:41+00:00` | `2026-04-12 21:22:41 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:22:41+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:22:41+00:00` | `2026-04-12 21:22:41 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:41:36+00:00` | `2026-04-13 08:41:36 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:43:04+00:00` | `2026-04-13 08:43:04 (Lima)` |
| Última firma humana | `2026-04-13T13:43:17+00:00` | `2026-04-13 08:43:17 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.34 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:22:41 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:43:04 (Lima), es decir **11.34 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:21:24+00:00` | `2026-04-12 21:21:24 (Lima)` | -0.02h |
| 1 | ESTELA CUBAS orlando FIR 09584262 sw c3f3bc6999d450b97a4324db7b134f3cfa78b3e7 | 09584262 | `2026-04-13T13:43:04+00:00` | `2026-04-13 08:43:04 (Lima)` | +11.34h |
| 2 | ESPINOZA TORRES rori Jhander FIR 09586284 sw c7097aaf0bc421b1d2b24fed198cb9475bea6077 | 09586284 | `2026-04-13T13:43:17+00:00` | `2026-04-13 08:43:17 (Lima)` | +11.34h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055290**
2. Descargar el PDF del acta
3. Verificar SHA-256: `09aac3838a2bf0357aa53e9e39473b072ef2b2cd0e12534c32b057175b6c09b6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
