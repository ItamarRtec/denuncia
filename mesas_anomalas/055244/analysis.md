# Mesa 055244 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.566271+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 7207 MARISCAL RAMON CASTILLA (código 3371)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 252
- Votos válidos: 223
- Participación: 84.281%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:19:14+00:00` | `2026-04-12 21:19:14 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:19:14+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:19:14+00:00` | `2026-04-12 21:19:14 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:54:52+00:00` | `2026-04-13 08:54:52 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:55:09+00:00` | `2026-04-13 08:55:09 (Lima)` |
| Última firma humana | `2026-04-13T13:55:24+00:00` | `2026-04-13 08:55:24 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.60 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:19:14 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:55:09 (Lima), es decir **11.60 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:19:11+00:00` | `2026-04-12 21:19:11 (Lima)` | -0.00h |
| 1 | QUISPE OSTOS melane Dapfne FIR 71258766 sw 574aeeaa0086c02c9ad21d673bc61e857f0f0d97 | 71258766 | `2026-04-13T13:55:09+00:00` | `2026-04-13 08:55:09 (Lima)` | +11.60h |
| 2 | RAMOS OBLITAS miguel Ricardo FIR 72552611 sw b4cc4c43d0004b8d31922d682597d35f877a2bbc | 72552611 | `2026-04-13T13:55:24+00:00` | `2026-04-13 08:55:24 (Lima)` | +11.60h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055244**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4094100a6abcbcb6020a5933ea3b4b78e6b8ea05c618c81dd3a374a7935f3aee`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
