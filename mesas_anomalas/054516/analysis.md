# Mesa 054516 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.381297+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: EL AGUSTINO
- **Local de votación**: ESTADIO MUNICIPAL MARCELINO CCAICO ARONE (código 13105)
- **Ubigeo**: 140135

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 260
- Votos válidos: 229
- Participación: 86.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:09:05+00:00` | `2026-04-12 20:09:05 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:09:05+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:09:05+00:00` | `2026-04-12 20:09:05 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:53:36+00:00` | `2026-04-12 21:53:36 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:53:51+00:00` | `2026-04-12 21:53:51 (Lima)` |
| Última firma humana | `2026-04-13T02:54:18+00:00` | `2026-04-12 21:54:18 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.75 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:09:05 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:53:51 (Lima), es decir **1.75 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:09:03+00:00` | `2026-04-12 20:09:03 (Lima)` | -0.00h |
| 1 | QUISPE CHAVEZ bety FIR 09939505 sw 47fed7b83524707615d2b869480b75620561d2f0 | 09939505 | `2026-04-13T02:53:51+00:00` | `2026-04-12 21:53:51 (Lima)` | +1.75h |
| 2 | QUISPE CUBA paulino Julio FIR 09424491 sw bc387fceb56b02bbc826a5aab4a2343cd46804af | 09424491 | `2026-04-13T02:54:07+00:00` | `2026-04-12 21:54:07 (Lima)` | +1.75h |
| 3 | QUIQUIA LIVIA santos Nelson FIR 10469287 sw 470aca989b7f1edd87bf385e6a242cea7e1ad5c7 | 10469287 | `2026-04-13T02:54:18+00:00` | `2026-04-12 21:54:18 (Lima)` | +1.75h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054516**
2. Descargar el PDF del acta
3. Verificar SHA-256: `108b819b878068b741b6aac3503889f791f971223f257fd5d837ef3c090f99df`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
