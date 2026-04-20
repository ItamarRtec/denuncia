# Mesa 082123 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.097509+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CALLAO
- **Local de votación**: IEP DIVINO MAESTRO (código 52998)
- **Ubigeo**: 240101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 203
- Votos válidos: 150
- Participación: 67.893%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:32:30+00:00` | `2026-04-12 20:32:30 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:32:30+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:32:30+00:00` | `2026-04-12 20:32:30 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:45:24+00:00` | `2026-04-12 21:45:24 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:45:42+00:00` | `2026-04-12 21:45:42 (Lima)` |
| Última firma humana | `2026-04-13T02:46:12+00:00` | `2026-04-12 21:46:12 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.22 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:32:30 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:45:42 (Lima), es decir **1.22 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:32:28+00:00` | `2026-04-12 20:32:28 (Lima)` | -0.00h |
| 1 | GIRALDO NEYRA felix Humberto FIR 25574761 sw 296b9188c81364503a464669cb9a8c207cb0fb1e | 25574761 | `2026-04-13T02:45:42+00:00` | `2026-04-12 21:45:42 (Lima)` | +1.22h |
| 2 | HAYNES RAMIREZ roberto Carlos FIR 25861464 sw d12877f908a7f7236725177f780318445da31528 | 25861464 | `2026-04-13T02:46:12+00:00` | `2026-04-12 21:46:12 (Lima)` | +1.23h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082123**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8932a0f65c2b54cba26f3f748ba4b2eb58eefb45a82d4b8c1898db2a55b60e8f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
