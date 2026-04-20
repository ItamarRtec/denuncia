# Mesa 055755 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.004000+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IESTP FE Y ALEGRIA 75 (código 27204)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 216
- Votos válidos: 198
- Participación: 72.241%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:50:32+00:00` | `2026-04-12 20:50:32 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:50:32+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:50:32+00:00` | `2026-04-12 20:50:32 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:24:01+00:00` | `2026-04-12 22:24:01 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:24:26+00:00` | `2026-04-12 22:24:26 (Lima)` |
| Última firma humana | `2026-04-13T03:25:15+00:00` | `2026-04-12 22:25:15 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.56 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:50:32 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:24:26 (Lima), es decir **1.56 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:50:30+00:00` | `2026-04-12 20:50:30 (Lima)` | -0.00h |
| 1 | URCIA QUINTANILLA evelyn Jazmin FIR 74909684 sw 1c4c89ea87820ffb3fa1e0aba158087d94fb06ad | 74909684 | `2026-04-13T03:24:26+00:00` | `2026-04-12 22:24:26 (Lima)` | +1.56h |
| 2 | VERDE SALVATIERRA billy William FIR 75345409 sw 1eac1abd0eefebfc758551a88239856fbd66f453 | 75345409 | `2026-04-13T03:24:38+00:00` | `2026-04-12 22:24:38 (Lima)` | +1.57h |
| 3 | ZEGARRA PEREZ paola Esther FIR 44797789 sw 78eb88464a2f03974ace61bd250f72dd12992e51 | 44797789 | `2026-04-13T03:24:49+00:00` | `2026-04-12 22:24:49 (Lima)` | +1.57h |
| 4 | CUCHO CARBAJAL manuel Jose FIR 45905744 sw 1710b8921cff6768429f06516cf1d375d03814cd | 45905744 | `2026-04-13T03:25:15+00:00` | `2026-04-12 22:25:15 (Lima)` | +1.58h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055755**
2. Descargar el PDF del acta
3. Verificar SHA-256: `827fe1d25cb10c3625c2498afb764421ae705df4d6fd94c0bdca333e92924680`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
