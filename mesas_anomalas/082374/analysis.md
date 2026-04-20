# Mesa 082374 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.542074+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CALLAO
- **Local de votación**: COMPLEJO DEPORTIVO VALERIANO LÓPEZ (código 54706)
- **Ubigeo**: 240101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 192
- Votos válidos: 167
- Participación: 64.214%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:48:24+00:00` | `2026-04-12 19:48:24 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:48:24+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:48:24+00:00` | `2026-04-12 19:48:24 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:21:58+00:00` | `2026-04-12 21:21:58 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:26:43+00:00` | `2026-04-12 21:26:43 (Lima)` |
| Última firma humana | `2026-04-13T02:27:13+00:00` | `2026-04-12 21:27:13 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.64 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:48:24 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:26:43 (Lima), es decir **1.64 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:48:22+00:00` | `2026-04-12 19:48:22 (Lima)` | -0.00h |
| 1 | GUANILO VARGAS DE TELLO carolina Isabel FIR 16734258 sw b332f114cd7f32a62b2f13c1651e5c32c346747d | 16734258 | `2026-04-13T02:26:43+00:00` | `2026-04-12 21:26:43 (Lima)` | +1.64h |
| 2 | GARCIA ROJAS luis Alberto FIR 25765417 sw d57f16b95e61d28bd11990f30023d17e3655bed1 | 25765417 | `2026-04-13T02:26:56+00:00` | `2026-04-12 21:26:56 (Lima)` | +1.64h |
| 3 | GOMEZ SANTAMARIA linet Marlene FIR 76477491 sw 358103713d99c186d1d4ae66434fdb89f78612e5 | 76477491 | `2026-04-13T02:27:13+00:00` | `2026-04-12 21:27:13 (Lima)` | +1.65h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082374**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c36db686f664eb7008f9a700968bfdf2a476eed789f4c6460805933348bb418f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
