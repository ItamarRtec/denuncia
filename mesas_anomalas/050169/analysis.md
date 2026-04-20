# Mesa 050169 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.993633+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: CEGNE SANTA ANA (código 17362)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 262
- Votos válidos: 252
- Participación: 87.625%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:15:49+00:00` | `2026-04-12 21:15:49 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:15:49+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:15:49+00:00` | `2026-04-12 21:15:49 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:11:44+00:00` | `2026-04-13 08:11:44 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:31:58+00:00` | `2026-04-13 08:31:58 (Lima)` |
| Última firma humana | `2026-04-13T13:38:12+00:00` | `2026-04-13 08:38:12 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.27 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:15:49 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:31:58 (Lima), es decir **11.27 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:15:46+00:00` | `2026-04-12 21:15:46 (Lima)` | -0.00h |
| 1 | DIAZ RUIZ maria Esther FIR 25709814 sw e02d4d22e221677ad1866136b852a43984d7b4b9 | 25709814 | `2026-04-13T13:31:58+00:00` | `2026-04-13 08:31:58 (Lima)` | +11.27h |
| 2 | DIAZ SANCHEZ jose Manuel FIR 07764240 sw df3c2dd25f76638fbafbca85c17423c3864d4dbf | 07764240 | `2026-04-13T13:35:52+00:00` | `2026-04-13 08:35:52 (Lima)` | +11.33h |
| 3 | DOMINGUEZ ALVARADO maria Del Pilar FIR 10374501 sw 3d56cbb801bcfeb43fcc10122ac31c981808d2a8 | 10374501 | `2026-04-13T13:38:12+00:00` | `2026-04-13 08:38:12 (Lima)` | +11.37h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050169**
2. Descargar el PDF del acta
3. Verificar SHA-256: `9e83e59aba50259819031d5b050bb083a1d4f812a22c2e29374fcd51a5784856`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
