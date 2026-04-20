# Mesa 050546 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.269611+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: COLEGIO CHAMPAGNAT (código 3195)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 217
- Votos válidos: 205
- Participación: 72.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:57:59+00:00` | `2026-04-12 20:57:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:57:59+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:57:59+00:00` | `2026-04-12 20:57:59 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:06:00+00:00` | `2026-04-13 08:06:00 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:06:30+00:00` | `2026-04-13 08:06:30 (Lima)` |
| Última firma humana | `2026-04-13T13:18:59+00:00` | `2026-04-13 08:18:59 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.14 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:57:59 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:06:30 (Lima), es decir **11.14 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:57:56+00:00` | `2026-04-12 20:57:56 (Lima)` | -0.00h |
| 1 | MONTENEGRO CARDENAS mercedes Felicia FIR 08091766 sw 57717886ff8880638255ddda0ac08a16f3ece0c1 | 08091766 | `2026-04-13T13:06:30+00:00` | `2026-04-13 08:06:30 (Lima)` | +11.14h |
| 2 | MIRANDA MENDOZA betty Victoria FIR 10308330 sw f633f18b10720476fe94fc9a4e5cdf34888df74f | 10308330 | `2026-04-13T13:06:49+00:00` | `2026-04-13 08:06:49 (Lima)` | +11.15h |
| 3 | MORALES FLORES marcelo Santiago FIR 72970445 sw a73d72567250d31767c6d8edf239a28804808c19 | 72970445 | `2026-04-13T13:16:29+00:00` | `2026-04-13 08:16:29 (Lima)` | +11.31h |
| 4 | MOSCOL HIDALGO yuliana Margarita FIR 45266404 sw 512787f39509e4df7349d0e7816bfe1e462adcaf | 45266404 | `2026-04-13T13:18:59+00:00` | `2026-04-13 08:18:59 (Lima)` | +11.35h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050546**
2. Descargar el PDF del acta
3. Verificar SHA-256: `ce5e618628f016ff2af27ec67945aaaf56033e30995404122207809c3c383a68`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
