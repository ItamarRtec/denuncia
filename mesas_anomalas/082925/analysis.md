# Mesa 082925 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.630678+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: LA PERLA
- **Local de votación**: IE PARROQUIAL SAN JOSE (código 4854)
- **Ubigeo**: 240105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 283
- Votos válidos: 262
- Participación: 94.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:37:43+00:00` | `2026-04-12 22:37:43 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:37:43+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:37:43+00:00` | `2026-04-12 22:37:43 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T15:02:00+00:00` | `2026-04-13 10:02:00 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T15:02:16+00:00` | `2026-04-13 10:02:16 (Lima)` |
| Última firma humana | `2026-04-13T15:04:20+00:00` | `2026-04-13 10:04:20 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.41 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:37:43 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 10:02:16 (Lima), es decir **11.41 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:37:42+00:00` | `2026-04-12 22:37:42 (Lima)` | -0.00h |
| 1 | DIAZ PUCCIO carmen Juana FIR 25779483 sw 809c6428e370db95d82448261a9451627acb82a3 | 25779483 | `2026-04-13T15:02:16+00:00` | `2026-04-13 10:02:16 (Lima)` | +11.41h |
| 2 | ESQUERRE GUEVARA maria Cristina FIR 02778735 sw 4bb176f5e9de3f9a47c8b1cc0e2300dd57be4240 | 02778735 | `2026-04-13T15:02:55+00:00` | `2026-04-13 10:02:55 (Lima)` | +11.42h |
| 3 | COMPALLE ALVITES flor De Maria FIR 06101955 sw e74742fb1b4dd901f55e1628c80d9cf287e186d3 | 06101955 | `2026-04-13T15:03:12+00:00` | `2026-04-13 10:03:12 (Lima)` | +11.42h |
| 4 | AVILA PAREDES gino Alberto FIR 25766544 sw b832c5559475dca1b9ca6a4904a38af9180cdb8e | 25766544 | `2026-04-13T15:03:49+00:00` | `2026-04-13 10:03:49 (Lima)` | +11.44h |
| 5 | LOPEZ RAMOS maria Antonieta FIR 70833432 sw 9bffcc8d41d017598c75a69e113e65188a51d8bf | 70833432 | `2026-04-13T15:04:20+00:00` | `2026-04-13 10:04:20 (Lima)` | +11.44h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082925**
2. Descargar el PDF del acta
3. Verificar SHA-256: `fc544fc1569e23862f0f7821a6048fc9e8f11df4efaeaf4e5c0344043ec68d4e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
