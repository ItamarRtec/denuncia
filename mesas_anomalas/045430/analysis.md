# Mesa 045430 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.130710+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: COLEGIO MEDICO DEL PERU (código 54879)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 199
- Votos válidos: 191
- Participación: 66.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:34:07+00:00` | `2026-04-12 20:34:07 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:34:07+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:34:07+00:00` | `2026-04-12 20:34:07 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:59:11+00:00` | `2026-04-12 22:59:11 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:59:28+00:00` | `2026-04-12 22:59:28 (Lima)` |
| Última firma humana | `2026-04-13T04:00:18+00:00` | `2026-04-12 23:00:18 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.42 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:34:07 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:59:28 (Lima), es decir **2.42 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:34:05+00:00` | `2026-04-12 20:34:05 (Lima)` | -0.00h |
| 1 | BERROCAL MORENO DE KAHN sarita Del Pilar FIR 10545316 sw d0b8acc028810d068518780704db546f95eecb86 | 10545316 | `2026-04-13T03:59:28+00:00` | `2026-04-12 22:59:28 (Lima)` | +2.42h |
| 2 | BURGA RENGIFO elizabeth FIR 06249740 sw 742be552260c89a402f988683e69f2392dd8801a | 06249740 | `2026-04-13T03:59:40+00:00` | `2026-04-12 22:59:40 (Lima)` | +2.43h |
| 3 | BRAITHWAITE PEREZ john FIR 07883119 sw 7b185679d4f33466969a836820b736a4d1bcd0d2 | 07883119 | `2026-04-13T03:59:51+00:00` | `2026-04-12 22:59:51 (Lima)` | +2.43h |
| 4 | RIOS FERNANDEZ sharon Michelle FIR 70434251 sw d4a5b6d301c860b6bbae5e4372f03b5d71d8eba0 | 70434251 | `2026-04-13T04:00:18+00:00` | `2026-04-12 23:00:18 (Lima)` | +2.44h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045430**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5b11d6734ccfb6a2616473aadcb87bff5b142ebf2f7fff5feae735f496595471`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
