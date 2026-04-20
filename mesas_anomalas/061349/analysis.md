# Mesa 061349 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.530298+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LOS OLIVOS
- **Local de votación**: IEP ALEXANDER VON HUMBOLDT (código 31259)
- **Ubigeo**: 140142

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 218
- Votos válidos: 190
- Participación: 72.91%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:12:50+00:00` | `2026-04-12 21:12:50 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:12:50+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:12:50+00:00` | `2026-04-12 21:12:50 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:42:06+00:00` | `2026-04-12 22:42:06 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:42:29+00:00` | `2026-04-12 22:42:29 (Lima)` |
| Última firma humana | `2026-04-13T03:42:52+00:00` | `2026-04-12 22:42:52 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.49 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:12:50 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:42:29 (Lima), es decir **1.49 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:12:48+00:00` | `2026-04-12 21:12:48 (Lima)` | -0.00h |
| 1 | ARCE ATENCIO edgar FIR 08664168 sw 048e6b8ae5ad05343118d7720ae406e71ba98813 | 08664168 | `2026-04-13T03:42:29+00:00` | `2026-04-12 22:42:29 (Lima)` | +1.49h |
| 2 | ARELLANO CANTARO maria Soledad FIR 10710272 sw 0e105814f1e85b0a096aaad8e8942fee8b60c58e | 10710272 | `2026-04-13T03:42:41+00:00` | `2026-04-12 22:42:41 (Lima)` | +1.50h |
| 3 | ANTENUCCI CAMAVILCA maria Esther FIR 22665430 sw cd1a200941dea2d79f9eea34c2ac3ca38bdb6c32 | 22665430 | `2026-04-13T03:42:52+00:00` | `2026-04-12 22:42:52 (Lima)` | +1.50h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061349**
2. Descargar el PDF del acta
3. Verificar SHA-256: `64db9d93bd21fe705c06789819245de009dc37153aeb77eabd2c9e011c2fbde9`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
