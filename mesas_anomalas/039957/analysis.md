# Mesa 039957 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.062002+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CARABAYLLO
- **Local de votación**: IEP JUAN PABLO II (código 52888)
- **Ubigeo**: 140105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 229
- Votos válidos: 195
- Participación: 76.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:36:38+00:00` | `2026-04-12 21:36:38 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:36:38+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:36:38+00:00` | `2026-04-12 21:36:38 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T17:06:14+00:00` | `2026-04-13 12:06:14 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T17:06:50+00:00` | `2026-04-13 12:06:50 (Lima)` |
| Última firma humana | `2026-04-13T17:07:21+00:00` | `2026-04-13 12:07:21 (Lima)` |

**Brecha primera firma humana vs publicación:** **+14.50 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:36:38 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 12:06:50 (Lima), es decir **14.50 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:36:35+00:00` | `2026-04-12 21:36:35 (Lima)` | -0.00h |
| 1 | HUAMALI CRISTOBAL mariela FIR 76071607 sw a421c80b63ef8035d86138fedf52c2fc992d326a | 76071607 | `2026-04-13T17:06:50+00:00` | `2026-04-13 12:06:50 (Lima)` | +14.50h |
| 2 | HILARIO BLANCO jesus Javier FIR 10190365 sw 9fe9dd60c3edc7216d4573f500009cb7991977f8 | 10190365 | `2026-04-13T17:07:06+00:00` | `2026-04-13 12:07:06 (Lima)` | +14.51h |
| 3 | HOYOS AMARINGO tiffany Brissette FIR 76940776 sw 1d6c5f9ab758fcbb53a7deb8d2b444c2cfb35913 | 76940776 | `2026-04-13T17:07:21+00:00` | `2026-04-13 12:07:21 (Lima)` | +14.51h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **039957**
2. Descargar el PDF del acta
3. Verificar SHA-256: `0c937ce286db81e8e94f0d714868fd627bbd246501c9ca86ab407849d8f2ac38`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
