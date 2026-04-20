# Mesa 083612 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.066250+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: VENTANILLA
- **Local de votación**: IE 5141 DIVINO MAESTRO (código 10029)
- **Ubigeo**: 240106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 236
- Votos válidos: 188
- Participación: 78.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:41:17+00:00` | `2026-04-12 21:41:17 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:37:32+00:00` | `2026-04-12 21:37:32 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:41:17+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:41:17+00:00` | `2026-04-12 21:41:17 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:22:36+00:00` | `2026-04-13 09:22:36 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:22:53+00:00` | `2026-04-13 09:22:53 (Lima)` |
| Última firma humana | `2026-04-13T14:23:26+00:00` | `2026-04-13 09:23:26 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.69 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:41:17 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:22:53 (Lima), es decir **11.69 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:37:28+00:00` | `2026-04-12 21:37:28 (Lima)` | -0.06h |
| 1 | RIVERA ARIAS juan Gualberto FIR 09365262 sw 92f44a48aa6fbb5fb483f2e88ad1f16976c50108 | 09365262 | `2026-04-13T14:22:53+00:00` | `2026-04-13 09:22:53 (Lima)` | +11.69h |
| 2 | QUIROZ CORREA jorge Luis FIR 25798357 sw edb6393edb31f463645dacef44528dc0563f15c5 | 25798357 | `2026-04-13T14:23:11+00:00` | `2026-04-13 09:23:11 (Lima)` | +11.70h |
| 3 | RISCO CHAVEZ rossan Estefany FIR 48083247 sw d556be50d170d23f12ee8086593f12e1e73ecf20 | 48083247 | `2026-04-13T14:23:26+00:00` | `2026-04-13 09:23:26 (Lima)` | +11.70h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083612**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c8d0b784acec7a03c24c48c75d554e2c57139983599c42f7908984bb87dfb612`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
