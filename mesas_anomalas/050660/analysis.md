# Mesa 050660 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.591324+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IE 7058 MARIA DE FATIMA (código 3201)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 254
- Votos válidos: 236
- Participación: 84.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:56:50+00:00` | `2026-04-12 19:56:50 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:56:50+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:56:50+00:00` | `2026-04-12 19:56:50 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:31:26+00:00` | `2026-04-13 00:31:26 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:31:43+00:00` | `2026-04-13 00:31:43 (Lima)` |
| Última firma humana | `2026-04-13T05:32:15+00:00` | `2026-04-13 00:32:15 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.58 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:56:50 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:31:43 (Lima), es decir **4.58 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:56:48+00:00` | `2026-04-12 19:56:48 (Lima)` | -0.00h |
| 1 | IZURIETA MANRIQUE daphnee Grace FIR 29664229 sw 546d44feec0e95126097827138e035c9c817b10e | 29664229 | `2026-04-13T05:31:43+00:00` | `2026-04-13 00:31:43 (Lima)` | +4.58h |
| 2 | LOPEZ HUAMAN edwin Abdias FIR 76159141 sw 128aea166d482c834dfaac3aefa6f3de34aec8bb | 76159141 | `2026-04-13T05:31:58+00:00` | `2026-04-13 00:31:58 (Lima)` | +4.59h |
| 3 | LA TORRE CORDOVA elizabeth Aurora FIR 29560352 sw 0600118fc40cc21fced0763eac650359dd6f3a0e | 29560352 | `2026-04-13T05:32:15+00:00` | `2026-04-13 00:32:15 (Lima)` | +4.59h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050660**
2. Descargar el PDF del acta
3. Verificar SHA-256: `45e16abb3ad755586f8f2b14fff5792d6b1edc6e6e66e9e37ddbedf2318e4bf0`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
