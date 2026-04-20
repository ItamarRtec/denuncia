# Mesa 045350 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.290911+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: UNIVERSIDAD NACIONAL FEDERICO VILLARREAL SEDE LOCAL 05 (código 54289)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 276
- Votos válidos: 271
- Participación: 92.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:55:00+00:00` | `2026-04-12 19:55:00 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:55:00+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:55:00+00:00` | `2026-04-12 19:55:00 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:11:24+00:00` | `2026-04-12 22:11:24 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:12:06+00:00` | `2026-04-12 22:12:06 (Lima)` |
| Última firma humana | `2026-04-13T03:13:38+00:00` | `2026-04-12 22:13:38 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.29 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:55:00 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:12:06 (Lima), es decir **2.29 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:54:58+00:00` | `2026-04-12 19:54:58 (Lima)` | -0.00h |
| 1 | OLAECHEA PEREA ursula Maria FIR 07869641 sw e116952fb83ca75c735d9d860b9eec07bcd77356 | 07869641 | `2026-04-13T03:12:06+00:00` | `2026-04-12 22:12:06 (Lima)` | +2.29h |
| 2 | MORON DE LA TORRE gustavo Jorge Luis FIR 22093320 sw 1a33a1de1c8a28eac24d34205f2a09a2c94d7ae0 | 22093320 | `2026-04-13T03:12:22+00:00` | `2026-04-12 22:12:22 (Lima)` | +2.29h |
| 3 | MESIA SANCHEZ selva Del Rocio FIR 18085194 sw 5ae4604597033e2d75d3b37a3c945afcca7819c6 | 18085194 | `2026-04-13T03:12:34+00:00` | `2026-04-12 22:12:34 (Lima)` | +2.29h |
| 4 | MARROQUIN CALDERON DE SMITH patricia FIR 07773837 sw 8e6dd14d89092434356ae9860496a201bb820c90 | 07773837 | `2026-04-13T03:13:02+00:00` | `2026-04-12 22:13:02 (Lima)` | +2.30h |
| 5 | ALIAGA VIDAL julio Ernesto FIR 06394553 sw 740bc526a7caaa1a8cf95eed474933b160a5b68b | 06394553 | `2026-04-13T03:13:38+00:00` | `2026-04-12 22:13:38 (Lima)` | +2.31h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045350**
2. Descargar el PDF del acta
3. Verificar SHA-256: `db08ee470d9a54579d8d85222fe7344c571c98835b1c0a753d3f84607b4e2cc9`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
