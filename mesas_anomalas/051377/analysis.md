# Mesa 051377 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.491466+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IEP INNOVA SCHOOLS SURCO - AMBROSIO (código 52886)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 224
- Votos válidos: 212
- Participación: 74.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:54:13+00:00` | `2026-04-12 20:54:13 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:54:13+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:54:13+00:00` | `2026-04-12 20:54:13 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:56:49+00:00` | `2026-04-13 00:56:49 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:57:09+00:00` | `2026-04-13 00:57:09 (Lima)` |
| Última firma humana | `2026-04-13T05:58:13+00:00` | `2026-04-13 00:58:13 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.05 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:54:13 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:57:09 (Lima), es decir **4.05 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:54:11+00:00` | `2026-04-12 20:54:11 (Lima)` | -0.00h |
| 1 | FIGUEROLA DUTHURBURU kenneth Lucius Marvin FIR 09541775 sw 6d7285c404e4b396d37ce103ae45fde6e5af033e | 09541775 | `2026-04-13T05:57:09+00:00` | `2026-04-13 00:57:09 (Lima)` | +4.05h |
| 2 | FLORES HUAYNA patricia Marlene FIR 25701237 sw eebc5152e3a091f825933b820c8c42f3cd8e7813 | 25701237 | `2026-04-13T05:57:47+00:00` | `2026-04-13 00:57:47 (Lima)` | +4.06h |
| 3 | FALCON DAMIANO alex Eduardo FIR 45313222 sw e79dd35ce57f2f8c16d17025e213e499bead1b61 | 45313222 | `2026-04-13T05:58:13+00:00` | `2026-04-13 00:58:13 (Lima)` | +4.07h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051377**
2. Descargar el PDF del acta
3. Verificar SHA-256: `dcb6001c7c70a860ddc70224ad0f0076a81cded33506d0d82b7bf33d37ae4231`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
