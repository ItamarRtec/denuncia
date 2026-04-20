# Mesa 061993 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.830712+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IEP PATRON SAN ISIDRO DE SANTA ANITA (código 7403)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 247
- Votos válidos: 227
- Participación: 82.609%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:34:11+00:00` | `2026-04-12 21:34:11 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:34:11+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:34:11+00:00` | `2026-04-12 21:34:11 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:52:28+00:00` | `2026-04-12 22:52:28 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:52:43+00:00` | `2026-04-12 22:52:43 (Lima)` |
| Última firma humana | `2026-04-13T03:53:32+00:00` | `2026-04-12 22:53:32 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.31 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:34:11 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:52:43 (Lima), es decir **1.31 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:29:50+00:00` | `2026-04-12 21:29:50 (Lima)` | -0.07h |
| 1 | MONTOYA REYNA gustavo Tobias FIR 09773944 sw 0e015cbab7d21bbba4db0efbaa4fa5d2173d8ef6 | 09773944 | `2026-04-13T03:52:43+00:00` | `2026-04-12 22:52:43 (Lima)` | +1.31h |
| 2 | MONTOYA TANTALEAN mariano FIR 43062631 sw 6f33b5ab1caacbbc40686b15069bf32a0325ee68 | 43062631 | `2026-04-13T03:52:57+00:00` | `2026-04-12 22:52:57 (Lima)` | +1.31h |
| 3 | MATOS ORTEGA edgardo Gil FIR 09882238 sw b5a631d612100584cf82144d455077cb836cf85f | 09882238 | `2026-04-13T03:53:10+00:00` | `2026-04-12 22:53:10 (Lima)` | +1.32h |
| 4 | LAZARO HUAMAN elvis FIR 42961558 sw 6d730fe5ea996ee0da56c8a5c8b8bc80515796da | 42961558 | `2026-04-13T03:53:32+00:00` | `2026-04-12 22:53:32 (Lima)` | +1.32h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061993**
2. Descargar el PDF del acta
3. Verificar SHA-256: `765e9e0e33cfb751fdfa72a8e472cf7cdd2a85cfcf98eaa19e9e894fbc1bbd52`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
