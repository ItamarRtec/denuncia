# Mesa 054824 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.317964+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: EL AGUSTINO
- **Local de votación**: IEP APPU NUEVO PERU - ANEXO (código 54111)
- **Ubigeo**: 140135

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 223
- Votos válidos: 191
- Participación: 74.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:33:55+00:00` | `2026-04-12 20:33:55 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:33:55+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:33:55+00:00` | `2026-04-12 20:33:55 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:12:05+00:00` | `2026-04-12 22:12:05 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:12:34+00:00` | `2026-04-12 22:12:34 (Lima)` |
| Última firma humana | `2026-04-13T03:13:17+00:00` | `2026-04-12 22:13:17 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.64 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:33:55 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:12:34 (Lima), es decir **1.64 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:33:53+00:00` | `2026-04-12 20:33:53 (Lima)` | -0.00h |
| 1 | RIVERA RAMOS xiomara Magaly FIR 74613539 sw 5de46db942e0e621d19385fb5a636b38b85f4e07 | 74613539 | `2026-04-13T03:12:34+00:00` | `2026-04-12 22:12:34 (Lima)` | +1.64h |
| 2 | QUISPE RIVAS leea Krisstell FIR 70723882 sw a2bde1fb6e6ebf79a6287b79ac735b9617861e5c | 70723882 | `2026-04-13T03:12:43+00:00` | `2026-04-12 22:12:43 (Lima)` | +1.65h |
| 3 | RIVERA AQUINO valeria Ildeliza FIR 77269121 sw 379308388a04be0f3e0b02acc21b5825848c7096 | 77269121 | `2026-04-13T03:12:54+00:00` | `2026-04-12 22:12:54 (Lima)` | +1.65h |
| 4 | MIRANDA CABANA manuel Lorenzo FIR 09099361 sw 506830db6ec3fb5c6501bdfdec81ff58ab22fcbc | 09099361 | `2026-04-13T03:13:17+00:00` | `2026-04-12 22:13:17 (Lima)` | +1.66h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054824**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3132c0ed3a38f6ddab218f538d719377f403152ab1fb03a91d4fe98378249985`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
