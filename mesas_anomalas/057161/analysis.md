# Mesa 057161 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.714579+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IE NICOLAS COPERNICO (código 3460)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 257
- Votos válidos: 210
- Participación: 85.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:37:07+00:00` | `2026-04-12 20:37:07 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:37:07+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:37:07+00:00` | `2026-04-12 20:37:07 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:17:45+00:00` | `2026-04-13 08:17:45 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:18:07+00:00` | `2026-04-13 08:18:07 (Lima)` |
| Última firma humana | `2026-04-13T13:20:19+00:00` | `2026-04-13 08:20:19 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.68 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:37:07 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:18:07 (Lima), es decir **11.68 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:37:04+00:00` | `2026-04-12 20:37:04 (Lima)` | -0.00h |
| 1 | FLORES VARGAS alfredo FIR 44617539 sw 80ac817949822fd5b688b20a20478e9b5d8e15bf | 44617539 | `2026-04-13T13:18:07+00:00` | `2026-04-13 08:18:07 (Lima)` | +11.68h |
| 2 | FERNANDEZ AUCCAPURI alexandra Diana FIR 75906106 sw 9286b52375d3c8f9022f7d2c4cec5b646dad2d15 | 75906106 | `2026-04-13T13:18:30+00:00` | `2026-04-13 08:18:30 (Lima)` | +11.69h |
| 3 | PADILLA DE LA CRUZ monica Antonieta FIR 09270956 sw 163068508bbf1f929e30fb69ffcb02b3bcc015b4 | 09270956 | `2026-04-13T13:20:19+00:00` | `2026-04-13 08:20:19 (Lima)` | +11.72h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **057161**
2. Descargar el PDF del acta
3. Verificar SHA-256: `0457c3f00bdde6e4a159ca77e6041e6fbc70eef5e973d23b4e5ff9633d0abda1`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
