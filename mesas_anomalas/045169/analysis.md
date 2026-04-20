# Mesa 045169 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.175072+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: COLEGIO INMACULADO CORAZON (código 2991)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 217
- Votos válidos: 208
- Participación: 72.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:41:48+00:00` | `2026-04-12 20:41:48 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:41:48+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:41:48+00:00` | `2026-04-12 20:41:48 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:13:52+00:00` | `2026-04-13 00:13:52 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:15:04+00:00` | `2026-04-13 00:15:04 (Lima)` |
| Última firma humana | `2026-04-13T05:15:29+00:00` | `2026-04-13 00:15:29 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.55 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:41:48 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:15:04 (Lima), es decir **3.55 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:41:46+00:00` | `2026-04-12 20:41:46 (Lima)` | -0.00h |
| 1 | BARAZORDA URRUTIA DE RUIZ maria Luisa FIR 07333490 sw 4ac340550daac2724a11ad47cf75d96dfa37f4c6 | 07333490 | `2026-04-13T05:15:04+00:00` | `2026-04-13 00:15:04 (Lima)` | +3.55h |
| 2 | ARRASCUE BACA antonio Fermin FIR 40615112 sw b766b1553c76f0b21901644c65af3706f114a303 | 40615112 | `2026-04-13T05:15:17+00:00` | `2026-04-13 00:15:17 (Lima)` | +3.56h |
| 3 | BACA MONGE giselle Graciela FIR 44085134 sw 6b2a1b1056cd7d14585c3e6f1099df0343a5ee70 | 44085134 | `2026-04-13T05:15:29+00:00` | `2026-04-13 00:15:29 (Lima)` | +3.56h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045169**
2. Descargar el PDF del acta
3. Verificar SHA-256: `63edd930130109cb22789af21987a78c7163ab2ad7a654c50bc184cc9e3484d5`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
