# Mesa 050662 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.353825+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IE 7058 MARIA DE FATIMA (código 3201)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 245
- Votos válidos: 226
- Participación: 81.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:17:09+00:00` | `2026-04-12 20:17:09 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:17:09+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:17:09+00:00` | `2026-04-12 20:17:09 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:38:30+00:00` | `2026-04-12 23:38:30 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:39:31+00:00` | `2026-04-12 23:39:31 (Lima)` |
| Última firma humana | `2026-04-13T04:39:54+00:00` | `2026-04-12 23:39:54 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.37 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:17:09 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:39:31 (Lima), es decir **3.37 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:17:07+00:00` | `2026-04-12 20:17:07 (Lima)` | -0.00h |
| 1 | QUINTANILLA CAYCHO alberto Carlos FIR 40535592 sw aba7bad5d9ad4ca16d326614342b1d43174e5cfa | 40535592 | `2026-04-13T04:39:31+00:00` | `2026-04-12 23:39:31 (Lima)` | +3.37h |
| 2 | ROJO ALZAMORA pablo Roberto FIR 07350897 sw 9cbb62fef7466fa35a6439e180bfd7c16266e2fc | 07350897 | `2026-04-13T04:39:43+00:00` | `2026-04-12 23:39:43 (Lima)` | +3.38h |
| 3 | RIVERA VALVERDE geancarlo Jesus FIR 75199440 sw 1b51f9eff62d7878e6b0dbbfeb02385d026e5ecf | 75199440 | `2026-04-13T04:39:54+00:00` | `2026-04-12 23:39:54 (Lima)` | +3.38h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050662**
2. Descargar el PDF del acta
3. Verificar SHA-256: `9f7bab078da1a72c8288f7e3b42435260ea35edd8ce8805e7a8e1ac22c99312d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
