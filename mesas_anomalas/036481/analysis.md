# Mesa 036481 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.275408+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: UNIVERSIDAD NACIONAL MAYOR DE SAN MARCOS (código 2674)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 205
- Votos válidos: 176
- Participación: 68.562%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:42:05+00:00` | `2026-04-12 21:42:05 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:42:05+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:42:05+00:00` | `2026-04-12 21:42:05 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:30:10+00:00` | `2026-04-13 08:30:10 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:30:28+00:00` | `2026-04-13 08:30:28 (Lima)` |
| Última firma humana | `2026-04-13T13:30:48+00:00` | `2026-04-13 08:30:48 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.81 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:42:05 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:30:28 (Lima), es decir **10.81 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:40:01+00:00` | `2026-04-12 21:40:01 (Lima)` | -0.03h |
| 1 | RONDO ARMAS daisy Ibonne FIR 42112119 sw 881463b6a72770eb22564f71fc33ce5602d30d7b | 42112119 | `2026-04-13T13:30:28+00:00` | `2026-04-13 08:30:28 (Lima)` | +10.81h |
| 2 | ROQUE CONTRERAS juan Luis FIR 07683316 sw 61fcd536d77725ac6d8a6b073ffa8bd5921b96d5 | 07683316 | `2026-04-13T13:30:39+00:00` | `2026-04-13 08:30:39 (Lima)` | +10.81h |
| 3 | ROJAS VARGAS miguel Angel FIR 09960475 sw afa37856d98504d90e826293a4674fe822f30e9e | 09960475 | `2026-04-13T13:30:48+00:00` | `2026-04-13 08:30:48 (Lima)` | +10.81h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036481**
2. Descargar el PDF del acta
3. Verificar SHA-256: `565fdbf207a47779d7d5ef512a0974af42ca8da51451949aa78b471914f108b9`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
