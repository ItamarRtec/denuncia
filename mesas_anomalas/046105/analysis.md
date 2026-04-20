# Mesa 046105 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.802215+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUEBLO LIBRE
- **Local de votación**: IDIOMAS PUCP (código 14087)
- **Ubigeo**: 140117

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 238
- Votos válidos: 225
- Participación: 79.599%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:43:48+00:00` | `2026-04-12 20:43:48 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:43:48+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:43:48+00:00` | `2026-04-12 20:43:48 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:01:54+00:00` | `2026-04-13 08:01:54 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:15:49+00:00` | `2026-04-13 08:15:49 (Lima)` |
| Última firma humana | `2026-04-13T13:19:55+00:00` | `2026-04-13 08:19:55 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.53 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:43:48 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:15:49 (Lima), es decir **11.53 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:43:46+00:00` | `2026-04-12 20:43:46 (Lima)` | -0.00h |
| 1 | ULLOA MEDINA carlos Roberto FIR 09626393 sw aef9f9888d6e9c8077a8594a88ecb2615a9c0edb | 09626393 | `2026-04-13T13:15:49+00:00` | `2026-04-13 08:15:49 (Lima)` | +11.53h |
| 2 | VALDEZ CABALLERO moises FIR 40535536 sw 3dd0a92b31101ad64a2e8d258fa87f7ea57529de | 40535536 | `2026-04-13T13:18:01+00:00` | `2026-04-13 08:18:01 (Lima)` | +11.57h |
| 3 | TORRES GUZMAN giovanna Tatiana FIR 06122724 sw 5387be4ca59caee4fcb66958dfdf268ccefd05db | 06122724 | `2026-04-13T13:19:55+00:00` | `2026-04-13 08:19:55 (Lima)` | +11.60h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046105**
2. Descargar el PDF del acta
3. Verificar SHA-256: `45477baf9cf3a7b207f44cf8732860b9e54e67dae6a448aab3156a89186e3421`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
