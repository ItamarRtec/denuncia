# Mesa 083047 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.654303+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: LA PERLA
- **Local de votación**: LOCAL DE EDUCACION CULTURA Y DEPORTE (código 54269)
- **Ubigeo**: 240105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 232
- Votos válidos: 211
- Participación: 77.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:45:43+00:00` | `2026-04-12 20:45:43 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:45:43+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:45:43+00:00` | `2026-04-12 20:45:43 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:14:18+00:00` | `2026-04-12 23:14:18 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:14:31+00:00` | `2026-04-12 23:14:31 (Lima)` |
| Última firma humana | `2026-04-13T04:15:04+00:00` | `2026-04-12 23:15:04 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.48 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:45:43 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:14:31 (Lima), es decir **2.48 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:45:41+00:00` | `2026-04-12 20:45:41 (Lima)` | -0.00h |
| 1 | GUTIERREZ INGA vanessa FIR 47468834 sw daca0a5099bb4d620cbf020796c6ca494dbaf27c | 47468834 | `2026-04-13T04:14:31+00:00` | `2026-04-12 23:14:31 (Lima)` | +2.48h |
| 2 | GUTIERREZ SAENZ carlos Antonio FIR 09255936 sw 5fdb3b5019215259118fb41509839d1d0b09feb2 | 09255936 | `2026-04-13T04:14:51+00:00` | `2026-04-12 23:14:51 (Lima)` | +2.49h |
| 3 | GUERRA GOMEZ rosana Milagros FIR 08718354 sw 8b9b612ac2ddfd5aaac68f3e6a3177d1cd18f444 | 08718354 | `2026-04-13T04:15:04+00:00` | `2026-04-12 23:15:04 (Lima)` | +2.49h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083047**
2. Descargar el PDF del acta
3. Verificar SHA-256: `600c18945d61f03b788b4ef3a1d1b6b95611aba48addf3f229084a9f3edc5a9c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
