# Mesa 083035 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.511916+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: LA PERLA
- **Local de votación**: IEPM COLEGIO MILITAR LEONCIO PRADO (código 40913)
- **Ubigeo**: 240105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 222
- Votos válidos: 204
- Participación: 74.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:59:27+00:00` | `2026-04-12 21:59:27 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:59:27+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:59:27+00:00` | `2026-04-12 21:59:27 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:20:10+00:00` | `2026-04-13 09:20:10 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:20:27+00:00` | `2026-04-13 09:20:27 (Lima)` |
| Última firma humana | `2026-04-13T14:21:35+00:00` | `2026-04-13 09:21:35 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.35 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:59:27 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:20:27 (Lima), es decir **11.35 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:59:24+00:00` | `2026-04-12 21:59:24 (Lima)` | -0.00h |
| 1 | VALENCIA GOMEZ VELASQUEZ nelda Angelica FIR 70808577 sw bac034b308e52fe734a29b1e0d68340eab686e7f | 70808577 | `2026-04-13T14:20:27+00:00` | `2026-04-13 09:20:27 (Lima)` | +11.35h |
| 2 | VASQUEZ BOBADILLA adrian Alonso FIR 74208012 sw c4721bf3f3708cb99d1735e0c9d1083aee6116bd | 74208012 | `2026-04-13T14:20:55+00:00` | `2026-04-13 09:20:55 (Lima)` | +11.36h |
| 3 | ESPINOZA SALINAS sugei Katrina FIR 75254607 sw aa3bea84dc4ef0744605a50c275c0de614125346 | 75254607 | `2026-04-13T14:21:35+00:00` | `2026-04-13 09:21:35 (Lima)` | +11.37h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083035**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3966ec048272cae4af0bf85749ec6fe0c1e11b59bac655ab8a4783be9891b029`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
