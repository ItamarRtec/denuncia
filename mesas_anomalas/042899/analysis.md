# Mesa 042899 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.468411+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA VICTORIA
- **Local de votación**: IE 1112 VICTOR ANDRES BELAUNDE (código 2902)
- **Ubigeo**: 140109

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 219
- Votos válidos: 199
- Participación: 73.244%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T04:21:32+00:00` | `2026-04-12 23:21:32 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T04:21:32+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T04:21:32+00:00` | `2026-04-12 23:21:32 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:02:44+00:00` | `2026-04-13 09:02:44 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:03:48+00:00` | `2026-04-13 09:03:48 (Lima)` |
| Última firma humana | `2026-04-13T14:04:28+00:00` | `2026-04-13 09:04:28 (Lima)` |

**Brecha primera firma humana vs publicación:** **+9.70 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 23:21:32 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:03:48 (Lima), es decir **9.70 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T04:21:31+00:00` | `2026-04-12 23:21:31 (Lima)` | -0.00h |
| 1 | MARCOS NICHO mirtha Cecilia FIR 07473466 sw b98a8fa83de412c394a731a7b3f7a9789d8a2001 | 07473466 | `2026-04-13T14:03:48+00:00` | `2026-04-13 09:03:48 (Lima)` | +9.70h |
| 2 | MELGAR SABOYA yennyfer Rebeca FIR 48167793 sw c943df18985e8d1118c2a8692d7a10d162ec4686 | 48167793 | `2026-04-13T14:04:04+00:00` | `2026-04-13 09:04:04 (Lima)` | +9.71h |
| 3 | MEDRANO BRUNO pablo Algerlis FIR 77792476 sw 187cc562a5569537c44d633393bc91a7c4ab4f54 | 77792476 | `2026-04-13T14:04:28+00:00` | `2026-04-13 09:04:28 (Lima)` | +9.72h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042899**
2. Descargar el PDF del acta
3. Verificar SHA-256: `05b6559b515976ca478640983c17cb2cd9f2fc7b634775521b5c1260f4590f48`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
