# Mesa 042476 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.581652+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: IEP INNOVA SCHOOLS - CHORRILLOS LOS FAISANES (código 54780)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 238
- Votos válidos: 215
- Participación: 79.599%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:47:29+00:00` | `2026-04-12 20:47:29 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:47:29+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:47:29+00:00` | `2026-04-12 20:47:29 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:34:09+00:00` | `2026-04-13 07:34:09 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:35:12+00:00` | `2026-04-13 07:35:12 (Lima)` |
| Última firma humana | `2026-04-13T12:36:31+00:00` | `2026-04-13 07:36:31 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.80 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:47:29 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:35:12 (Lima), es decir **10.80 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:47:27+00:00` | `2026-04-12 20:47:27 (Lima)` | -0.00h |
| 1 | ZEGARRA OCAMPO juan Manuel FIR 43820805 sw 7b2e3e901fa9860547fafbcb9b523f7be44c6805 | 43820805 | `2026-04-13T12:35:12+00:00` | `2026-04-13 07:35:12 (Lima)` | +10.80h |
| 2 | YABAR RODRIGUEZ angie Genesis FIR 47579521 sw 725b557269619e5a7335d43f23e8afdfe1fa35bc | 47579521 | `2026-04-13T12:35:58+00:00` | `2026-04-13 07:35:58 (Lima)` | +10.81h |
| 3 | YAURI LOZANO gloria Cecilia FIR 10231161 sw 4cd83412b5187d24ae0be5c8222db435573d1a72 | 10231161 | `2026-04-13T12:36:31+00:00` | `2026-04-13 07:36:31 (Lima)` | +10.82h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042476**
2. Descargar el PDF del acta
3. Verificar SHA-256: `394f948a89213c686322f13a6e8a7f80978bcfe9f664dc03c5ec52338e4d14de`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
