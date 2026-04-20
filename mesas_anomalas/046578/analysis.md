# Mesa 046578 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.586170+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUENTE PIEDRA
- **Local de votación**: IE 2076 ABRAHAM LINCOLN (código 5101)
- **Ubigeo**: 140119

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 256
- Votos válidos: 234
- Participación: 85.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:25:58+00:00` | `2026-04-12 21:25:58 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:25:58+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:25:58+00:00` | `2026-04-12 21:25:58 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T07:14:53+00:00` | `2026-04-13 02:14:53 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T07:15:16+00:00` | `2026-04-13 02:15:16 (Lima)` |
| Última firma humana | `2026-04-13T07:16:25+00:00` | `2026-04-13 02:16:25 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.82 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:25:58 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 02:15:16 (Lima), es decir **4.82 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:24:58+00:00` | `2026-04-12 21:24:58 (Lima)` | -0.02h |
| 1 | NOMBERTO BALLENA joan Alex FIR 47467480 sw b2b09e239ff045de2fbc74db12b38e7930c050ca | 47467480 | `2026-04-13T07:15:16+00:00` | `2026-04-13 02:15:16 (Lima)` | +4.82h |
| 2 | MURGA MIGUEL herlin Brandon FIR 74723695 sw bbb078dfe8f4afd47abde9031e08760600799a49 | 74723695 | `2026-04-13T07:15:36+00:00` | `2026-04-13 02:15:36 (Lima)` | +4.83h |
| 3 | OLIVOS GARCIA rosario Teresa FIR 10195620 sw f2856eb7b4543d30954b03a805cf29826054a3a4 | 10195620 | `2026-04-13T07:15:50+00:00` | `2026-04-13 02:15:50 (Lima)` | +4.83h |
| 4 | GOMERO ESPINOZA eusebio Fortunato FIR 32298596 sw a836ba3f14dd67bd0fcf9e02f6f5a395ac9dca77 | 32298596 | `2026-04-13T07:16:25+00:00` | `2026-04-13 02:16:25 (Lima)` | +4.84h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046578**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3109e0fbf25c5a958b12c0fdab09b457e11cd7a7e0f77b66296e1168e0ba49db`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
