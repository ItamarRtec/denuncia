# Mesa 081742 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.230323+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CALLAO
- **Local de votación**: COMPLEJO DEPORTIVO RAMÓN CASTILLA (código 17604)
- **Ubigeo**: 240101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 221
- Votos válidos: 193
- Participación: 73.913%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:48:14+00:00` | `2026-04-12 20:48:14 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:48:14+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:48:14+00:00` | `2026-04-12 20:48:14 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:03:10+00:00` | `2026-04-12 22:03:10 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:03:27+00:00` | `2026-04-12 22:03:27 (Lima)` |
| Última firma humana | `2026-04-13T03:04:29+00:00` | `2026-04-12 22:04:29 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.25 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:48:14 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:03:27 (Lima), es decir **1.25 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:48:12+00:00` | `2026-04-12 20:48:12 (Lima)` | -0.00h |
| 1 | BUSTAMANTE PEREZ jose Luis FIR 25788493 sw 90efdfa2de8b12ba1d2d34594d646cf8d0a6cabf | 25788493 | `2026-04-13T03:03:27+00:00` | `2026-04-12 22:03:27 (Lima)` | +1.25h |
| 2 | BOLIVAR ESCUDERO victor Julio FIR 25782080 sw 4885f91e6ca172f289479b57a056bf97762fbb39 | 25782080 | `2026-04-13T03:03:51+00:00` | `2026-04-12 22:03:51 (Lima)` | +1.26h |
| 3 | VALLE GONZALES andrea Consuelo FIR 25842026 sw d9576a1e8738b83f9486fd493e819d65ddd4811f | 25842026 | `2026-04-13T03:04:29+00:00` | `2026-04-12 22:04:29 (Lima)` | +1.27h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **081742**
2. Descargar el PDF del acta
3. Verificar SHA-256: `0c58ab8ac23c30feecb8ba165de429b036bd7b95dbaf0ba07ed79bcc11b2a28f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
