# Mesa 062089 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.258247+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IEP SAN LUIS GONZAGA (código 32227)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 255
- Votos válidos: 223
- Participación: 85.284%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:04:29+00:00` | `2026-04-12 21:04:29 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:04:29+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:04:29+00:00` | `2026-04-12 21:04:29 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:41:21+00:00` | `2026-04-13 00:41:21 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:41:48+00:00` | `2026-04-13 00:41:48 (Lima)` |
| Última firma humana | `2026-04-13T05:42:19+00:00` | `2026-04-13 00:42:19 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.62 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:04:29 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:41:48 (Lima), es decir **3.62 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:04:26+00:00` | `2026-04-12 21:04:26 (Lima)` | -0.00h |
| 1 | VILLANUEVA SIMBRON DE BERRIOS cecilia Berloz FIR 07970657 sw 9a9eb69aa0671e5b5ef6bf1495c94390aa2abacd | 07970657 | `2026-04-13T05:41:48+00:00` | `2026-04-13 00:41:48 (Lima)` | +3.62h |
| 2 | ZAPATA AREVALO digna Zobeida FIR 01161527 sw 14e9078ee79645f1505a07ba9f4397872e603a04 | 01161527 | `2026-04-13T05:42:08+00:00` | `2026-04-13 00:42:08 (Lima)` | +3.63h |
| 3 | VARGAS ACOSTA yoselyn Karen FIR 75330038 sw a9d66ff41ab947aa6bf85ee9fa57d9bcfc5b389c | 75330038 | `2026-04-13T05:42:19+00:00` | `2026-04-13 00:42:19 (Lima)` | +3.63h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **062089**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3f755c999c8a05bb608aa0f354d4c36e83b607e94e4641188600317ad62e7267`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
