# Mesa 051290 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.998899+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: UNIVERSIDAD DE LIMA 2 (código 51521)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 205
- Votos válidos: 196
- Participación: 68.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T05:56:42+00:00` | `2026-04-13 00:56:42 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T05:56:42+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T05:56:42+00:00` | `2026-04-13 00:56:42 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:29:24+00:00` | `2026-04-13 08:29:24 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:29:40+00:00` | `2026-04-13 08:29:40 (Lima)` |
| Última firma humana | `2026-04-13T13:30:33+00:00` | `2026-04-13 08:30:33 (Lima)` |

**Brecha primera firma humana vs publicación:** **+7.55 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-13 00:56:42 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:29:40 (Lima), es decir **7.55 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T05:56:41+00:00` | `2026-04-13 00:56:41 (Lima)` | -0.00h |
| 1 | ARRIETA BORGO luis Enrique FIR 41596116 sw f4268b8e52e4b8b2992569da42f9bd8540c77ac2 | 41596116 | `2026-04-13T13:29:40+00:00` | `2026-04-13 08:29:40 (Lima)` | +7.55h |
| 2 | BANONI YUPANQUI DE SOLIS marlene Patricia FIR 09537539 sw a04d561754bdc1daa3cc7c27e6ce0cf5a994b946 | 09537539 | `2026-04-13T13:30:18+00:00` | `2026-04-13 08:30:18 (Lima)` | +7.56h |
| 3 | AYALA RONCAL arianne Jhaseth FIR 75432252 sw 5c108b1aaf53519e0dfb9c16a32af3e677fecf3f | 75432252 | `2026-04-13T13:30:33+00:00` | `2026-04-13 08:30:33 (Lima)` | +7.56h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051290**
2. Descargar el PDF del acta
3. Verificar SHA-256: `ee984cab091d727358ef9708e031c08f39be462987f68e7e9e1ddb07c6e21436`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
