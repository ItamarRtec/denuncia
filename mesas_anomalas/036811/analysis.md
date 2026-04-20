# Mesa 036811 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.653179+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE ARGENTINA (código 32206)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 224
- Votos válidos: 200
- Participación: 74.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:43:25+00:00` | `2026-04-12 20:43:25 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:43:25+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:43:25+00:00` | `2026-04-12 20:43:25 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:26:41+00:00` | `2026-04-13 07:26:41 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:27:08+00:00` | `2026-04-13 07:27:08 (Lima)` |
| Última firma humana | `2026-04-13T12:27:35+00:00` | `2026-04-13 07:27:35 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.73 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:43:25 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:27:08 (Lima), es decir **10.73 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:43:23+00:00` | `2026-04-12 20:43:23 (Lima)` | -0.00h |
| 1 | BABILONIA HUERTA mariclaire Vivian FIR 73043577 sw fae3cba21ac21d246fd25b055badf46cf1ee1f25 | 73043577 | `2026-04-13T12:27:08+00:00` | `2026-04-13 07:27:08 (Lima)` | +10.73h |
| 2 | AYLAS LANDA diana Candy FIR 70852690 sw 3596c8abaf901defa15d6b9be217149df4b7347e | 70852690 | `2026-04-13T12:27:24+00:00` | `2026-04-13 07:27:24 (Lima)` | +10.73h |
| 3 | BOCZ SALAZAR antonia Lizet FIR 62643449 sw 3cc9ca22515155ee64173129417b7f449363f607 | 62643449 | `2026-04-13T12:27:35+00:00` | `2026-04-13 07:27:35 (Lima)` | +10.74h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036811**
2. Descargar el PDF del acta
3. Verificar SHA-256: `0d4bbec5ee6dcdebcdd9cb721257381586baf81265dd521f9717e7227cb1a7a6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
