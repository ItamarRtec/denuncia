# Mesa 050562 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.601010+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: COLEGIO CHAMPAGNAT (código 3195)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 227
- Votos válidos: 214
- Participación: 75.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:50:01+00:00` | `2026-04-12 20:50:01 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:50:01+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:50:01+00:00` | `2026-04-12 20:50:01 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:58:51+00:00` | `2026-04-13 00:58:51 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:59:15+00:00` | `2026-04-13 00:59:15 (Lima)` |
| Última firma humana | `2026-04-13T05:59:43+00:00` | `2026-04-13 00:59:43 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.15 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:50:01 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:59:15 (Lima), es decir **4.15 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:49:57+00:00` | `2026-04-12 20:49:57 (Lima)` | -0.00h |
| 1 | ZAMUDIO PARDO FIGUEROA ricardo Gustavo FIR 09868637 sw ca5b77d55df02bbdd569b56cf2a5ce89565725c2 | 09868637 | `2026-04-13T05:59:15+00:00` | `2026-04-13 00:59:15 (Lima)` | +4.15h |
| 2 | WILLIAMZON RELUZ stephany Melissa FIR 72813371 sw d49e6dccd7c962976c49e68c17ae26cbcb3ea005 | 72813371 | `2026-04-13T05:59:43+00:00` | `2026-04-13 00:59:43 (Lima)` | +4.16h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050562**
2. Descargar el PDF del acta
3. Verificar SHA-256: `363b3d027c57a1871bced6469775e524a12e11428b11c0aa1f8c89603b0cb0cc`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
