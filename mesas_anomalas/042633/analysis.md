# Mesa 042633 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.796437+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LA VICTORIA
- **Local de votación**: IE 1119 NUESTRA SEÑORA DEL ROSARIO DE FATIMA (código 2886)
- **Ubigeo**: 140109

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 237
- Votos válidos: 214
- Participación: 79.264%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:32:14+00:00` | `2026-04-12 20:32:14 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:32:14+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:32:14+00:00` | `2026-04-12 20:32:14 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:50:53+00:00` | `2026-04-12 21:50:53 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:54:25+00:00` | `2026-04-12 21:54:25 (Lima)` |
| Última firma humana | `2026-04-13T02:57:15+00:00` | `2026-04-12 21:57:15 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.37 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:32:14 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:54:25 (Lima), es decir **1.37 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:32:12+00:00` | `2026-04-12 20:32:12 (Lima)` | -0.00h |
| 1 | PARCO FERNANDEZ alexander Jaime FIR 72504177 sw 5ec080cbfd91d206c380fb8c5f1407157a9052fa | 72504177 | `2026-04-13T02:54:25+00:00` | `2026-04-12 21:54:25 (Lima)` | +1.37h |
| 2 | PACHECO OBREGON DE PEREYRA yris FIR 09710989 sw 583cc983d95ebc528b9773d9949d6b9380ea0891 | 09710989 | `2026-04-13T02:56:29+00:00` | `2026-04-12 21:56:29 (Lima)` | +1.40h |
| 3 | MAZA MAMANI DE HIDALGO patricia Janet FIR 07469252 sw 33725dde196fe02005dc9d59788d26bc5803d0c8 | 07469252 | `2026-04-13T02:57:15+00:00` | `2026-04-12 21:57:15 (Lima)` | +1.42h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042633**
2. Descargar el PDF del acta
3. Verificar SHA-256: `7ed70a525e3e0fa928cf7ac28ba76932b0d7b72da3257fc2ae6837dbcdb0354a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
