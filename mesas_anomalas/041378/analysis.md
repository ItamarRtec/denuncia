# Mesa 041378 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.512883+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IEP MARIA GORETTI DEL ALAMO (código 54413)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 223
- Votos válidos: 193
- Participación: 74.582%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:15:18+00:00` | `2026-04-12 22:15:18 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:15:18+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:15:18+00:00` | `2026-04-12 22:15:18 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:58:46+00:00` | `2026-04-13 08:58:46 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:59:11+00:00` | `2026-04-13 08:59:11 (Lima)` |
| Última firma humana | `2026-04-13T13:59:43+00:00` | `2026-04-13 08:59:43 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.73 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:15:18 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:59:11 (Lima), es decir **10.73 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:15:16+00:00` | `2026-04-12 22:15:16 (Lima)` | -0.00h |
| 1 | VALVERDE HIDALGO marisol Estrella FIR 77599914 sw e3b270d65c2b0a2ea37e854247fcb36ca0d96eba | 77599914 | `2026-04-13T13:59:11+00:00` | `2026-04-13 08:59:11 (Lima)` | +10.73h |
| 2 | TORRES ORE marlene FIR 09479718 sw 3cecc7d41e5089b69f9e4de4ec31b37cf6d53d6a | 09479718 | `2026-04-13T13:59:34+00:00` | `2026-04-13 08:59:34 (Lima)` | +10.74h |
| 3 | VALDIVIA GAVILAN leonel Anibal FIR 76023551 sw 0c986ac360533ea47ce90afe7788571fae3479e3 | 76023551 | `2026-04-13T13:59:43+00:00` | `2026-04-13 08:59:43 (Lima)` | +10.74h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041378**
2. Descargar el PDF del acta
3. Verificar SHA-256: `281cd151be87593f1f88ae4c2168dbb7d8bc51fdcc590cf12acfd8d9cedfe83f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
