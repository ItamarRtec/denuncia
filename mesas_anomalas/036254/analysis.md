# Mesa 036254 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.436264+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE 1168 HEROES DEL CENEPA (código 2658)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 235
- Votos válidos: 211
- Participación: 78.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:17:07+00:00` | `2026-04-12 20:17:07 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:17:07+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:17:07+00:00` | `2026-04-12 20:17:07 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T10:15:42+00:00` | `2026-04-13 05:15:42 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T10:15:56+00:00` | `2026-04-13 05:15:56 (Lima)` |
| Última firma humana | `2026-04-13T10:16:22+00:00` | `2026-04-13 05:16:22 (Lima)` |

**Brecha primera firma humana vs publicación:** **+8.98 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:17:07 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 05:15:56 (Lima), es decir **8.98 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:17:05+00:00` | `2026-04-12 20:17:05 (Lima)` | -0.00h |
| 1 | VERDE SANTIAGO olenka Lisset FIR 75050251 sw 7a332349d121eda1751d4792fe7011ee4cfa38c5 | 75050251 | `2026-04-13T10:15:56+00:00` | `2026-04-13 05:15:56 (Lima)` | +8.98h |
| 2 | YARLEQUE ARTEAGA oscar Jose FIR 06276632 sw bb142904b6f0b0d7b5c40d24912f4bf7d707fbab | 06276632 | `2026-04-13T10:16:09+00:00` | `2026-04-13 05:16:09 (Lima)` | +8.98h |
| 3 | YUEN CASHU yanet Elizabeth FIR 09427303 sw ab59d4c84f64b8cffcf9d175f173f148f58b6f32 | 09427303 | `2026-04-13T10:16:22+00:00` | `2026-04-13 05:16:22 (Lima)` | +8.99h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036254**
2. Descargar el PDF del acta
3. Verificar SHA-256: `189b5874360646827bd741b4b6d4d5fac0507c27628bd8e147cf3e853ed8f222`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
