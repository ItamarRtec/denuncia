# Mesa 051208 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.905346+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: CAMPO DEPORTIVO EL TANQUE (código 34926)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 223
- Votos válidos: 205
- Participación: 74.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:55:44+00:00` | `2026-04-12 21:55:44 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:55:44+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:55:44+00:00` | `2026-04-12 21:55:44 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:03:49+00:00` | `2026-04-13 00:03:49 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:04:02+00:00` | `2026-04-13 00:04:02 (Lima)` |
| Última firma humana | `2026-04-13T05:04:24+00:00` | `2026-04-13 00:04:24 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.14 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:55:44 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:04:02 (Lima), es decir **2.14 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:55:42+00:00` | `2026-04-12 21:55:42 (Lima)` | -0.00h |
| 1 | MONTELLANOS CORZO ernesto Gerardo FIR 07628618 sw 37bed8c328d9e54b70672b6245d3e8a832b1a6c3 | 07628618 | `2026-04-13T05:04:02+00:00` | `2026-04-13 00:04:02 (Lima)` | +2.14h |
| 2 | MAMANI ALVAREZ jhon Denis FIR 70101966 sw d91350278c15a2000e99f9a9e72d1937536e6966 | 70101966 | `2026-04-13T05:04:13+00:00` | `2026-04-13 00:04:13 (Lima)` | +2.14h |
| 3 | MIRANDA MAYURI yolanda Victoria FIR 09880227 sw 522845948188f3583f931a180273f449cac36a8e | 09880227 | `2026-04-13T05:04:24+00:00` | `2026-04-13 00:04:24 (Lima)` | +2.14h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051208**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c12d3f9a9447a4a22628aaf2c66c1c3072950d9b9091937938c262029a11c889`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
