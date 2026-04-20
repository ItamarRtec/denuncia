# Mesa 054858 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.620093+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 629 6034 CESAR CARBONELL RODRIGUEZ (código 3347)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 229
- Votos válidos: 213
- Participación: 76.589%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:30:04+00:00` | `2026-04-12 21:30:04 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:30:04+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:30:04+00:00` | `2026-04-12 21:30:04 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T10:07:01+00:00` | `2026-04-13 05:07:01 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T10:07:35+00:00` | `2026-04-13 05:07:35 (Lima)` |
| Última firma humana | `2026-04-13T10:08:12+00:00` | `2026-04-13 05:08:12 (Lima)` |

**Brecha primera firma humana vs publicación:** **+7.63 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:30:04 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 05:07:35 (Lima), es decir **7.63 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:30:02+00:00` | `2026-04-12 21:30:02 (Lima)` | -0.00h |
| 1 | DEPAZ POMIANO lila Floribertha FIR 09989152 sw 4667e869b5a1ba056dfb1ab32c244ee6178793e6 | 09989152 | `2026-04-13T10:07:35+00:00` | `2026-04-13 05:07:35 (Lima)` | +7.63h |
| 2 | DEZA GUERRERO maria Elizabeth FIR 09288282 sw 483c621d98a9ad570b45dbd2d8ad772e8872ed1d | 09288282 | `2026-04-13T10:07:53+00:00` | `2026-04-13 05:07:53 (Lima)` | +7.63h |
| 3 | DOMINGUEZ VALENCIA miriam Elena FIR 40870560 sw 21e95fab2215b96cc16c9b5377e40f1218f207b2 | 40870560 | `2026-04-13T10:08:12+00:00` | `2026-04-13 05:08:12 (Lima)` | +7.64h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054858**
2. Descargar el PDF del acta
3. Verificar SHA-256: `74514816d6bb36e71f4f34fa3b883687fb7fa7adc85a5b27f6a1bc6df1a1c86d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
