# Mesa 046005 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.972689+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUEBLO LIBRE
- **Local de votación**: IE 04 NIÑO JESUS DE PRAGA (código 50932)
- **Ubigeo**: 140117

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 235
- Votos válidos: 220
- Participación: 78.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:46:59+00:00` | `2026-04-12 19:46:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:46:59+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:46:59+00:00` | `2026-04-12 19:46:59 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T01:00:38+00:00` | `2026-04-12 20:00:38 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T01:01:21+00:00` | `2026-04-12 20:01:21 (Lima)` |
| Última firma humana | `2026-04-13T01:02:18+00:00` | `2026-04-12 20:02:18 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.24 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:46:59 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 20:01:21 (Lima), es decir **0.24 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:46:58+00:00` | `2026-04-12 19:46:58 (Lima)` | -0.00h |
| 1 | CHAVEZ MOSQUEIRA lenin FIR 26723924 sw f514bb88bfd5f858881c522981b1a777e5a28ba8 | 26723924 | `2026-04-13T01:01:21+00:00` | `2026-04-12 20:01:21 (Lima)` | +0.24h |
| 2 | BAUTISTA ALZAMORA stanley FIR 40122480 sw 94ab0d966408e97fdc334ed76a3966c58d7c1a72 | 40122480 | `2026-04-13T01:01:34+00:00` | `2026-04-12 20:01:34 (Lima)` | +0.24h |
| 3 | CORDOVA PACHECO jean Carlo FIR 44099862 sw 013262f3b21324099bfaf0124532eddce4aad6a9 | 44099862 | `2026-04-13T01:01:46+00:00` | `2026-04-12 20:01:46 (Lima)` | +0.25h |
| 4 | VARGAS REPETTO rossicela Johana FIR 74987704 sw 320d706ccefaafc0da17005983e7ef85ce3be1ae | 74987704 | `2026-04-13T01:02:18+00:00` | `2026-04-12 20:02:18 (Lima)` | +0.26h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046005**
2. Descargar el PDF del acta
3. Verificar SHA-256: `a8fe3091f90633aa4884da7757b8f3f20bfc0e46883fef7b0eef8fc62f894cfa`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
