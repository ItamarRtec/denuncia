# Mesa 036509 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.559701+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE SIMON BOLIVAR (código 4944)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 261
- Votos válidos: 243
- Participación: 87.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:56:24+00:00` | `2026-04-12 21:56:24 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:53:25+00:00` | `2026-04-12 21:53:25 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:56:24+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:56:24+00:00` | `2026-04-12 21:56:24 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:22:17+00:00` | `2026-04-13 08:22:17 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:45:51+00:00` | `2026-04-13 08:45:51 (Lima)` |
| Última firma humana | `2026-04-13T13:51:22+00:00` | `2026-04-13 08:51:22 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.82 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:56:24 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:45:51 (Lima), es decir **10.82 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:48:21+00:00` | `2026-04-12 21:48:21 (Lima)` | -0.13h |
| 1 | MIRABAL PILLACA jean Pool FIR 60777591 sw e5db2a3ab2ffce26d754f3d1e20031186ebb307a | 60777591 | `2026-04-13T13:45:51+00:00` | `2026-04-13 08:45:51 (Lima)` | +10.82h |
| 2 | MONTALVAN CABEZAS david Fernando FIR 07949764 sw b3bab8f7fca2b8ef8176136458d20a960592f993 | 07949764 | `2026-04-13T13:49:04+00:00` | `2026-04-13 08:49:04 (Lima)` | +10.88h |
| 3 | MORALES HUANCA candy Yesica FIR 44174967 sw e8e1fd7f03bb32a94efa77cf7ec0cb4634122955 | 44174967 | `2026-04-13T13:51:22+00:00` | `2026-04-13 08:51:22 (Lima)` | +10.92h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036509**
2. Descargar el PDF del acta
3. Verificar SHA-256: `884679e0ecdd8a21b4f40a5d6271251785e1917eaa2c785cdc1e0e48ad93370a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
