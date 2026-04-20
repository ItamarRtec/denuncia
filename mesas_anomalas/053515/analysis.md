# Mesa 053515 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.796551+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: JESÚS MARÍA
- **Local de votación**: CONCHA ACUSTICA DEL CAMPO DE MARTE (código 32536)
- **Ubigeo**: 140133

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 232
- Votos válidos: 209
- Participación: 77.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:04:58+00:00` | `2026-04-12 20:04:58 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:04:58+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:04:58+00:00` | `2026-04-12 20:04:58 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:24:55+00:00` | `2026-04-12 22:24:55 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:25:42+00:00` | `2026-04-12 22:25:42 (Lima)` |
| Última firma humana | `2026-04-13T03:25:42+00:00` | `2026-04-12 22:25:42 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.35 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:04:58 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:25:42 (Lima), es decir **2.35 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:04:56+00:00` | `2026-04-12 20:04:56 (Lima)` | -0.00h |
| 1 | VISURRAGA LOPEZ roberto Carlos FIR 08138489 sw e48a230d4cca6ba9605cca2992c5816476cad3d2 | 08138489 | `2026-04-13T03:25:42+00:00` | `2026-04-12 22:25:42 (Lima)` | +2.35h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **053515**
2. Descargar el PDF del acta
3. Verificar SHA-256: `969c28eb55cd09adb1846e8751f897dc98453f5fbd95d11314d3dcfdea829b65`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **1** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
