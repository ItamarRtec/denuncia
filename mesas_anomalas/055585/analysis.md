# Mesa 055585 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.778545+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 6078 SANTA ROSA (código 13865)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 233
- Votos válidos: 219
- Participación: 77.926%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:06:59+00:00` | `2026-04-12 22:06:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:06:59+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:06:59+00:00` | `2026-04-12 22:06:59 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T07:48:05+00:00` | `2026-04-13 02:48:05 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T08:21:53+00:00` | `2026-04-13 03:21:53 (Lima)` |
| Última firma humana | `2026-04-13T08:22:12+00:00` | `2026-04-13 03:22:12 (Lima)` |

**Brecha primera firma humana vs publicación:** **+5.25 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:06:59 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 03:21:53 (Lima), es decir **5.25 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:06:59+00:00` | `2026-04-12 22:06:59 (Lima)` | +0.00h |
| 1 | ROMAN HUAMAN carmen Victoria FIR 09694256 sw 2b42f59bccc275f486dbfa47f954b87618a9b5b9 | 09694256 | `2026-04-13T08:21:53+00:00` | `2026-04-13 03:21:53 (Lima)` | +5.25h |
| 2 | SIANCAS GARCIA jorge Luis FIR 42217656 sw c52c438c309cf1a79c318725cfbfbfdbfb8c47d0 | 42217656 | `2026-04-13T08:22:03+00:00` | `2026-04-13 03:22:03 (Lima)` | +5.25h |
| 3 | REYMER FERNANDEZ sonia Yvonne FIR 08350674 sw 40532c39f4b4c4ab1eb9a1e369e7ca973ce37469 | 08350674 | `2026-04-13T08:22:12+00:00` | `2026-04-13 03:22:12 (Lima)` | +5.25h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055585**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2f6f35cb35a4c0cacb5a3c31b301888ed16539ea94e9823dcbb945afbaae1667`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
