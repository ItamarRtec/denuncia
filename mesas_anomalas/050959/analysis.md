# Mesa 050959 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.483555+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: UNIVERSIDAD MARCELINO CHAMPAGNAT (código 3220)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 278
- Votos válidos: 272
- Participación: 92.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:10:16+00:00` | `2026-04-12 21:10:16 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:10:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:10:16+00:00` | `2026-04-12 21:10:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:35:28+00:00` | `2026-04-13 07:35:28 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:36:14+00:00` | `2026-04-13 07:36:14 (Lima)` |
| Última firma humana | `2026-04-13T12:37:16+00:00` | `2026-04-13 07:37:16 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.43 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:10:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:36:14 (Lima), es decir **10.43 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:10:09+00:00` | `2026-04-12 21:10:09 (Lima)` | -0.00h |
| 1 | ROBLES GAMARRA gretty Patricia FIR 31665524 sw f9a27f5a1255a51e3b015dfdb04882e86512e358 | 31665524 | `2026-04-13T12:36:14+00:00` | `2026-04-13 07:36:14 (Lima)` | +10.43h |
| 2 | RODRIGUEZ ANTEZANA alfredo Javier FIR 43391628 sw bc33888ac753afff8349d62304cfbefb5f46299d | 43391628 | `2026-04-13T12:36:53+00:00` | `2026-04-13 07:36:53 (Lima)` | +10.44h |
| 3 | ROJAS LOPEZ gisella FIR 45478607 sw 67c6fb34bfdf170ca05825a09a7e63493158e654 | 45478607 | `2026-04-13T12:37:16+00:00` | `2026-04-13 07:37:16 (Lima)` | +10.45h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050959**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e1710f664bcabfdffee7f67df4160dd5bbcbd3832b5c2d906943b5ee1b2d9bef`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
