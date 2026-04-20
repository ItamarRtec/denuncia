# Mesa 042838 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.611790+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA VICTORIA
- **Local de votación**: IE PARROQUIAL REINA DE LAS AMERICAS SECUNDARIA (código 2898)
- **Ubigeo**: 140109

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 248
- Votos válidos: 231
- Participación: 82.943%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:25:13+00:00` | `2026-04-12 22:25:13 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:25:13+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:25:13+00:00` | `2026-04-12 22:25:13 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:50:19+00:00` | `2026-04-13 08:50:19 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:50:33+00:00` | `2026-04-13 08:50:33 (Lima)` |
| Última firma humana | `2026-04-13T13:53:02+00:00` | `2026-04-13 08:53:02 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.42 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:25:13 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:50:33 (Lima), es decir **10.42 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:25:12+00:00` | `2026-04-12 22:25:12 (Lima)` | -0.00h |
| 1 | ATENCIA VILLACORTA raul FIR 46014555 sw 43d7861e6fd233ce1d7dc8be630c1c6bff01033b | 46014555 | `2026-04-13T13:50:33+00:00` | `2026-04-13 08:50:33 (Lima)` | +10.42h |
| 2 | BLAS CASAS federico FIR 20723622 sw 078865f2ae48541a519cbd3f0d1a4662ba6d253b | 20723622 | `2026-04-13T13:51:08+00:00` | `2026-04-13 08:51:08 (Lima)` | +10.43h |
| 3 | BURGA PAREDES claudia Julissa FIR 41706673 sw d51b1314e78ba3db5a744ae012b11097525832af | 41706673 | `2026-04-13T13:53:02+00:00` | `2026-04-13 08:53:02 (Lima)` | +10.46h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042838**
2. Descargar el PDF del acta
3. Verificar SHA-256: `440b0b2db608366cd02ac9c76406facf1fffd6fecd6d68a220a31f981d8289fe`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
