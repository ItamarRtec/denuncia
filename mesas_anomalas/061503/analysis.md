# Mesa 061503 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.231964+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LOS OLIVOS
- **Local de votación**: CEPD EL BUEN PASTOR (código 54427)
- **Ubigeo**: 140142

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 233
- Votos válidos: 205
- Participación: 77.926%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:10:30+00:00` | `2026-04-12 21:10:30 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:10:30+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:10:30+00:00` | `2026-04-12 21:10:30 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:48:01+00:00` | `2026-04-12 22:48:01 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:48:54+00:00` | `2026-04-12 22:48:54 (Lima)` |
| Última firma humana | `2026-04-13T03:49:14+00:00` | `2026-04-12 22:49:14 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.64 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:10:30 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:48:54 (Lima), es decir **1.64 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:09:52+00:00` | `2026-04-12 21:09:52 (Lima)` | -0.01h |
| 1 | TOMAS RAMOS alessandra Mercedes FIR 70502903 sw 0a97d6a257252c3f0398ad7f6e1b49e215d1891a | 70502903 | `2026-04-13T03:48:54+00:00` | `2026-04-12 22:48:54 (Lima)` | +1.64h |
| 2 | TUMIALAN CALVAY antonio Efrain FIR 71324432 sw 7225c16d520c6889a4a87088a0c5ffe8a77c13c2 | 71324432 | `2026-04-13T03:49:14+00:00` | `2026-04-12 22:49:14 (Lima)` | +1.65h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061503**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8cd4a22c1234bcfb17f4e149077d7c71eddd20aad6fac71825db610acf89953c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
