# Mesa 082788 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.690137+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CARMEN DE LA LEGUA - REYNOSO
- **Local de votación**: IE RAUL PORRAS BARRENECHEA (código 4840)
- **Ubigeo**: 240104

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 290
- Votos emitidos: 245
- Votos válidos: 215
- Participación: 84.483%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:31:17+00:00` | `2026-04-12 20:31:17 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:31:17+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:31:17+00:00` | `2026-04-12 20:31:17 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:40:55+00:00` | `2026-04-12 21:40:55 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:41:10+00:00` | `2026-04-12 21:41:10 (Lima)` |
| Última firma humana | `2026-04-13T02:44:26+00:00` | `2026-04-12 21:44:26 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.16 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:31:17 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:41:10 (Lima), es decir **1.16 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:31:14+00:00` | `2026-04-12 20:31:14 (Lima)` | -0.00h |
| 1 | URQUIZA HUAMANCULI carmen Marcela FIR 41944180 sw ed0811a5e90a4f6f9863ba0ac4c74fa008ad1280 | 41944180 | `2026-04-13T02:41:10+00:00` | `2026-04-12 21:41:10 (Lima)` | +1.16h |
| 2 | TRILLO MARTINEZ consuelo Marina FIR 00229556 sw d464f1b960a5de31bb00b26c582f12e26da1a7ea | 00229556 | `2026-04-13T02:41:32+00:00` | `2026-04-12 21:41:32 (Lima)` | +1.17h |
| 3 | TUESTA TRIGOSO josue Elmer FIR 76214137 sw c92c8377d30a36a54c1e28db56f0e08bafa84620 | 76214137 | `2026-04-13T02:41:45+00:00` | `2026-04-12 21:41:45 (Lima)` | +1.17h |
| 4 | FABIAN MALLQUI ketty FIR 72931784 sw 74a7ba58ecd43993aa4029a0a4aae2ee07d87506 | 72931784 | `2026-04-13T02:43:02+00:00` | `2026-04-12 21:43:02 (Lima)` | +1.20h |
| 5 | MIRANDA URBANO raul Carlos FIR 25795562 sw 41a130b45a1728b92b4520134da13013f1b1c36e | 25795562 | `2026-04-13T02:43:39+00:00` | `2026-04-12 21:43:39 (Lima)` | +1.21h |
| 6 | SALCEDO CHINCHAY thalia Mercedes FIR 60795660 sw 2c74e27f33a0b27403402bea74f194f286c3f147 | 60795660 | `2026-04-13T02:44:01+00:00` | `2026-04-12 21:44:01 (Lima)` | +1.21h |
| 7 | RAMOS BLAS doris Violeta FIR 25643273 sw 80e42a34689ba000d1cba53965c81721ca5c7470 | 25643273 | `2026-04-13T02:44:26+00:00` | `2026-04-12 21:44:26 (Lima)` | +1.22h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082788**
2. Descargar el PDF del acta
3. Verificar SHA-256: `34bbd22762b040598f75ebcf1d877b2f45e12b2ee84ac51468f0e5c564562d77`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **7** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
