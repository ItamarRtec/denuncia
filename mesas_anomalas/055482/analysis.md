# Mesa 055482 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.559597+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IEP SACO OLIVEROS (código 3384)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 255
- Votos válidos: 229
- Participación: 85.284%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:19:14+00:00` | `2026-04-12 21:19:14 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:19:14+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:19:14+00:00` | `2026-04-12 21:19:14 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:05:33+00:00` | `2026-04-13 00:05:33 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:07:09+00:00` | `2026-04-13 00:07:09 (Lima)` |
| Última firma humana | `2026-04-13T05:07:32+00:00` | `2026-04-13 00:07:32 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.80 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:19:14 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:07:09 (Lima), es decir **2.80 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:18:02+00:00` | `2026-04-12 21:18:02 (Lima)` | -0.02h |
| 1 | TITO OLANO barbara Raquel FIR 47704771 sw ee6ad77d2e26f41760aacca26857f58c4f511747 | 47704771 | `2026-04-13T05:07:09+00:00` | `2026-04-13 00:07:09 (Lima)` | +2.80h |
| 2 | VELASQUEZ GARCIA richard Johnny FIR 09584084 sw ff6e29b2dc9253f824a8513233a244720fe9777a | 09584084 | `2026-04-13T05:07:23+00:00` | `2026-04-13 00:07:23 (Lima)` | +2.80h |
| 3 | UBILLUS QUISPE jose Ricardo FIR 43892083 sw 10165953d11eebeff9e2d534c825481772ea636f | 43892083 | `2026-04-13T05:07:32+00:00` | `2026-04-13 00:07:32 (Lima)` | +2.81h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055482**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5a4fbfbd676820f0317cab2a1a9d705239c5f894186ff654d156e2606976ee80`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
