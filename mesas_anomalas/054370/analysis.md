# Mesa 054370 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.793182+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: EL AGUSTINO
- **Local de votación**: IE 1045 NUESTRA SEÑORA DE FATIMA (código 3329)
- **Ubigeo**: 140135

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 230
- Votos emitidos: 171
- Votos válidos: 150
- Participación: 74.348%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:05:12+00:00` | `2026-04-12 20:05:12 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:05:12+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:05:12+00:00` | `2026-04-12 20:05:12 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:10:24+00:00` | `2026-04-12 21:10:24 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:11:52+00:00` | `2026-04-12 21:11:52 (Lima)` |
| Última firma humana | `2026-04-13T02:12:46+00:00` | `2026-04-12 21:12:46 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.11 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:05:12 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:11:52 (Lima), es decir **1.11 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:05:10+00:00` | `2026-04-12 20:05:10 (Lima)` | -0.00h |
| 1 | AGUILAR CRUZATTI analucia Massiel FIR 76227805 sw a723955b03ef033f3589c5ba72fa1038d8ebfa5b | 76227805 | `2026-04-13T02:11:52+00:00` | `2026-04-12 21:11:52 (Lima)` | +1.11h |
| 2 | AGUIRRE MONTORO marleni Judiht FIR 07079104 sw b52995df884319fa6f7ce77372d8cc6c824c064f | 07079104 | `2026-04-13T02:12:27+00:00` | `2026-04-12 21:12:27 (Lima)` | +1.12h |
| 3 | ANAYA TIPE pool Henry FIR 41632216 sw 939dee7e8c03aa63b3d25a444cd69bdb37ddc1db | 41632216 | `2026-04-13T02:12:46+00:00` | `2026-04-12 21:12:46 (Lima)` | +1.13h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054370**
2. Descargar el PDF del acta
3. Verificar SHA-256: `fd030805c2439e44b72b577b990cfb916238adfac16961281b1c3ae6095aa37c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
