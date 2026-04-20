# Mesa 054900 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.726500+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 6037 INCA PACHACUTEC - SECUNDARIA (código 3349)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 230
- Votos válidos: 206
- Participación: 76.923%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:55:16+00:00` | `2026-04-12 20:55:16 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:55:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:55:16+00:00` | `2026-04-12 20:55:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T11:50:16+00:00` | `2026-04-13 06:50:16 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T11:51:00+00:00` | `2026-04-13 06:51:00 (Lima)` |
| Última firma humana | `2026-04-13T11:51:23+00:00` | `2026-04-13 06:51:23 (Lima)` |

**Brecha primera firma humana vs publicación:** **+9.93 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:55:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 06:51:00 (Lima), es decir **9.93 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:55:14+00:00` | `2026-04-12 20:55:14 (Lima)` | -0.00h |
| 1 | PARRAGUEZ MERCADO diana Elizabeth FIR 72506010 sw 09b97d749e14b2ced5784f7af2fb4e883115edf2 | 72506010 | `2026-04-13T11:51:00+00:00` | `2026-04-13 06:51:00 (Lima)` | +9.93h |
| 2 | PEREZ NOLORBE juan Pablo FIR 47935019 sw 1346c1fd39c1dcd4112d7cb1f6d661b094b3b019 | 47935019 | `2026-04-13T11:51:12+00:00` | `2026-04-13 06:51:12 (Lima)` | +9.93h |
| 3 | PRADO CABRERA lucyen Marye FIR 48297938 sw 1857cb70df50f38fa73a8a992ff19323e30c1ec7 | 48297938 | `2026-04-13T11:51:23+00:00` | `2026-04-13 06:51:23 (Lima)` | +9.94h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054900**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2e0799cf0448f5363390a894dec1bb2c5b26501fd897d54bec171400a71aa0d7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
