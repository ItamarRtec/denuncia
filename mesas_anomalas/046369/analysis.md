# Mesa 046369 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.545169+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUENTE PIEDRA
- **Local de votación**: IE 5168 ROSA LUZ (código 3036)
- **Ubigeo**: 140119

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 262
- Votos válidos: 227
- Participación: 87.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:04:07+00:00` | `2026-04-12 22:04:07 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:04:07+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:04:07+00:00` | `2026-04-12 22:04:07 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:40:30+00:00` | `2026-04-13 08:40:30 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:45:12+00:00` | `2026-04-13 08:45:12 (Lima)` |
| Última firma humana | `2026-04-13T13:51:27+00:00` | `2026-04-13 08:51:27 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.68 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:04:07 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:45:12 (Lima), es decir **10.68 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:04:05+00:00` | `2026-04-12 22:04:05 (Lima)` | -0.00h |
| 1 | PORLLES TAPULLIMA daniela Patricia FIR 75284999 sw baaf2c60d12ea7b6f4da5abcd4d6fe718d49cea8 | 75284999 | `2026-04-13T13:45:12+00:00` | `2026-04-13 08:45:12 (Lima)` | +10.68h |
| 2 | QUISPE CORONEL lizet Dolores FIR 41398029 sw 2027c0250222c0282a353ee91f87e608086d808d | 41398029 | `2026-04-13T13:49:16+00:00` | `2026-04-13 08:49:16 (Lima)` | +10.75h |
| 3 | QUISPE RAMIREZ marco FIR 09605694 sw c1ec3f8fa09d1485be3d98d41bf1f7f6cd775b21 | 09605694 | `2026-04-13T13:51:27+00:00` | `2026-04-13 08:51:27 (Lima)` | +10.79h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046369**
2. Descargar el PDF del acta
3. Verificar SHA-256: `285934e852e8730bd07a550537d56a9cf99b66f919af621c97a04fc07032915e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
