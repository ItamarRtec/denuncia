# Mesa 054905 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.349698+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 6037 INCA PACHACUTEC - SECUNDARIA (código 3349)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 229
- Votos válidos: 200
- Participación: 76.589%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:44:16+00:00` | `2026-04-12 21:44:16 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:44:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:44:16+00:00` | `2026-04-12 21:44:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:16:48+00:00` | `2026-04-13 09:16:48 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:17:24+00:00` | `2026-04-13 09:17:24 (Lima)` |
| Última firma humana | `2026-04-13T14:17:49+00:00` | `2026-04-13 09:17:49 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.55 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:44:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:17:24 (Lima), es decir **11.55 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:44:14+00:00` | `2026-04-12 21:44:14 (Lima)` | -0.00h |
| 1 | VELASQUEZ GRANADOS jordy Mario FIR 47927466 sw 1ca212366a2bf7c7ca1d4fa6b2999d6d30764671 | 47927466 | `2026-04-13T14:17:24+00:00` | `2026-04-13 09:17:24 (Lima)` | +11.55h |
| 2 | VENTOCILLA CORNEJO marlene Janet FIR 09977337 sw fb6861732be0f15a224f054f1914e4945ac6e72a | 09977337 | `2026-04-13T14:17:37+00:00` | `2026-04-13 09:17:37 (Lima)` | +11.56h |
| 3 | VALENCIA QUISPE miguel Angel FIR 42194893 sw 8881418b4e81d2ed54bbe6e01af9608395b3b540 | 42194893 | `2026-04-13T14:17:49+00:00` | `2026-04-13 09:17:49 (Lima)` | +11.56h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054905**
2. Descargar el PDF del acta
3. Verificar SHA-256: `41f7743c25b8c3ba3a43fc8c6e46922f23db280e3f92f8e6dbd13b34edf09016`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
