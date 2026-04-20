# Mesa 083099 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.654003+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: VENTANILLA
- **Local de votación**: IE 5086 POLITECNICO DE VENTANILLA (código 4862)
- **Ubigeo**: 240106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 268
- Votos válidos: 242
- Participación: 89.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:24:50+00:00` | `2026-04-12 19:24:50 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:24:50+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:24:50+00:00` | `2026-04-12 19:24:50 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:13:05+00:00` | `2026-04-13 00:13:05 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:13:20+00:00` | `2026-04-13 00:13:20 (Lima)` |
| Última firma humana | `2026-04-13T05:14:25+00:00` | `2026-04-13 00:14:25 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.81 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:24:50 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:13:20 (Lima), es decir **4.81 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:24:47+00:00` | `2026-04-12 19:24:47 (Lima)` | -0.00h |
| 1 | QUISPE CARTAGENA katherine Zoila FIR 43668328 sw 719df65a37a3944cb2380a4cd1f0f742edc7fe75 | 43668328 | `2026-04-13T05:13:20+00:00` | `2026-04-13 00:13:20 (Lima)` | +4.81h |
| 2 | PEREZ INUMA jose Armando FIR 05265389 sw 7814870f254133b6f20f6b4e05409eea5efd6c6b | 05265389 | `2026-04-13T05:13:33+00:00` | `2026-04-13 00:13:33 (Lima)` | +4.81h |
| 3 | PARODI SAYAS santosa FIR 07806581 sw 66ba213036cb5dde3673702edf96e096619f2378 | 07806581 | `2026-04-13T05:13:48+00:00` | `2026-04-13 00:13:48 (Lima)` | +4.82h |
| 4 | PANDURO DAVILA herberi FIR 45023850 sw fafce2dc222d170e1a9eac7ce3449378a9268be4 | 45023850 | `2026-04-13T05:14:25+00:00` | `2026-04-13 00:14:25 (Lima)` | +4.83h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083099**
2. Descargar el PDF del acta
3. Verificar SHA-256: `a9b65e40bb4fc4386b90af4345adeb6c29205ecfabdb2cefa788d31692fe1332`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
