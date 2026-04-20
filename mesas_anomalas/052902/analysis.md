# Mesa 052902 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.743279+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IEP FRIEDRICH WOHLER (código 14350)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 234
- Votos válidos: 213
- Participación: 78.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:08:12+00:00` | `2026-04-12 20:08:12 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:08:12+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:08:12+00:00` | `2026-04-12 20:08:12 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:34:39+00:00` | `2026-04-12 21:34:39 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:35:30+00:00` | `2026-04-12 21:35:30 (Lima)` |
| Última firma humana | `2026-04-13T02:35:58+00:00` | `2026-04-12 21:35:58 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.46 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:08:12 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:35:30 (Lima), es decir **1.46 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:08:10+00:00` | `2026-04-12 20:08:10 (Lima)` | -0.00h |
| 1 | ARATOMA DIAZ veronica Tola FIR 41908610 sw 1ad4ac3b794ce8b9e709fad7cc48ad4c976cb274 | 41908610 | `2026-04-13T02:35:30+00:00` | `2026-04-12 21:35:30 (Lima)` | +1.46h |
| 2 | BUTILIER CELESTINO jairo Junior FIR 76673011 sw fb42cb790d454eac853b97e6dec2c51db8931fcb | 76673011 | `2026-04-13T02:35:45+00:00` | `2026-04-12 21:35:45 (Lima)` | +1.46h |
| 3 | BAZAN MALDONADO luis Yordan FIR 42225472 sw e86f2803187d8c553aaf603a4b155eaa1db61cfa | 42225472 | `2026-04-13T02:35:58+00:00` | `2026-04-12 21:35:58 (Lima)` | +1.46h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **052902**
2. Descargar el PDF del acta
3. Verificar SHA-256: `b88a96cdc300a633bf6f9b452ea48804f61af0837d9f07c2422b24d2fbd907d8`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
