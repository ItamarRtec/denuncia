# Mesa 042422 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.111122+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: IEP INNOVA SCHOOLS - CHORRILLOS HORIZONTES (código 54417)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 241
- Votos válidos: 218
- Participación: 80.602%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:17:28+00:00` | `2026-04-12 21:17:28 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:17:28+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:17:28+00:00` | `2026-04-12 21:17:28 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:16:01+00:00` | `2026-04-13 08:16:01 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:16:29+00:00` | `2026-04-13 08:16:29 (Lima)` |
| Última firma humana | `2026-04-13T13:16:56+00:00` | `2026-04-13 08:16:56 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.98 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:17:28 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:16:29 (Lima), es decir **10.98 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:16:55+00:00` | `2026-04-12 21:16:55 (Lima)` | -0.01h |
| 1 | HUYHUA MOTTA ana Maria FIR 09150953 sw d0b99ee6a3281c30e424472d3f94944a8ecec72a | 09150953 | `2026-04-13T13:16:29+00:00` | `2026-04-13 08:16:29 (Lima)` | +10.98h |
| 2 | HUAMAN TINEO edson De Jesus FIR 46331648 sw 7b2500acd034d2c36a2330e8e666a673870a1767 | 46331648 | `2026-04-13T13:16:43+00:00` | `2026-04-13 08:16:43 (Lima)` | +10.99h |
| 3 | HUARCAYA USQUIANO jessenia FIR 48307726 sw 3ac9a189f9d688009bb8e3f87afa12272b25b3a1 | 48307726 | `2026-04-13T13:16:56+00:00` | `2026-04-13 08:16:56 (Lima)` | +10.99h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042422**
2. Descargar el PDF del acta
3. Verificar SHA-256: `19dc11b000cbb28ee0ce8ec00e71ef59e61f14ee17a34e74d54f2e3ae26f31a0`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
