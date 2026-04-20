# Mesa 051689 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.403623+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: CEBE ESPECIAL SURQUILLO (código 3224)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 255
- Votos válidos: 246
- Participación: 85.284%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:22:32+00:00` | `2026-04-12 20:22:32 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:22:32+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:22:32+00:00` | `2026-04-12 20:22:32 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:46:24+00:00` | `2026-04-13 00:46:24 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:46:52+00:00` | `2026-04-13 00:46:52 (Lima)` |
| Última firma humana | `2026-04-13T05:47:24+00:00` | `2026-04-13 00:47:24 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.41 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:22:32 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:46:52 (Lima), es decir **4.41 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:22:30+00:00` | `2026-04-12 20:22:30 (Lima)` | -0.00h |
| 1 | LAMA SALOMON selim Adel FIR 10267160 sw 6fc1dfceb09c45b0fa983d2ba9fbfbae5def5f2f | 10267160 | `2026-04-13T05:46:52+00:00` | `2026-04-13 00:46:52 (Lima)` | +4.41h |
| 2 | LLONTOP MOYA jorge Luis FIR 06990225 sw 0da09490e44f45ae074773754c6fa99b58a741a2 | 06990225 | `2026-04-13T05:47:08+00:00` | `2026-04-13 00:47:08 (Lima)` | +4.41h |
| 3 | LEUNG GRANADOS kai Jong FIR 44120847 sw ca05f8d67919c638dcfcdd223df6cbb2850155d5 | 44120847 | `2026-04-13T05:47:24+00:00` | `2026-04-13 00:47:24 (Lima)` | +4.41h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051689**
2. Descargar el PDF del acta
3. Verificar SHA-256: `b8a66ee76a17c9978503506c1999a71651565832a9cd0b7fb56b603de4dffd10`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
