# Mesa 036842 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.000954+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IEP SANTISIMA TRINIDAD (código 34866)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 251
- Votos válidos: 230
- Participación: 83.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:35:00+00:00` | `2026-04-12 21:35:00 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:35:00+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:35:00+00:00` | `2026-04-12 21:35:00 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:54:47+00:00` | `2026-04-13 07:54:47 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:55:15+00:00` | `2026-04-13 07:55:15 (Lima)` |
| Última firma humana | `2026-04-13T12:57:12+00:00` | `2026-04-13 07:57:12 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.34 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:35:00 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:55:15 (Lima), es decir **10.34 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:34:57+00:00` | `2026-04-12 21:34:57 (Lima)` | -0.00h |
| 1 | MORAN CALIXTO luisa Fiorella FIR 75420953 sw 734727d947c5d2204a2d6412eb77d500f3071662 | 75420953 | `2026-04-13T12:55:15+00:00` | `2026-04-13 07:55:15 (Lima)` | +10.34h |
| 2 | MENDEZ ZAPATA aaron Ulises FIR 73769404 sw f62fd636d0debba7bfa52031a2a3501ce5b99615 | 73769404 | `2026-04-13T12:55:43+00:00` | `2026-04-13 07:55:43 (Lima)` | +10.35h |
| 3 | MENDOZA AGUIRRE rosa FIR 31655072 sw 1274b444a9cfe3a6b7472b4c9f5a68f67d1f0fda | 31655072 | `2026-04-13T12:56:16+00:00` | `2026-04-13 07:56:16 (Lima)` | +10.35h |
| 4 | MUJICA ESQUIVEL maria Greta FIR 06042852 sw 238169ec3df7cbe0b09a6a179424c28c0ff54a6d | 06042852 | `2026-04-13T12:57:12+00:00` | `2026-04-13 07:57:12 (Lima)` | +10.37h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036842**
2. Descargar el PDF del acta
3. Verificar SHA-256: `fc526db61384b4c5f18ccbd9e6f7eca688967fe49bc03aa298ae22ea6a34b192`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
