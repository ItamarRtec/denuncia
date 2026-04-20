# Mesa 083304 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.534164+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: VENTANILLA
- **Local de votación**: IE 5122 JOSE ANDRES RAZURI ESTEVEZ (código 4876)
- **Ubigeo**: 240106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 231
- Votos válidos: 203
- Participación: 77.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:51:21+00:00` | `2026-04-12 21:51:21 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:51:21+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:51:21+00:00` | `2026-04-12 21:51:21 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:38:03+00:00` | `2026-04-13 09:38:03 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:38:24+00:00` | `2026-04-13 09:38:24 (Lima)` |
| Última firma humana | `2026-04-13T14:39:07+00:00` | `2026-04-13 09:39:07 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.78 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:51:21 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:38:24 (Lima), es decir **11.78 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:51:15+00:00` | `2026-04-12 21:51:15 (Lima)` | -0.00h |
| 1 | RAMOS ESCOBEDO karina Liliana FIR 76282835 sw c196c60fac1d262cb756791eadaf6ba1cf02d798 | 76282835 | `2026-04-13T14:38:24+00:00` | `2026-04-13 09:38:24 (Lima)` | +11.78h |
| 2 | RAMOS PRINCIPE robinson FIR 45646285 sw 4d04c39fe13be15b37f1d36f1e8586158630f262 | 45646285 | `2026-04-13T14:38:37+00:00` | `2026-04-13 09:38:37 (Lima)` | +11.79h |
| 3 | QUISPE HUAMAN miguel Salvador FIR 10802546 sw 4922d19f9d752802123bff62a9d52ef76d6b66cc | 10802546 | `2026-04-13T14:38:51+00:00` | `2026-04-13 09:38:51 (Lima)` | +11.79h |
| 4 | BONILLA DIONISIO raquel Ycela FIR 41434078 sw 04acec78ecf56a1c088b7cb4ef7a77db4d2f88d0 | 41434078 | `2026-04-13T14:39:07+00:00` | `2026-04-13 09:39:07 (Lima)` | +11.80h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083304**
2. Descargar el PDF del acta
3. Verificar SHA-256: `1815ec9479b12f031d31f98fb1557c6b0050dca3e31c6fec3cc9fdee341cdb25`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
