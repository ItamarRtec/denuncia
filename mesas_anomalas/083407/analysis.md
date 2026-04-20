# Mesa 083407 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.871697+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: VENTANILLA
- **Local de votación**: IE 5051 VIRGEN DE FATIMA- SECUNDARIA (código 4882)
- **Ubigeo**: 240106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 228
- Votos válidos: 189
- Participación: 76.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:00:05+00:00` | `2026-04-12 21:00:05 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:00:05+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:00:05+00:00` | `2026-04-12 21:00:05 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:58:31+00:00` | `2026-04-12 21:58:31 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:59:31+00:00` | `2026-04-12 21:59:31 (Lima)` |
| Última firma humana | `2026-04-13T03:00:33+00:00` | `2026-04-12 22:00:33 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.99 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:00:05 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:59:31 (Lima), es decir **0.99 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:00:02+00:00` | `2026-04-12 21:00:02 (Lima)` | -0.00h |
| 1 | HERRERA AYOQUE dan Nelson FIR 40981287 sw dbee6c54540e144b0f877a5df99386e3b08865a7 | 40981287 | `2026-04-13T02:59:31+00:00` | `2026-04-12 21:59:31 (Lima)` | +0.99h |
| 2 | GUERRA ORTEGA maritza FIR 10741339 sw 447be3de191a4db6be1ac8983928e6d8eb42062f | 10741339 | `2026-04-13T03:00:13+00:00` | `2026-04-12 22:00:13 (Lima)` | +1.00h |
| 3 | FLORES MINAYA jorge Eduardo FIR 45770526 sw f5e98659b78634aee7449f4e5857aeddd4160602 | 45770526 | `2026-04-13T03:00:33+00:00` | `2026-04-12 22:00:33 (Lima)` | +1.01h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083407**
2. Descargar el PDF del acta
3. Verificar SHA-256: `75fdaeda8bbfaf7676b6212d289f083ef67c45122ba439ee39b6250f24b58ce8`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
