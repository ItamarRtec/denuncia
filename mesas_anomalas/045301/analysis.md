# Mesa 045301 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.814287+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: IEP ADVIENTO (código 32594)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 196
- Votos válidos: 185
- Participación: 65.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:14:16+00:00` | `2026-04-12 21:14:16 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:14:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:14:16+00:00` | `2026-04-12 21:14:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T07:10:09+00:00` | `2026-04-13 02:10:09 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T07:10:26+00:00` | `2026-04-13 02:10:26 (Lima)` |
| Última firma humana | `2026-04-13T07:11:22+00:00` | `2026-04-13 02:11:22 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.94 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:14:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 02:10:26 (Lima), es decir **4.94 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:14:14+00:00` | `2026-04-12 21:14:14 (Lima)` | -0.00h |
| 1 | MOREAU  samuel Hubert Charles FIR 49081503 sw 3c6746fa86c0677d5d7ae202c87e4187377f412e | 49081503 | `2026-04-13T07:10:26+00:00` | `2026-04-13 02:10:26 (Lima)` | +4.94h |
| 2 | NAVARRO VILLACORTA jose Percy FIR 06094101 sw 35bc9fff44975e74ac6902727027bb6787325cbf | 06094101 | `2026-04-13T07:10:53+00:00` | `2026-04-13 02:10:53 (Lima)` | +4.94h |
| 3 | NORABUENA PADILLA DE BENTFELD evelyn FIR 07773202 sw bb3e479462c0f547d1902592a3f9aae154dc5107 | 07773202 | `2026-04-13T07:11:22+00:00` | `2026-04-13 02:11:22 (Lima)` | +4.95h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045301**
2. Descargar el PDF del acta
3. Verificar SHA-256: `6bcdef92f499167d6bda9a57457056bf6b2b0a14f6091ffa93d1d4744ceb16b8`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
