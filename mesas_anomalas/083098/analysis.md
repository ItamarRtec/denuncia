# Mesa 083098 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.044274+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: VENTANILLA
- **Local de votación**: IE 5086 POLITECNICO DE VENTANILLA (código 4862)
- **Ubigeo**: 240106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 261
- Votos válidos: 206
- Participación: 87.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:50:51+00:00` | `2026-04-12 19:50:51 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:50:51+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:50:51+00:00` | `2026-04-12 19:50:51 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:23:52+00:00` | `2026-04-12 21:23:52 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:24:19+00:00` | `2026-04-12 21:24:19 (Lima)` |
| Última firma humana | `2026-04-13T02:24:45+00:00` | `2026-04-12 21:24:45 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.56 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:50:51 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:24:19 (Lima), es decir **1.56 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:50:49+00:00` | `2026-04-12 19:50:49 (Lima)` | -0.00h |
| 1 | OSORIO VIERA luis Alberto FIR 40709247 sw 28a936e1d9fbdcdc19a8a69a7f454fafb239ea05 | 40709247 | `2026-04-13T02:24:19+00:00` | `2026-04-12 21:24:19 (Lima)` | +1.56h |
| 2 | MONTALVAN CALLA mari Martha Lizet FIR 46312400 sw b90267439da17135a91454b6794acb16ee973111 | 46312400 | `2026-04-13T02:24:45+00:00` | `2026-04-12 21:24:45 (Lima)` | +1.56h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083098**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5d0b0d45f8436cdd21a492c20fbab1dd8f50123b2d79be427e6da18444a04acb`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
