# Mesa 045066 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.035229+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: COLEGIO ADVENTISTA MIRAFLORES (código 2984)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 225
- Votos válidos: 209
- Participación: 75.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:05:06+00:00` | `2026-04-12 21:05:06 (Lima)` |
| `C` | Contabilizada | `2026-04-13T01:40:21+00:00` | `2026-04-12 20:40:21 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:05:06+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:05:06+00:00` | `2026-04-12 21:05:06 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:05:49+00:00` | `2026-04-12 23:05:49 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:06:25+00:00` | `2026-04-12 23:06:25 (Lima)` |
| Última firma humana | `2026-04-13T04:09:05+00:00` | `2026-04-12 23:09:05 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.02 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:05:06 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:06:25 (Lima), es decir **2.02 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:40:19+00:00` | `2026-04-12 20:40:19 (Lima)` | -0.41h |
| 1 | DEL ROSARIO ALIAGA lorena Elizabeth FIR 10278643 sw a10c5f49178fa036ccef60862750ea07b26de687 | 10278643 | `2026-04-13T04:06:25+00:00` | `2026-04-12 23:06:25 (Lima)` | +2.02h |
| 2 | D'ARRIGO MACAVILCA victor Guillermo FIR 25699596 sw 5eb37fe1c00b01eef058f10c795f6052b3c510e1 | 25699596 | `2026-04-13T04:06:57+00:00` | `2026-04-12 23:06:57 (Lima)` | +2.03h |
| 3 | FERNANDEZ HUERTA aracelli FIR 07823996 sw a5ff7ef5d4dd96ede2f707b658af35cf9449773f | 07823996 | `2026-04-13T04:07:22+00:00` | `2026-04-12 23:07:22 (Lima)` | +2.04h |
| 4 | SOTELO VASQUEZ marco Antonio Francisco FIR 43351252 sw 0eaf480023b3a8df8b0521a0cd1023b9e1d069c6 | 43351252 | `2026-04-13T04:09:05+00:00` | `2026-04-12 23:09:05 (Lima)` | +2.07h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045066**
2. Descargar el PDF del acta
3. Verificar SHA-256: `03560538d34cab0e907aedd413f0ee6630c4913ca57a15f7d5ac0019813ce4e2`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
