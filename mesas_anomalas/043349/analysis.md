# Mesa 043349 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.728996+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA MOLINA
- **Local de votación**: IEP COOP. SERV. EDUC. ING. CARLOS LISSON BEINGOLEA LTDA. (código 2924)
- **Ubigeo**: 140110

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 258
- Votos válidos: 245
- Participación: 86.288%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:08:48+00:00` | `2026-04-12 21:08:48 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:08:48+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:08:48+00:00` | `2026-04-12 21:08:48 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:46:52+00:00` | `2026-04-12 22:46:52 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:47:12+00:00` | `2026-04-12 22:47:12 (Lima)` |
| Última firma humana | `2026-04-13T03:50:11+00:00` | `2026-04-12 22:50:11 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.64 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:08:48 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:47:12 (Lima), es decir **1.64 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:08:21+00:00` | `2026-04-12 21:08:21 (Lima)` | -0.01h |
| 1 | VENTURA VILLANUEVA evelio FIR 10221537 sw b2c54e08b2d264aa32dce57124119e439c929f28 | 10221537 | `2026-04-13T03:47:12+00:00` | `2026-04-12 22:47:12 (Lima)` | +1.64h |
| 2 | VILLA PALACIOS sabrina Alexandra FIR 46410122 sw 7300e006000cd4caf0c144e7a8facac07a0d07fb | 46410122 | `2026-04-13T03:48:25+00:00` | `2026-04-12 22:48:25 (Lima)` | +1.66h |
| 3 | VILLAFANA OTAROLA flor De Maria FIR 10063992 sw 5fa8a93a57318767b1a74851a12e47b1ef23af44 | 10063992 | `2026-04-13T03:49:27+00:00` | `2026-04-12 22:49:27 (Lima)` | +1.68h |
| 4 | LLALLICO QUISPE paola Jessica FIR 70277707 sw 64a2d6118555e47fec871a6ec8752856ba813aa4 | 70277707 | `2026-04-13T03:50:11+00:00` | `2026-04-12 22:50:11 (Lima)` | +1.69h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **043349**
2. Descargar el PDF del acta
3. Verificar SHA-256: `375b2db7266e7862766a22cbfb6525bfa9dd5ddf3fe0ab8249d625e6b053220c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
