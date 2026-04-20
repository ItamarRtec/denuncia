# Mesa 051913 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.132395+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: ESTADIO MUNICIPAL CARLOS A. MOSCOSO 2 (código 40995)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 224
- Votos válidos: 199
- Participación: 74.916%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:08:37+00:00` | `2026-04-12 21:08:37 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:08:37+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:08:37+00:00` | `2026-04-12 21:08:37 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:42:25+00:00` | `2026-04-12 22:42:25 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:45:51+00:00` | `2026-04-12 22:45:51 (Lima)` |
| Última firma humana | `2026-04-13T03:46:24+00:00` | `2026-04-12 22:46:24 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.62 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:08:37 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:45:51 (Lima), es decir **1.62 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:08:35+00:00` | `2026-04-12 21:08:35 (Lima)` | -0.00h |
| 1 | PALACIOS FLORES marilyn Stefanny FIR 72503950 sw 7a735655686f28868721be5a7930ffb6d3785c21 | 72503950 | `2026-04-13T03:45:51+00:00` | `2026-04-12 22:45:51 (Lima)` | +1.62h |
| 2 | PALACIOS HUERTAS dina Erlinda FIR 16022869 sw f053c13efbbb5713fb2870387e642fd48531979c | 16022869 | `2026-04-13T03:46:24+00:00` | `2026-04-12 22:46:24 (Lima)` | +1.63h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051913**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4b7273083418e0daf6e28d0a4dd4216aaaced523c9ec07fff5b37e1c1e929ebf`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
