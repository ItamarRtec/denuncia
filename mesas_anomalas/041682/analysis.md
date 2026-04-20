# Mesa 041682 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.678858+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: IE 6090 JOSE OLAYA BALANDRA (código 2858)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 248
- Votos válidos: 226
- Participación: 82.943%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T04:10:53+00:00` | `2026-04-12 23:10:53 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T04:10:53+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T04:10:53+00:00` | `2026-04-12 23:10:53 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:52:19+00:00` | `2026-04-13 09:52:19 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:53:06+00:00` | `2026-04-13 09:53:06 (Lima)` |
| Última firma humana | `2026-04-13T14:53:29+00:00` | `2026-04-13 09:53:29 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.70 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 23:10:53 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:53:06 (Lima), es decir **10.70 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T04:10:51+00:00` | `2026-04-12 23:10:51 (Lima)` | -0.00h |
| 1 | MENDOZA VIGO edson Wagner FIR 47299545 sw 1557f1bd2271429152a83ea0306f9fa5c2aa9a5b | 47299545 | `2026-04-13T14:53:06+00:00` | `2026-04-13 09:53:06 (Lima)` | +10.70h |
| 2 | MEDINA SOTO judith FIR 09486743 sw 9c1bb9cd4729b5a5b0cf76b4247b80b0da4f6c8a | 09486743 | `2026-04-13T14:53:18+00:00` | `2026-04-13 09:53:18 (Lima)` | +10.71h |
| 3 | MARTINEZ PORRAS roland Rafael FIR 41257917 sw 93812bb29fcc8ea557c1b2da9e1fd5f7aa9cc214 | 41257917 | `2026-04-13T14:53:29+00:00` | `2026-04-13 09:53:29 (Lima)` | +10.71h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041682**
2. Descargar el PDF del acta
3. Verificar SHA-256: `96e4453772ea85ec522b775bb2057143d0e8790d1eca7cbef4d360e60ded0c4b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
