# Mesa 051044 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.355156+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: UNIVERSIDAD RICARDO PALMA (código 3221)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 297
- Votos emitidos: 221
- Votos válidos: 205
- Participación: 74.411%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:31:36+00:00` | `2026-04-12 21:31:36 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:31:36+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:31:36+00:00` | `2026-04-12 21:31:36 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:59:57+00:00` | `2026-04-13 08:59:57 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:00:19+00:00` | `2026-04-13 09:00:19 (Lima)` |
| Última firma humana | `2026-04-13T14:00:56+00:00` | `2026-04-13 09:00:56 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.48 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:31:36 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:00:19 (Lima), es decir **11.48 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:24:23+00:00` | `2026-04-12 21:24:23 (Lima)` | -0.12h |
| 1 | WILLIAMS GUERRERO martin Alberto FIR 25588517 sw 09c3999af64ad890cebd4cf23e6cab7c5c94764f | 25588517 | `2026-04-13T14:00:19+00:00` | `2026-04-13 09:00:19 (Lima)` | +11.48h |
| 2 | WU LARA eduardo Jose FIR 07458980 sw 64eb2cec20fb90cb891f271a771818afc3b7edf7 | 07458980 | `2026-04-13T14:00:56+00:00` | `2026-04-13 09:00:56 (Lima)` | +11.49h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051044**
2. Descargar el PDF del acta
3. Verificar SHA-256: `96b1fba505726f68955f2a9721c6c14ca0202b5cebc9c4e597c078bf797d8f84`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
