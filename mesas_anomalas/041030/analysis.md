# Mesa 041030 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.378795+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IEP MARIA MONTESSORI STOPPIANI (código 32951)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 201
- Votos válidos: 172
- Participación: 67.224%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:48:50+00:00` | `2026-04-12 20:48:50 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:48:50+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:48:50+00:00` | `2026-04-12 20:48:50 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:12:51+00:00` | `2026-04-13 07:12:51 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:24:29+00:00` | `2026-04-13 07:24:29 (Lima)` |
| Última firma humana | `2026-04-13T12:30:31+00:00` | `2026-04-13 07:30:31 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.59 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:48:50 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:24:29 (Lima), es decir **10.59 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:48:47+00:00` | `2026-04-12 20:48:47 (Lima)` | -0.00h |
| 1 | PECHE MACHAY DE RIOS judith Margarita FIR 48203125 sw 077282cc74135506952fd1752f8ae18cb048c5e6 | 48203125 | `2026-04-13T12:24:29+00:00` | `2026-04-13 07:24:29 (Lima)` | +10.59h |
| 2 | PONCE DE LA CRUZ jose Antonio FIR 80419476 sw 285e1c0651867de7cc2d7111b5029512763877de | 80419476 | `2026-04-13T12:27:58+00:00` | `2026-04-13 07:27:58 (Lima)` | +10.65h |
| 3 | PIMENTEL RUIZ edson FIR 45820080 sw bcd5ee33bd62d8f6c9b7752d83c147437b9b9c7b | 45820080 | `2026-04-13T12:29:12+00:00` | `2026-04-13 07:29:12 (Lima)` | +10.67h |
| 4 | PEREZ RUIZ farid Anselmi FIR 71146360 sw ff510e60af580ad8de49325727b6b3386e6c77d7 | 71146360 | `2026-04-13T12:30:09+00:00` | `2026-04-13 07:30:09 (Lima)` | +10.69h |
| 5 | PORRAS TORRES carmen Rosa FIR 06743004 sw b61c7c1d01974f5438060c59dda6a6194987e42d | 06743004 | `2026-04-13T12:30:31+00:00` | `2026-04-13 07:30:31 (Lima)` | +10.69h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041030**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c4d80abfa944abbd2146ceb54947aca816d4244d31021d25036cb53eee7fb4e3`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
