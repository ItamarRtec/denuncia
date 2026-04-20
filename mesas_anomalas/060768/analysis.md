# Mesa 060768 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.297870+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LOS OLIVOS
- **Local de votación**: IE 2087 REPUBLICA ORIENTAL DEL URUGUAY (código 3547)
- **Ubigeo**: 140142

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 248
- Votos válidos: 219
- Participación: 82.943%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:45:06+00:00` | `2026-04-12 20:45:06 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:45:06+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:45:06+00:00` | `2026-04-12 20:45:06 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:52:18+00:00` | `2026-04-12 21:52:18 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:53:09+00:00` | `2026-04-12 21:53:09 (Lima)` |
| Última firma humana | `2026-04-13T02:53:52+00:00` | `2026-04-12 21:53:52 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.13 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:45:06 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:53:09 (Lima), es decir **1.13 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:45:04+00:00` | `2026-04-12 20:45:04 (Lima)` | -0.00h |
| 1 | SOLIS ALAYO maria Cristina FIR 71192197 sw 82ed93d9422f373834a985d7bbfa6ab1966925d0 | 71192197 | `2026-04-13T02:53:09+00:00` | `2026-04-12 21:53:09 (Lima)` | +1.13h |
| 2 | TRUJILLO TORRES alberto Mateo FIR 43278808 sw 704f2e44b2e57e0013f78aabf8a847c7919bceeb | 43278808 | `2026-04-13T02:53:23+00:00` | `2026-04-12 21:53:23 (Lima)` | +1.14h |
| 3 | ROJAS OLORTEGUI yanet Pamela FIR 71403400 sw b30dacc256038b1ddbd730ba9ec9f795e786bd89 | 71403400 | `2026-04-13T02:53:52+00:00` | `2026-04-12 21:53:52 (Lima)` | +1.15h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **060768**
2. Descargar el PDF del acta
3. Verificar SHA-256: `469481aa8613759cb8a7c9e6f29f548c676c639782ea658c4caa737c9f736236`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
