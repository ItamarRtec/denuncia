# Mesa 036295 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.917917+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE EMBLEMATICA HIPOLITO UNANUE (código 2659)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 229
- Votos válidos: 198
- Participación: 76.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:34:31+00:00` | `2026-04-12 21:34:31 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:29:59+00:00` | `2026-04-12 21:29:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:34:31+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:34:31+00:00` | `2026-04-12 21:34:31 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:19:53+00:00` | `2026-04-13 08:19:53 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:20:25+00:00` | `2026-04-13 08:20:25 (Lima)` |
| Última firma humana | `2026-04-13T13:21:13+00:00` | `2026-04-13 08:21:13 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.77 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:34:31 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:20:25 (Lima), es decir **10.77 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:29:50+00:00` | `2026-04-12 21:29:50 (Lima)` | -0.08h |
| 1 | UZURIAGA ESPINEL jorge Luis FIR 40390402 sw 3626b36bb955fe33b30d0f98d5e82159ba07cf48 | 40390402 | `2026-04-13T13:20:25+00:00` | `2026-04-13 08:20:25 (Lima)` | +10.77h |
| 2 | UBIDIA RODRIGUEZ martin Alfonso FIR 10427034 sw 80dbca9c84205bf3da709ad2e9d3d8839e7e5859 | 10427034 | `2026-04-13T13:20:47+00:00` | `2026-04-13 08:20:47 (Lima)` | +10.77h |
| 3 | VALCARCEL LOZANO valeria Sofia FIR 76599311 sw cb687ddafaa7aca8dcd5c0833060e6ae79e60894 | 76599311 | `2026-04-13T13:21:13+00:00` | `2026-04-13 08:21:13 (Lima)` | +10.78h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036295**
2. Descargar el PDF del acta
3. Verificar SHA-256: `72e23de743683e8c8019b447bb280d146afd077885cbc70524147b2c9c085cb2`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
