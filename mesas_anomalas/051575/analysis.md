# Mesa 051575 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.321058+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: LOSA DEPORTIVA MEDALLA MILAGROSA (código 54310)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 214
- Votos válidos: 198
- Participación: 71.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:58:39+00:00` | `2026-04-12 19:58:39 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:58:39+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:58:39+00:00` | `2026-04-12 19:58:39 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:42:26+00:00` | `2026-04-12 23:42:26 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:43:04+00:00` | `2026-04-12 23:43:04 (Lima)` |
| Última firma humana | `2026-04-13T04:43:48+00:00` | `2026-04-12 23:43:48 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.74 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:58:39 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:43:04 (Lima), es decir **3.74 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:58:38+00:00` | `2026-04-12 19:58:38 (Lima)` | -0.00h |
| 1 | PHOCCO GARCIA ivonne Natalia FIR 09391794 sw 61261218b4d2779570614542ea5d092f75961cc6 | 09391794 | `2026-04-13T04:43:04+00:00` | `2026-04-12 23:43:04 (Lima)` | +3.74h |
| 2 | QUISPE NINAHUANCA marco Antonio FIR 21287433 sw c8c000c73db9a0791f5e44ffba44f53580d262f6 | 21287433 | `2026-04-13T04:43:21+00:00` | `2026-04-12 23:43:21 (Lima)` | +3.75h |
| 3 | RICSE CARHUAMACA marcial Ruben FIR 10257191 sw f559e5690c6e7c3789f94465e18ace754a669205 | 10257191 | `2026-04-13T04:43:48+00:00` | `2026-04-12 23:43:48 (Lima)` | +3.75h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051575**
2. Descargar el PDF del acta
3. Verificar SHA-256: `25b405689382bbc3f42b50591cf9f1c69e9196fd6f85813821f0575d3f63474e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
