# Mesa 055677 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.034561+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IEP FERMIN TANGUIS (código 13919)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 236
- Votos válidos: 215
- Participación: 78.93%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:43:49+00:00` | `2026-04-12 22:43:49 (Lima)` |
| `C` | Contabilizada | `2026-04-13T03:40:15+00:00` | `2026-04-12 22:40:15 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:43:49+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:43:49+00:00` | `2026-04-12 22:43:49 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T15:10:07+00:00` | `2026-04-13 10:10:07 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T15:14:45+00:00` | `2026-04-13 10:14:45 (Lima)` |
| Última firma humana | `2026-04-13T15:18:39+00:00` | `2026-04-13 10:18:39 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.52 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:43:49 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 10:14:45 (Lima), es decir **11.52 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:40:13+00:00` | `2026-04-12 22:40:13 (Lima)` | -0.06h |
| 1 | RIVAS LOPEZ cesar Augusto FIR 10707350 sw 56a4d92d9bda2ee1a2eeab22e9609c03bc4a8c3f | 10707350 | `2026-04-13T15:14:45+00:00` | `2026-04-13 10:14:45 (Lima)` | +11.52h |
| 2 | RODRIGUEZ BEDIA judith Rocio FIR 44755689 sw 3448df213584bc354574b56fc08955078477409c | 44755689 | `2026-04-13T15:17:03+00:00` | `2026-04-13 10:17:03 (Lima)` | +11.55h |
| 3 | ROBLES PEREZ silvia Yazu FIR 46098624 sw 9f9da7956fa2454d918a26f812b9edbdcf500f72 | 46098624 | `2026-04-13T15:18:39+00:00` | `2026-04-13 10:18:39 (Lima)` | +11.58h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055677**
2. Descargar el PDF del acta
3. Verificar SHA-256: `7b3e8d242c15045f3a32289666dc7222bd77cc1cf804a7a1ccc8ba809ed4593b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
