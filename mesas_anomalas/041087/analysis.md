# Mesa 041087 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.300066+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IE 2026 SIMON BOLIVAR (código 50371)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 271
- Votos válidos: 246
- Participación: 90.635%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:30:34+00:00` | `2026-04-12 21:30:34 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:14:11+00:00` | `2026-04-12 21:14:11 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:30:34+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:30:34+00:00` | `2026-04-12 21:30:34 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T08:27:47+00:00` | `2026-04-13 03:27:47 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T08:28:07+00:00` | `2026-04-13 03:28:07 (Lima)` |
| Última firma humana | `2026-04-13T08:28:36+00:00` | `2026-04-13 03:28:36 (Lima)` |

**Brecha primera firma humana vs publicación:** **+5.96 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:30:34 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 03:28:07 (Lima), es decir **5.96 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:14:08+00:00` | `2026-04-12 21:14:08 (Lima)` | -0.27h |
| 1 | IPENZA VERA david Francisco FIR 09031701 sw 5e1ba5229ba368fd9802802be24cc990f0f81997 | 09031701 | `2026-04-13T08:28:07+00:00` | `2026-04-13 03:28:07 (Lima)` | +5.96h |
| 2 | HERNANDEZ AQUIJE alex Martin FIR 21575356 sw c6e67c1380d0195ecf7edc5e1dd1afb22e6abded | 21575356 | `2026-04-13T08:28:23+00:00` | `2026-04-13 03:28:23 (Lima)` | +5.96h |
| 3 | INCIO VILLEGAS maria Elena FIR 45478042 sw 552feb0b1ae06f567f35947a326bd117f48b19ea | 45478042 | `2026-04-13T08:28:36+00:00` | `2026-04-13 03:28:36 (Lima)` | +5.97h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041087**
2. Descargar el PDF del acta
3. Verificar SHA-256: `41ade26118e9c9d8820bb6ec41cb2da4d325d4301057efeaf8337acc74c63b14`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
