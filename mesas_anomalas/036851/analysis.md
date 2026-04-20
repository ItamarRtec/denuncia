# Mesa 036851 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.776720+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IEP SANTISIMA TRINIDAD (código 34866)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 247
- Votos válidos: 216
- Participación: 82.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:47:47+00:00` | `2026-04-12 21:47:47 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:45:51+00:00` | `2026-04-12 21:45:51 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:47:47+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:47:47+00:00` | `2026-04-12 21:47:47 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:49:48+00:00` | `2026-04-13 07:49:48 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:56:41+00:00` | `2026-04-13 07:56:41 (Lima)` |
| Última firma humana | `2026-04-13T13:03:06+00:00` | `2026-04-13 08:03:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.15 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:47:47 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:56:41 (Lima), es decir **10.15 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:45:46+00:00` | `2026-04-12 21:45:46 (Lima)` | -0.03h |
| 1 | VIZCARDO LANEGRA felipe FIR 76668545 sw 72dde7399f0579136aa062c5a223de1abf3dc38e | 76668545 | `2026-04-13T12:56:41+00:00` | `2026-04-13 07:56:41 (Lima)` | +10.15h |
| 2 | VILLANUEVA ALARCON adriana Lizeth FIR 76599312 sw b1805e539fb1bf8cc3f9dee60405e81328971785 | 76599312 | `2026-04-13T12:59:39+00:00` | `2026-04-13 07:59:39 (Lima)` | +10.20h |
| 3 | VILLANUEVA CAMPOS mabel Rossana FIR 06128775 sw 0b9896b15d08e13e35de376e8314f6da9e2668f0 | 06128775 | `2026-04-13T13:03:06+00:00` | `2026-04-13 08:03:06 (Lima)` | +10.26h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036851**
2. Descargar el PDF del acta
3. Verificar SHA-256: `41bc7f828e83a9827ffbcedc227586f1dd4a7bdc304cb17d5950a4e3d4352360`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
