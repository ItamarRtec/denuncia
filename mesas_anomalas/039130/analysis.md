# Mesa 039130 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.483827+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: BREÑA
- **Local de votación**: UNIVERSIDAD INTERAMERICANA DE DESARROLLO (código 50360)
- **Ubigeo**: 140104

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 230
- Votos válidos: 211
- Participación: 76.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:56:12+00:00` | `2026-04-12 21:56:12 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:56:12+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:56:12+00:00` | `2026-04-12 21:56:12 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:25:25+00:00` | `2026-04-13 09:25:25 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:25:43+00:00` | `2026-04-13 09:25:43 (Lima)` |
| Última firma humana | `2026-04-13T14:26:22+00:00` | `2026-04-13 09:26:22 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.49 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:56:12 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:25:43 (Lima), es decir **11.49 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:56:09+00:00` | `2026-04-12 21:56:09 (Lima)` | -0.00h |
| 1 | SAAVEDRA GUILLEN edita Emilia FIR 07912818 sw 3a9fa80c0b9205bff162876aa9b9b4656a3e51ab | 07912818 | `2026-04-13T14:25:43+00:00` | `2026-04-13 09:25:43 (Lima)` | +11.49h |
| 2 | SALAZAR LA TORRE cesar Armando FIR 78375991 sw c67892938c39930a30abf04408882510f9fa6b6c | 78375991 | `2026-04-13T14:26:06+00:00` | `2026-04-13 09:26:06 (Lima)` | +11.50h |
| 3 | RUFINO CASTILLO irvin Alexander FIR 74066706 sw 8d0802449a81e4bc68e87d11b06500586183bacf | 74066706 | `2026-04-13T14:26:22+00:00` | `2026-04-13 09:26:22 (Lima)` | +11.50h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **039130**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8680d0a61d08c9c585dd274ef0e6cb63983420b890d6cbfb78c8bc19d27598ed`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
