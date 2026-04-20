# Mesa 043547 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.417333+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA MOLINA
- **Local de votación**: IEP COLEGIO BRUNING (código 50925)
- **Ubigeo**: 140110

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 212
- Votos válidos: 190
- Participación: 70.903%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:36:56+00:00` | `2026-04-12 21:36:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:36:56+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:36:56+00:00` | `2026-04-12 21:36:56 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:16:25+00:00` | `2026-04-13 09:16:25 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:16:56+00:00` | `2026-04-13 09:16:56 (Lima)` |
| Última firma humana | `2026-04-13T14:19:49+00:00` | `2026-04-13 09:19:49 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.67 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:36:56 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:16:56 (Lima), es decir **11.67 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:32:15+00:00` | `2026-04-12 21:32:15 (Lima)` | -0.08h |
| 1 | LOPEZ BENATE augusto Rodrigo FIR 74863218 sw e6d3886c8b3a9bff7bfe53fa37365e53c9aeccaa | 74863218 | `2026-04-13T14:16:56+00:00` | `2026-04-13 09:16:56 (Lima)` | +11.67h |
| 2 | MALDONADO HINOSTROZA gloria Nery FIR 19976872 sw fdef9c2b669965eb134126daef81f426a7c395c9 | 19976872 | `2026-04-13T14:18:44+00:00` | `2026-04-13 09:18:44 (Lima)` | +11.70h |
| 3 | MEGO CHIRINOS aldo FIR 41919005 sw 87b47cb6a9b53341819ce3e9e46dbbabccd3a61f | 41919005 | `2026-04-13T14:19:49+00:00` | `2026-04-13 09:19:49 (Lima)` | +11.71h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **043547**
2. Descargar el PDF del acta
3. Verificar SHA-256: `447af203817b2ee7b4bf6d686259d4c014edb9d8de83701ce0a4a4e0a39100f4`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
