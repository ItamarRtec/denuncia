# Mesa 061962 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.099146+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IEP VIRGEN DE FATIMA MILAGROSA (código 4996)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 261
- Votos válidos: 238
- Participación: 87.291%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:00:07+00:00` | `2026-04-12 22:00:07 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:00:07+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:00:07+00:00` | `2026-04-12 22:00:07 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:06:35+00:00` | `2026-04-13 09:06:35 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:06:58+00:00` | `2026-04-13 09:06:58 (Lima)` |
| Última firma humana | `2026-04-13T14:07:09+00:00` | `2026-04-13 09:07:09 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.11 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:00:07 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:06:58 (Lima), es decir **11.11 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:00:05+00:00` | `2026-04-12 22:00:05 (Lima)` | -0.00h |
| 1 | CCAYO ARAUJO elizabeth Kennedy FIR 46957715 sw 61bbcd656cd6daa1344f56dc3c8f9ea318fa1460 | 46957715 | `2026-04-13T14:06:58+00:00` | `2026-04-13 09:06:58 (Lima)` | +11.11h |
| 2 | CHAVEZ GAMARRA noelia FIR 41751648 sw 8447c13a3ec092eaffc2ba6172ff4a2451c478c6 | 41751648 | `2026-04-13T14:07:09+00:00` | `2026-04-13 09:07:09 (Lima)` | +11.12h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061962**
2. Descargar el PDF del acta
3. Verificar SHA-256: `6c59b7ab2d34e3e6a80eed47abf4a9e48bb48cdc0471e83437a49c89879e5c0b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
