# Mesa 045239 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.828704+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: IEP SANTA RITA DE CASIA (código 2996)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 218
- Votos válidos: 210
- Participación: 72.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:56:55+00:00` | `2026-04-12 19:56:55 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:56:55+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:56:55+00:00` | `2026-04-12 19:56:55 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:49:27+00:00` | `2026-04-12 23:49:27 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:49:44+00:00` | `2026-04-12 23:49:44 (Lima)` |
| Última firma humana | `2026-04-13T04:50:56+00:00` | `2026-04-12 23:50:56 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.88 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:56:55 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:49:44 (Lima), es decir **3.88 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:56:53+00:00` | `2026-04-12 19:56:53 (Lima)` | -0.00h |
| 1 | FIGARI BELLO patricia FIR 07882523 sw 684cd9aec0e0793d237d1d8b504e89934cd6fa87 | 07882523 | `2026-04-13T04:49:44+00:00` | `2026-04-12 23:49:44 (Lima)` | +3.88h |
| 2 | DUNCKER BELEVAN eduardo Luis FIR 07756336 sw be53ed6e583848132209a2cb4eb8af4dbaa79d7f | 07756336 | `2026-04-13T04:50:04+00:00` | `2026-04-12 23:50:04 (Lima)` | +3.89h |
| 3 | GARCIA TORRES fabiola Marlene FIR 46038309 sw 4b6b3c992081a6967b12afacce7798ee0f68b662 | 46038309 | `2026-04-13T04:50:19+00:00` | `2026-04-12 23:50:19 (Lima)` | +3.89h |
| 4 | JULCA VELAZCO violeta Viviana FIR 07726062 sw 288127234cbd0209f66138768676b6da22edfa6a | 07726062 | `2026-04-13T04:50:56+00:00` | `2026-04-12 23:50:56 (Lima)` | +3.90h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045239**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2ada175bfa81fc10114d560da6ab5aafd880b29e0e2ae0912f8503563a129769`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
