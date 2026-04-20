# Mesa 040175 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.096838+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IE 2097 (código 2802)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 252
- Votos válidos: 231
- Participación: 84.281%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:03:03+00:00` | `2026-04-12 20:03:03 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:03:03+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:03:03+00:00` | `2026-04-12 20:03:03 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T01:52:03+00:00` | `2026-04-12 20:52:03 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T01:52:17+00:00` | `2026-04-12 20:52:17 (Lima)` |
| Última firma humana | `2026-04-13T01:54:00+00:00` | `2026-04-12 20:54:00 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.82 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:03:03 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 20:52:17 (Lima), es decir **0.82 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:03:01+00:00` | `2026-04-12 20:03:01 (Lima)` | -0.00h |
| 1 | CONSIGLIERI CERDAN anggelo Piero FIR 72642416 sw 4977ae35e3775c80fd275c89d999f35ec79690fe | 72642416 | `2026-04-13T01:52:17+00:00` | `2026-04-12 20:52:17 (Lima)` | +0.82h |
| 2 | CARRERA PAREDES mary Julia FIR 42733563 sw 74894c1d17d3d1b0b1da961607353e85b35e0414 | 42733563 | `2026-04-13T01:52:51+00:00` | `2026-04-12 20:52:51 (Lima)` | +0.83h |
| 3 | CARRILLO PERALTA mirella Cristina FIR 74694430 sw c9e0db1373d3f7dbdfd080af0bc28e43388add73 | 74694430 | `2026-04-13T01:54:00+00:00` | `2026-04-12 20:54:00 (Lima)` | +0.85h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **040175**
2. Descargar el PDF del acta
3. Verificar SHA-256: `9cd02ae86c7fbf43de79bf134cbabf800f470f8f734ee6a601995587a9b7727c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
