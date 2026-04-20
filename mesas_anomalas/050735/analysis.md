# Mesa 050735 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.717780+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IE 7087 SANTIAGO DE SURCO (código 3204)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 238
- Votos válidos: 227
- Participación: 79.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:29:35+00:00` | `2026-04-12 20:29:35 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:29:35+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:29:35+00:00` | `2026-04-12 20:29:35 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:41:44+00:00` | `2026-04-12 23:41:44 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:42:00+00:00` | `2026-04-12 23:42:00 (Lima)` |
| Última firma humana | `2026-04-13T04:43:12+00:00` | `2026-04-12 23:43:12 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.21 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:29:35 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:42:00 (Lima), es decir **3.21 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:29:33+00:00` | `2026-04-12 20:29:33 (Lima)` | -0.00h |
| 1 | ROJAS SEPULVEDA jose Alberto FIR 41331216 sw 4f1bdf1f7b64cacb9a2cd3a3221d1abe5d5d2c7d | 41331216 | `2026-04-13T04:42:00+00:00` | `2026-04-12 23:42:00 (Lima)` | +3.21h |
| 2 | RIVERA CHAVEZ virginia Consuelo FIR 42251897 sw bab0f39d075f4846baff5877ef091511cfe5c498 | 42251897 | `2026-04-13T04:42:20+00:00` | `2026-04-12 23:42:20 (Lima)` | +3.21h |
| 3 | ROMERO SUAREZ celso Jorge FIR 44284889 sw c5c7894ed217be5a65553509590ea097f51fdd99 | 44284889 | `2026-04-13T04:42:51+00:00` | `2026-04-12 23:42:51 (Lima)` | +3.22h |
| 4 | RIOS DIAZ nancy Magaly FIR 29726722 sw 1d0ef6a1832aa6e4792eafe4e7f2f581b9e96ae5 | 29726722 | `2026-04-13T04:43:12+00:00` | `2026-04-12 23:43:12 (Lima)` | +3.23h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050735**
2. Descargar el PDF del acta
3. Verificar SHA-256: `757cd7cd5bb3e066da0525a559ea1977bf2a5fa16b0b3fb03e5ffe57066d964c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
