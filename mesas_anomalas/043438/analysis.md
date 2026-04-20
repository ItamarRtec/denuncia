# Mesa 043438 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.987051+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA MOLINA
- **Local de votación**: IE 1286 HEROES DEL CENEPA (código 5138)
- **Ubigeo**: 140110

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 277
- Votos válidos: 273
- Participación: 92.642%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:33:23+00:00` | `2026-04-12 20:33:23 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:33:23+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:33:23+00:00` | `2026-04-12 20:33:23 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:02:10+00:00` | `2026-04-12 22:02:10 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:02:32+00:00` | `2026-04-12 22:02:32 (Lima)` |
| Última firma humana | `2026-04-13T03:03:42+00:00` | `2026-04-12 22:03:42 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.49 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:33:23 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:02:32 (Lima), es decir **1.49 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:33:20+00:00` | `2026-04-12 20:33:20 (Lima)` | -0.00h |
| 1 | YOHANN VENEGAS jonathan Santino FIR 70510672 sw eebee09183f083bede711e77edba2f4d76936a44 | 70510672 | `2026-04-13T03:02:32+00:00` | `2026-04-12 22:02:32 (Lima)` | +1.49h |
| 2 | ZAMORA MOSCOSO luby Tessy FIR 70114012 sw 394d72ab71452b7929f1d984fe99f3b42b5001df | 70114012 | `2026-04-13T03:02:52+00:00` | `2026-04-12 22:02:52 (Lima)` | +1.49h |
| 3 | SOBRINO RODRIGUEZ irma Gisella Del Rocio FIR 08162512 sw fdd4ddcb26d60f8e9bff4e192bf57c154ee3fff4 | 08162512 | `2026-04-13T03:03:10+00:00` | `2026-04-12 22:03:10 (Lima)` | +1.50h |
| 4 | BONILLA HERREROS fernando Miguel FIR 31614938 sw 4de3ab546baf394f0c6400ba736708c219f5f1e7 | 31614938 | `2026-04-13T03:03:42+00:00` | `2026-04-12 22:03:42 (Lima)` | +1.51h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **043438**
2. Descargar el PDF del acta
3. Verificar SHA-256: `a13ef4d0c5f006b347b6c80f8aea3eb4a32d2f7d94268ad16ba7ab41cb4d2578`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
