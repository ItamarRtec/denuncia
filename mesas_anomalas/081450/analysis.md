# Mesa 081450 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.177928+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CALLAO
- **Local de votación**: IE 5095 JULIO RAMON RIBEYRO (código 4794)
- **Ubigeo**: 240101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 265
- Votos válidos: 239
- Participación: 88.629%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:59:11+00:00` | `2026-04-12 22:59:11 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:59:11+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:59:11+00:00` | `2026-04-12 22:59:11 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:25:11+00:00` | `2026-04-13 09:25:11 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:25:34+00:00` | `2026-04-13 09:25:34 (Lima)` |
| Última firma humana | `2026-04-13T14:27:11+00:00` | `2026-04-13 09:27:11 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.44 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:59:11 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:25:34 (Lima), es decir **10.44 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:59:08+00:00` | `2026-04-12 22:59:08 (Lima)` | -0.00h |
| 1 | TICONA AGUILAR eduardo Manuel FIR 41634902 sw 0f9f57cff380d666f7e3765402440d38cbf636b0 | 41634902 | `2026-04-13T14:25:34+00:00` | `2026-04-13 09:25:34 (Lima)` | +10.44h |
| 2 | VALDIVIA GONZALES joselyn Rosa FIR 72889767 sw a26c1cf685a2d585244c412b7560ec02b134e9fe | 72889767 | `2026-04-13T14:26:05+00:00` | `2026-04-13 09:26:05 (Lima)` | +10.45h |
| 3 | TORRES CACERES elver Revelino FIR 40621607 sw f5a9d734f93d516c873ef550fbb8bf1fb1a513f3 | 40621607 | `2026-04-13T14:26:22+00:00` | `2026-04-13 09:26:22 (Lima)` | +10.45h |
| 4 | COPA TORRES tony Yohel FIR 44869556 sw f2c4d7d7d3e37dd69c0fb2a8eda8d851fab4b7e1 | 44869556 | `2026-04-13T14:27:11+00:00` | `2026-04-13 09:27:11 (Lima)` | +10.47h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **081450**
2. Descargar el PDF del acta
3. Verificar SHA-256: `31845cbe926a5573fcf62b4b1132bc8fa104b3c28c9e57ed0d37c85a44218bbf`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
