# Mesa 036207 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.731419+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE 1150 ABRAHAM ZEA CARREON (código 2655)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 253
- Votos válidos: 226
- Participación: 84.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:13:27+00:00` | `2026-04-12 22:13:27 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:13:27+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:13:27+00:00` | `2026-04-12 22:13:27 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:38:08+00:00` | `2026-04-13 08:38:08 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:38:31+00:00` | `2026-04-13 08:38:31 (Lima)` |
| Última firma humana | `2026-04-13T13:40:09+00:00` | `2026-04-13 08:40:09 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.42 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:13:27 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:38:31 (Lima), es decir **10.42 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:13:25+00:00` | `2026-04-12 22:13:25 (Lima)` | -0.00h |
| 1 | ANTICONA VASQUEZ miguel Esteban FIR 10638086 sw c561357341f70b926388310d0ac9bf77753c84d2 | 10638086 | `2026-04-13T13:38:31+00:00` | `2026-04-13 08:38:31 (Lima)` | +10.42h |
| 2 | ARANA CAMARENA steve Adolfo FIR 46885067 sw 7e16a913be6e562740a82277be974bc947383c2e | 46885067 | `2026-04-13T13:38:50+00:00` | `2026-04-13 08:38:50 (Lima)` | +10.42h |
| 3 | BALDEON DE LA CRUZ carlos Benjamin FIR 40284492 sw 252a997ad2fcefec8491261030141c73155c5e8a | 40284492 | `2026-04-13T13:39:07+00:00` | `2026-04-13 08:39:07 (Lima)` | +10.43h |
| 4 | RAMIREZ MORALES cesar Augusto FIR 08530099 sw caffc7819a60f447210bbf4cc5ee4e07b13c66e5 | 08530099 | `2026-04-13T13:40:09+00:00` | `2026-04-13 08:40:09 (Lima)` | +10.45h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036207**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3efe98c9e7673f13fd1ecdd751f89be304b48abd6a18b99fd1c9429fe09f195b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
