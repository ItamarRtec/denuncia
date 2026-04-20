# Mesa 047209 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.763826+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: RÍMAC
- **Local de votación**: IE 3021 SAN JUAN MACIAS (código 3061)
- **Ubigeo**: 140122

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 242
- Votos válidos: 210
- Participación: 80.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:11:45+00:00` | `2026-04-12 21:11:45 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:11:45+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:11:45+00:00` | `2026-04-12 21:11:45 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:14:23+00:00` | `2026-04-12 23:14:23 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:15:23+00:00` | `2026-04-12 23:15:23 (Lima)` |
| Última firma humana | `2026-04-13T04:17:03+00:00` | `2026-04-12 23:17:03 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.06 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:11:45 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:15:23 (Lima), es decir **2.06 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:11:43+00:00` | `2026-04-12 21:11:43 (Lima)` | -0.00h |
| 1 | OSORIO CORDERO jose Alberto FIR 08122785 sw f9c077a2f193d1c3540026334488e2cad616e795 | 08122785 | `2026-04-13T04:15:23+00:00` | `2026-04-12 23:15:23 (Lima)` | +2.06h |
| 2 | MIRANDA SANCHEZ david Hector FIR 08143832 sw b850049dcec5d210ef73f5a658f0edc995ea0b74 | 08143832 | `2026-04-13T04:15:41+00:00` | `2026-04-12 23:15:41 (Lima)` | +2.07h |
| 3 | PALACIOS GARCIA miguel Angel FIR 00250294 sw 26a91d4653986cef0ce9fc52b87f4044c84705c9 | 00250294 | `2026-04-13T04:16:01+00:00` | `2026-04-12 23:16:01 (Lima)` | +2.07h |
| 4 | CALDAS CHAHUAYA jharumy Lizbeth Karoline FIR 70545957 sw 23b161b5462566c68d0bc4c3ddf2cba29a878d49 | 70545957 | `2026-04-13T04:17:03+00:00` | `2026-04-12 23:17:03 (Lima)` | +2.09h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **047209**
2. Descargar el PDF del acta
3. Verificar SHA-256: `508e54ed6cf0d714f400e9adacf171f32dc8bd487bd1707683e4264309b736f4`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
