# Mesa 053041 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.040167+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IEP REINA CARMELITA (código 14417)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 230
- Votos emitidos: 151
- Votos válidos: 121
- Participación: 65.652%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:55:39+00:00` | `2026-04-12 21:55:39 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:55:39+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:55:39+00:00` | `2026-04-12 21:55:39 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:02:50+00:00` | `2026-04-13 09:02:50 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:03:13+00:00` | `2026-04-13 09:03:13 (Lima)` |
| Última firma humana | `2026-04-13T14:03:50+00:00` | `2026-04-13 09:03:50 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.13 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:55:39 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:03:13 (Lima), es decir **11.13 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:55:37+00:00` | `2026-04-12 21:55:37 (Lima)` | -0.00h |
| 1 | ALBINO CONTRERAS mathias Esteban FIR 61293947 sw 670bfc7103790b8c95a3a04f4f55793c7c7ad30f | 61293947 | `2026-04-13T14:03:13+00:00` | `2026-04-13 09:03:13 (Lima)` | +11.13h |
| 2 | ARTEAGA BOHORQUEZ sebastian Jesus FIR 60977466 sw 95c0905de3d037e65e90c38a25960ed8b5c4baa6 | 60977466 | `2026-04-13T14:03:31+00:00` | `2026-04-13 09:03:31 (Lima)` | +11.13h |
| 3 | ATAUCUSI HUAMANI natali Victoria FIR 60990600 sw 69e56264a2a13235be30cf54c03a799f8bc02243 | 60990600 | `2026-04-13T14:03:50+00:00` | `2026-04-13 09:03:50 (Lima)` | +11.14h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **053041**
2. Descargar el PDF del acta
3. Verificar SHA-256: `278f0f3e281bca7345bacf949ba7aa6c40570cf77d11604f60ea33d6e4405d36`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
