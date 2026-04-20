# Mesa 045036 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.717275+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: IE 7003 MANUEL FERNANDO BONILLA (código 2982)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 236
- Votos válidos: 218
- Participación: 78.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:57:59+00:00` | `2026-04-12 20:57:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:57:59+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:57:59+00:00` | `2026-04-12 20:57:59 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:42:19+00:00` | `2026-04-12 23:42:19 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:42:40+00:00` | `2026-04-12 23:42:40 (Lima)` |
| Última firma humana | `2026-04-13T04:43:06+00:00` | `2026-04-12 23:43:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.74 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:57:59 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:42:40 (Lima), es decir **2.74 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:57:57+00:00` | `2026-04-12 20:57:57 (Lima)` | -0.00h |
| 1 | DELLEPIANI MENDOZA italo Fabrizio FIR 76880348 sw 01eb0b71f98edabb716732beedc63ca340cadeeb | 76880348 | `2026-04-13T04:42:40+00:00` | `2026-04-12 23:42:40 (Lima)` | +2.74h |
| 2 | ESPANTOSO NEYRA DE FITTS maria Linda FIR 08256486 sw db59c26f88142c476841480cf8b15e2a40ae1311 | 08256486 | `2026-04-13T04:42:54+00:00` | `2026-04-12 23:42:54 (Lima)` | +2.75h |
| 3 | DAVILA PALACIOS carlos Oswaldo FIR 41810982 sw 7452b1636bbdf51b8b286554108ef6e32573ebdc | 41810982 | `2026-04-13T04:43:06+00:00` | `2026-04-12 23:43:06 (Lima)` | +2.75h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045036**
2. Descargar el PDF del acta
3. Verificar SHA-256: `eba371b3dfbe636fe1548c75bcaf25e05b3ab75ffa5d2ac37ec1084b5e796b01`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
