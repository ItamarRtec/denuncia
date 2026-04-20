# Mesa 042475 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.970132+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: IEP INNOVA SCHOOLS - CHORRILLOS LOS FAISANES (código 54780)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 239
- Votos válidos: 223
- Participación: 79.933%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:46:33+00:00` | `2026-04-12 20:46:33 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:46:33+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:46:33+00:00` | `2026-04-12 20:46:33 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:52:28+00:00` | `2026-04-13 07:52:28 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:53:03+00:00` | `2026-04-13 07:53:03 (Lima)` |
| Última firma humana | `2026-04-13T12:54:30+00:00` | `2026-04-13 07:54:30 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.11 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:46:33 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:53:03 (Lima), es decir **11.11 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:46:30+00:00` | `2026-04-12 20:46:30 (Lima)` | -0.00h |
| 1 | VALENCIA GUTIERREZ miguel Angel FIR 42035551 sw 635527c934079fcdf1730af6488b47c1f0c6298d | 42035551 | `2026-04-13T12:53:03+00:00` | `2026-04-13 07:53:03 (Lima)` | +11.11h |
| 2 | VELARDE ESPINOZA luis Alberto FIR 06290683 sw f666e8f63d580a193dcadeeeec80ff7aae0b9f85 | 06290683 | `2026-04-13T12:53:55+00:00` | `2026-04-13 07:53:55 (Lima)` | +11.12h |
| 3 | VEGA GARCIA odaliz Milagros FIR 10325736 sw 053bb0bb3c6c45596d076e56ef48551c739de488 | 10325736 | `2026-04-13T12:54:06+00:00` | `2026-04-13 07:54:06 (Lima)` | +11.13h |
| 4 | CISNEROS RUIZ alfredo FIR 40907719 sw 6ad1029e3ca8e35f57ef1188987681e7c33f5bdc | 40907719 | `2026-04-13T12:54:30+00:00` | `2026-04-13 07:54:30 (Lima)` | +11.13h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042475**
2. Descargar el PDF del acta
3. Verificar SHA-256: `7a377f481f82d5db18d4153c28c4e96accb64badf13ba244c31d39e2cf30b387`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
