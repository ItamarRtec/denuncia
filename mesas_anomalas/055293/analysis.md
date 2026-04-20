# Mesa 055293 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.954426+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE DE ACCION CONJUNTA PADRE ILUMINATO (código 3375)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 238
- Votos válidos: 205
- Participación: 79.599%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:11:12+00:00` | `2026-04-12 22:11:12 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:11:12+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:11:12+00:00` | `2026-04-12 22:11:12 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:33:19+00:00` | `2026-04-13 09:33:19 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:33:59+00:00` | `2026-04-13 09:33:59 (Lima)` |
| Última firma humana | `2026-04-13T14:34:48+00:00` | `2026-04-13 09:34:48 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.38 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:11:12 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:33:59 (Lima), es decir **11.38 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:11:11+00:00` | `2026-04-12 22:11:11 (Lima)` | -0.00h |
| 1 | HUACHACA LAPA aereopajita FIR 41984350 sw f1c4d24242e2d4f36316a18b44285122aa979b23 | 41984350 | `2026-04-13T14:33:59+00:00` | `2026-04-13 09:33:59 (Lima)` | +11.38h |
| 2 | HUAMAN CCOICCA marco Antonio FIR 10483732 sw 4228497faa19d6e829146187d90a345c18d3b7b3 | 10483732 | `2026-04-13T14:34:30+00:00` | `2026-04-13 09:34:30 (Lima)` | +11.39h |
| 3 | HUANACO PALOMINO flor Constantina FIR 10643971 sw 0672270959db53518bb974988ac85cda2705e138 | 10643971 | `2026-04-13T14:34:48+00:00` | `2026-04-13 09:34:48 (Lima)` | +11.39h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055293**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8b81ed448b52c21aa45be7be1e2b9e5119917882014cc5d9ac38a8f35eb56cac`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
