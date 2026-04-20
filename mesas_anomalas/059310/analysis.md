# Mesa 059310 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.571659+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN BORJA
- **Local de votación**: IEP AMADO DE DIOS - PRIMARIA (código 53289)
- **Ubigeo**: 140140

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 231
- Votos válidos: 222
- Participación: 77.258%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:39:16+00:00` | `2026-04-12 20:39:16 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:39:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:39:16+00:00` | `2026-04-12 20:39:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:13:53+00:00` | `2026-04-12 23:13:53 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:14:50+00:00` | `2026-04-12 23:14:50 (Lima)` |
| Última firma humana | `2026-04-13T04:18:38+00:00` | `2026-04-12 23:18:38 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.59 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:39:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:14:50 (Lima), es decir **2.59 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:39:13+00:00` | `2026-04-12 20:39:13 (Lima)` | -0.00h |
| 1 | PATRON HEREDIA cesar Enrique FIR 07969398 sw 61953b85923e2ed625bf275603b7482ca3a12f1d | 07969398 | `2026-04-13T04:14:50+00:00` | `2026-04-12 23:14:50 (Lima)` | +2.59h |
| 2 | PASQUEL VILCARROMERO francisco Yafet FIR 09672141 sw e17a98b767fe941f08a8c0147ad55051a88de04e | 09672141 | `2026-04-13T04:17:52+00:00` | `2026-04-12 23:17:52 (Lima)` | +2.64h |
| 3 | QUINTANILLA GALVAN james Franklin FIR 40209410 sw 031ba058c3280ef7caaaf478336bc16a1ddbd1bf | 40209410 | `2026-04-13T04:18:07+00:00` | `2026-04-12 23:18:07 (Lima)` | +2.65h |
| 4 | ALARCON PEREZ sergio FIR 09542496 sw 5605e2be9874b80b74c4542d752c8431f5860320 | 09542496 | `2026-04-13T04:18:38+00:00` | `2026-04-12 23:18:38 (Lima)` | +2.66h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **059310**
2. Descargar el PDF del acta
3. Verificar SHA-256: `776d1879e262b66f647941af2bccf5bf700f1ea361cb66765ba225edb3752cdb`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
