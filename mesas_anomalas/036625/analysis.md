# Mesa 036625 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.235705+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE NUESTRA SEÑORA DE GUADALUPE (código 7380)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 204
- Votos válidos: 187
- Participación: 68.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:16:56+00:00` | `2026-04-12 22:16:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:16:56+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:16:56+00:00` | `2026-04-12 22:16:56 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:30:28+00:00` | `2026-04-13 08:30:28 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:34:13+00:00` | `2026-04-13 08:34:13 (Lima)` |
| Última firma humana | `2026-04-13T13:35:55+00:00` | `2026-04-13 08:35:55 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.29 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:16:56 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:34:13 (Lima), es decir **10.29 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:16:55+00:00` | `2026-04-12 22:16:55 (Lima)` | -0.00h |
| 1 | CASTILLO ROMERO jacqueline Cristina FIR 06268313 sw 63a9b91cfac7847ef5526081dcd5ceeffdfc7f47 | 06268313 | `2026-04-13T13:34:13+00:00` | `2026-04-13 08:34:13 (Lima)` | +10.29h |
| 2 | CASTELLANOS FRITSCHI gladys Edith FIR 25475807 sw c2b4f2246d2acf66c21d7ad080705ea6ea3cabac | 25475807 | `2026-04-13T13:35:22+00:00` | `2026-04-13 08:35:22 (Lima)` | +10.31h |
| 3 | CARRASCO SALAZAR simone Luz FIR 74297593 sw 2e5d5a19532371b825664c27a6bd79ab4fb250a5 | 74297593 | `2026-04-13T13:35:55+00:00` | `2026-04-13 08:35:55 (Lima)` | +10.32h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036625**
2. Descargar el PDF del acta
3. Verificar SHA-256: `0a2796d3df32c3a28e06cb8a6822fa12ae6731f1739631b107502fefd75045bd`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
