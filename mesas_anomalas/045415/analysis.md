# Mesa 045415 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.593122+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: PARQUE JOHN F KENNEDY (código 54877)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 297
- Votos emitidos: 206
- Votos válidos: 189
- Participación: 69.36%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:16:16+00:00` | `2026-04-12 19:16:16 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:16:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:16:16+00:00` | `2026-04-12 19:16:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:04:08+00:00` | `2026-04-12 22:04:08 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:04:19+00:00` | `2026-04-12 22:04:19 (Lima)` |
| Última firma humana | `2026-04-13T03:05:10+00:00` | `2026-04-12 22:05:10 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.80 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:16:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:04:19 (Lima), es decir **2.80 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:16:14+00:00` | `2026-04-12 19:16:14 (Lima)` | -0.00h |
| 1 | TATAJE ESCALANTE cesar Alberto FIR 09555226 sw 30e689ca2abdd2693fdeb15ab8d9cf3e6c62092a | 09555226 | `2026-04-13T03:04:19+00:00` | `2026-04-12 22:04:19 (Lima)` | +2.80h |
| 2 | TAVARA MEDINA oscar Gabriel FIR 71145463 sw 2388bedb09f7d38c9b524a53016c3d8bbf2b13a8 | 71145463 | `2026-04-13T03:04:31+00:00` | `2026-04-12 22:04:31 (Lima)` | +2.80h |
| 3 | TIRADO RODRIGUEZ alexis Silvana FIR 07870173 sw 6e8d321e835d657f59238c6ce3856622b01e8fbf | 07870173 | `2026-04-13T03:04:44+00:00` | `2026-04-12 22:04:44 (Lima)` | +2.81h |
| 4 | SANCHEZ MAIZONDO eduardo Moises FIR 08762800 sw c841c55dc109d53e8d95a19777ee3b052e47b610 | 08762800 | `2026-04-13T03:05:00+00:00` | `2026-04-12 22:05:00 (Lima)` | +2.81h |
| 5 | COYLA MORA adriana Nicole FIR 74774695 sw 32c2c654e3c13668faed37e6587724939fbdd348 | 74774695 | `2026-04-13T03:05:10+00:00` | `2026-04-12 22:05:10 (Lima)` | +2.81h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045415**
2. Descargar el PDF del acta
3. Verificar SHA-256: `285f014ccedd7d138e56d1cf6ca845cd145e0d96115de77921f81cde11b628b4`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
