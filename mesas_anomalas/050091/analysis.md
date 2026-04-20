# Mesa 050091 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.771386+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: IEP BUENAS NUEVAS (código 3175)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 254
- Votos válidos: 232
- Participación: 84.95%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:12:38+00:00` | `2026-04-12 21:12:38 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:12:38+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:12:38+00:00` | `2026-04-12 21:12:38 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:05:35+00:00` | `2026-04-13 00:05:35 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:06:19+00:00` | `2026-04-13 00:06:19 (Lima)` |
| Última firma humana | `2026-04-13T05:06:30+00:00` | `2026-04-13 00:06:30 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.89 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:12:38 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:06:19 (Lima), es decir **2.89 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:12:36+00:00` | `2026-04-12 21:12:36 (Lima)` | -0.00h |
| 1 | YARNOLD VILNER abraham Jose Alberto FIR 70413980 sw 129fb6b6c1d91fafe9c4b6617f088de177108c88 | 70413980 | `2026-04-13T05:06:19+00:00` | `2026-04-13 00:06:19 (Lima)` | +2.89h |
| 2 | VASQUEZ SUAREZ winston Adolfo FIR 43431015 sw 79c1218bd32579b013804221054888731c16ba4a | 43431015 | `2026-04-13T05:06:30+00:00` | `2026-04-13 00:06:30 (Lima)` | +2.90h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050091**
2. Descargar el PDF del acta
3. Verificar SHA-256: `de05d0dcb819982695872fa5034f271f1cbe7f16fd0d0be6f2ddc99f0a38fac1`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
