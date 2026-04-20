# Mesa 051693 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.908266+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: CEBE ESPECIAL SURQUILLO (código 3224)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 260
- Votos válidos: 250
- Participación: 86.957%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:40:54+00:00` | `2026-04-12 20:40:54 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:40:54+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:40:54+00:00` | `2026-04-12 20:40:54 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:25:37+00:00` | `2026-04-13 08:25:37 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:26:28+00:00` | `2026-04-13 08:26:28 (Lima)` |
| Última firma humana | `2026-04-13T13:27:57+00:00` | `2026-04-13 08:27:57 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.76 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:40:54 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:26:28 (Lima), es decir **11.76 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:40:52+00:00` | `2026-04-12 20:40:52 (Lima)` | -0.00h |
| 1 | VASQUEZ VALDEIGLESIAS facundo Alejandro FIR 70743532 sw d37f62481f52769a4796dfe225a67406a665e094 | 70743532 | `2026-04-13T13:26:28+00:00` | `2026-04-13 08:26:28 (Lima)` | +11.76h |
| 2 | TREVEJO MENDEZ amelia Mariela FIR 09303821 sw b44937e2af47f20a52e6f9393b3304d2c5c13c12 | 09303821 | `2026-04-13T13:26:39+00:00` | `2026-04-13 08:26:39 (Lima)` | +11.76h |
| 3 | ULLOA MARTINEZ dafne Carmen FIR 40098226 sw 046d41a89be3de85a0d1826a1603e833794805b2 | 40098226 | `2026-04-13T13:26:49+00:00` | `2026-04-13 08:26:49 (Lima)` | +11.77h |
| 4 | TAPULLIMA SANANCINA luis Miguel FIR 76196297 sw 6e5549d737ae79b701627b3808eeb1a95a500018 | 76196297 | `2026-04-13T13:27:57+00:00` | `2026-04-13 08:27:57 (Lima)` | +11.78h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051693**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2a58bd0f9aed41d5d382db31b9da999aaedaba0ddb2bed799bf0de5143e31972`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
