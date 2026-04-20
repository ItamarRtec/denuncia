# Mesa 040501 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.446958+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IE PERUANO SUIZO (código 2836)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 270
- Votos válidos: 253
- Participación: 90.301%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:55:48+00:00` | `2026-04-12 21:55:48 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:25:08+00:00` | `2026-04-12 21:25:08 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:55:48+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:55:48+00:00` | `2026-04-12 21:55:48 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:11:45+00:00` | `2026-04-13 09:11:45 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:12:51+00:00` | `2026-04-13 09:12:51 (Lima)` |
| Última firma humana | `2026-04-13T14:13:13+00:00` | `2026-04-13 09:13:13 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.28 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:55:48 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:12:51 (Lima), es decir **11.28 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:25:06+00:00` | `2026-04-12 21:25:06 (Lima)` | -0.51h |
| 1 | RASHUAMAN FLORES ricardo FIR 09004871 sw 59efbbb5d0cbbe13110986ddb422e56e99cd4c0f | 09004871 | `2026-04-13T14:12:51+00:00` | `2026-04-13 09:12:51 (Lima)` | +11.28h |
| 2 | RIOS FLORES fabiana Andrea FIR 75908045 sw fb9d7016048176a8130ac3a8ea05a98085326907 | 75908045 | `2026-04-13T14:13:02+00:00` | `2026-04-13 09:13:02 (Lima)` | +11.29h |
| 3 | RAMOS BARTUREN juan Diego Ever FIR 74720245 sw 18316835eceaa88ef6c55d1e0e767bdd9795c2ef | 74720245 | `2026-04-13T14:13:13+00:00` | `2026-04-13 09:13:13 (Lima)` | +11.29h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **040501**
2. Descargar el PDF del acta
3. Verificar SHA-256: `176540844cf6b1014193afca297db0e03d91ab9be2f6f6c4495862de4bfc8657`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
