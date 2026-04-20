# Mesa 045697 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.576109+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PACHACÁMAC
- **Local de votación**: IEP SEÑOR DE LA ASCENSION (código 13538)
- **Ubigeo**: 140116

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 243
- Votos válidos: 201
- Participación: 81.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:04:19+00:00` | `2026-04-12 21:04:19 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:04:19+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:04:19+00:00` | `2026-04-12 21:04:19 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:20:48+00:00` | `2026-04-13 00:20:48 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:21:18+00:00` | `2026-04-13 00:21:18 (Lima)` |
| Última firma humana | `2026-04-13T05:21:46+00:00` | `2026-04-13 00:21:46 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.28 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:04:19 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:21:18 (Lima), es decir **3.28 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:03:44+00:00` | `2026-04-12 21:03:44 (Lima)` | -0.01h |
| 1 | VILCA BAUTISTA diego D'alessandro FIR 61148542 sw 9adde0d373953103fa2addb93fea3d608e674963 | 61148542 | `2026-04-13T05:21:18+00:00` | `2026-04-13 00:21:18 (Lima)` | +3.28h |
| 2 | ZEVALLOS CALDERON edgar Demetrio FIR 10595998 sw 4987499fb27fc0f4349a26403304221fe7517bf3 | 10595998 | `2026-04-13T05:21:30+00:00` | `2026-04-13 00:21:30 (Lima)` | +3.29h |
| 3 | ZEGOVIA ROJAS gladis Angelica FIR 09744904 sw c51090e5e27a88f444967797185ff3a03aade1ae | 09744904 | `2026-04-13T05:21:46+00:00` | `2026-04-13 00:21:46 (Lima)` | +3.29h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045697**
2. Descargar el PDF del acta
3. Verificar SHA-256: `75a2d25f239e0ba75cbcea5e5164efc69d9edb9e21952deba02ebb5660f95ddb`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
