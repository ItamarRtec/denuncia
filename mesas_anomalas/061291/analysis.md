# Mesa 061291 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.609794+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LOS OLIVOS
- **Local de votación**: IEP MANUEL ASCENCIO SEGURA (código 17393)
- **Ubigeo**: 140142

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 247
- Votos válidos: 223
- Participación: 82.609%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:52:44+00:00` | `2026-04-12 20:52:44 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:52:44+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:52:44+00:00` | `2026-04-12 20:52:44 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:15:33+00:00` | `2026-04-12 22:15:33 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:15:43+00:00` | `2026-04-12 22:15:43 (Lima)` |
| Última firma humana | `2026-04-13T03:16:08+00:00` | `2026-04-12 22:16:08 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.38 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:52:44 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:15:43 (Lima), es decir **1.38 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:52:42+00:00` | `2026-04-12 20:52:42 (Lima)` | -0.00h |
| 1 | SANCHEZ SOLIS jorge Luis FIR 72932671 sw 9cb3864890ab8576f6c53259f47b32e7a4c367be | 72932671 | `2026-04-13T03:15:43+00:00` | `2026-04-12 22:15:43 (Lima)` | +1.38h |
| 2 | SALAZAR CRUZ yamile Alexandra FIR 72698753 sw 353c66db5b94fcab1d51e8575d35a49714c45f60 | 72698753 | `2026-04-13T03:15:55+00:00` | `2026-04-12 22:15:55 (Lima)` | +1.39h |
| 3 | SOTO EPQUIN fabian Marino FIR 74123680 sw fad685fecad3ed98746cf5e4be0d95896e445c15 | 74123680 | `2026-04-13T03:16:08+00:00` | `2026-04-12 22:16:08 (Lima)` | +1.39h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061291**
2. Descargar el PDF del acta
3. Verificar SHA-256: `da5350fde003bc07a082d60d7231b8b191ef0b64794dd4336b8b020a74caac03`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
