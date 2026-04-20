# Mesa 082544 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.189902+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: BELLAVISTA
- **Local de votación**: IE 5050 SAN PEDRO (código 4824)
- **Ubigeo**: 240102

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 268
- Votos válidos: 253
- Participación: 89.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:37:51+00:00` | `2026-04-12 20:37:51 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:37:51+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:37:51+00:00` | `2026-04-12 20:37:51 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:11:02+00:00` | `2026-04-12 22:11:02 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:11:19+00:00` | `2026-04-12 22:11:19 (Lima)` |
| Última firma humana | `2026-04-13T03:12:27+00:00` | `2026-04-12 22:12:27 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.56 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:37:51 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:11:19 (Lima), es decir **1.56 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:37:48+00:00` | `2026-04-12 20:37:48 (Lima)` | -0.00h |
| 1 | SANCHEZ DIAZ gisella Vanessa FIR 40232539 sw 4a90cce4cbefa5b849fc2e460d39a139ba825f01 | 40232539 | `2026-04-13T03:11:19+00:00` | `2026-04-12 22:11:19 (Lima)` | +1.56h |
| 2 | SANTISTEBAN VARGAS joel FIR 70888085 sw 2fb812c130964e6f761b09b7f1c0a8af0c981f9f | 70888085 | `2026-04-13T03:11:39+00:00` | `2026-04-12 22:11:39 (Lima)` | +1.56h |
| 3 | RUIZ MONTES jesus Francisco FIR 43309405 sw c33cf81aa8d4ea74e0616e9d787987fecb5db5ff | 43309405 | `2026-04-13T03:11:59+00:00` | `2026-04-12 22:11:59 (Lima)` | +1.57h |
| 4 | GALVAN CABEZAS erik Pio FIR 07502564 sw b1fd43fa06f433fc5157c8f2fa55ba56a254bb61 | 07502564 | `2026-04-13T03:12:27+00:00` | `2026-04-12 22:12:27 (Lima)` | +1.58h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082544**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2708772a4312fd60863c246b71401cdfbb38b067e9b6a6d01aafa598df855413`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
