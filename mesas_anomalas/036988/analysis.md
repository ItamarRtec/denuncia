# Mesa 036988 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.145171+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IEP INNOVA SCHOOLS BERTELLO (código 54803)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 223
- Votos válidos: 188
- Participación: 74.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:12:54+00:00` | `2026-04-12 22:12:54 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:12:54+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:12:54+00:00` | `2026-04-12 22:12:54 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T07:06:30+00:00` | `2026-04-13 02:06:30 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T07:07:52+00:00` | `2026-04-13 02:07:52 (Lima)` |
| Última firma humana | `2026-04-13T07:09:03+00:00` | `2026-04-13 02:09:03 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.92 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:12:54 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 02:07:52 (Lima), es decir **3.92 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:12:51+00:00` | `2026-04-12 22:12:51 (Lima)` | -0.00h |
| 1 | PAREDES AGUILAR maria Del Rosario FIR 29673997 sw 10c06ab7f3714129dd4b03232f0e4ebdc4e9dc78 | 29673997 | `2026-04-13T07:07:52+00:00` | `2026-04-13 02:07:52 (Lima)` | +3.92h |
| 2 | PANIHUARA CAPCHA luz Maria FIR 09960442 sw 65bd99ddfd7d067d5ba5f20f946e0f13c8afde0b | 09960442 | `2026-04-13T07:08:22+00:00` | `2026-04-13 02:08:22 (Lima)` | +3.92h |
| 3 | PAREDES SANCHEZ bartolome FIR 06138231 sw 9c66c5c2124e8ba3cb5cb760d24a8fadec88cdf3 | 06138231 | `2026-04-13T07:09:03+00:00` | `2026-04-13 02:09:03 (Lima)` | +3.94h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036988**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5113a136e4bea13269608d05bf77b6347faaedd8bb5bb65418795c32771f0e7c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
