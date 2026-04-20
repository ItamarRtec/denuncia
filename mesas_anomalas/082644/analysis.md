# Mesa 082644 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.621319+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: BELLAVISTA
- **Local de votación**: IEP VIRGEN DEL ROSARIO (código 51701)
- **Ubigeo**: 240102

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 247
- Votos válidos: 223
- Participación: 82.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:46:56+00:00` | `2026-04-12 20:46:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:46:56+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:46:56+00:00` | `2026-04-12 20:46:56 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:44:12+00:00` | `2026-04-12 22:44:12 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:44:28+00:00` | `2026-04-12 22:44:28 (Lima)` |
| Última firma humana | `2026-04-13T03:45:34+00:00` | `2026-04-12 22:45:34 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.96 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:46:56 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:44:28 (Lima), es decir **1.96 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:46:53+00:00` | `2026-04-12 20:46:53 (Lima)` | -0.00h |
| 1 | GARCIA MARTINEZ maria Belen FIR 74653390 sw 10045e4b76fc6ce44500dc7a77dcc81ae0b9d2fd | 74653390 | `2026-04-13T03:44:28+00:00` | `2026-04-12 22:44:28 (Lima)` | +1.96h |
| 2 | FIGUEROA AGUIRRE juan Maximo FIR 25483863 sw 96e8100152b7e8a459ad91e145658897d9a6fbc7 | 25483863 | `2026-04-13T03:45:34+00:00` | `2026-04-12 22:45:34 (Lima)` | +1.98h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082644**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5ed4148a2f3e7852279c19c891c09692738f2e41f0cc9818dd463ebcbbfe19ab`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
