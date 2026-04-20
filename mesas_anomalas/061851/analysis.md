# Mesa 061851 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.870418+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IEP ALFONSO UGARTE (código 3592)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 241
- Votos válidos: 224
- Participación: 80.602%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:13:24+00:00` | `2026-04-12 21:13:24 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:13:24+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:13:24+00:00` | `2026-04-12 21:13:24 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:36:13+00:00` | `2026-04-12 22:36:13 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:36:42+00:00` | `2026-04-12 22:36:42 (Lima)` |
| Última firma humana | `2026-04-13T03:37:23+00:00` | `2026-04-12 22:37:23 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.39 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:13:24 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:36:42 (Lima), es decir **1.39 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:12:26+00:00` | `2026-04-12 21:12:26 (Lima)` | -0.02h |
| 1 | ROMERO BRUNO veronica Alejandrina FIR 44006922 sw fb939e4591e6090500936287c07e5c2296944b30 | 44006922 | `2026-04-13T03:36:42+00:00` | `2026-04-12 22:36:42 (Lima)` | +1.39h |
| 2 | ROMERO NAJARRO wilber FIR 44903788 sw 53333f9098e157cff5a135e498aeffc54220b460 | 44903788 | `2026-04-13T03:36:59+00:00` | `2026-04-12 22:36:59 (Lima)` | +1.39h |
| 3 | SALAS MALPARTIDA alex Joel FIR 07045203 sw 00508d3b526747fa97a85579fd710a38c13a6484 | 07045203 | `2026-04-13T03:37:23+00:00` | `2026-04-12 22:37:23 (Lima)` | +1.40h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061851**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c10285618693766122dfe4073ed990b85fc8f92feb3fb7d6ab8498cd63d38100`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
