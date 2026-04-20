# Mesa 051766 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.235027+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: IE EMBLEMATICA RICARDO PALMA (código 3232)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 244
- Votos válidos: 218
- Participación: 81.605%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:51:01+00:00` | `2026-04-12 20:51:01 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:51:01+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:51:01+00:00` | `2026-04-12 20:51:01 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:05:46+00:00` | `2026-04-13 00:05:46 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:06:00+00:00` | `2026-04-13 00:06:00 (Lima)` |
| Última firma humana | `2026-04-13T05:06:36+00:00` | `2026-04-13 00:06:36 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.25 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:51:01 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:06:00 (Lima), es decir **3.25 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:50:59+00:00` | `2026-04-12 20:50:59 (Lima)` | -0.00h |
| 1 | MONTERO AMESQUITA maria Isabel FIR 08880434 sw 27f0b351cb5a828e404d46e7ffda3412665d6391 | 08880434 | `2026-04-13T05:06:00+00:00` | `2026-04-13 00:06:00 (Lima)` | +3.25h |
| 2 | MORANTE ALVAN jorge Daniel FIR 44633211 sw 2257fdd849089d7692aa8a9ed337957b96074575 | 44633211 | `2026-04-13T05:06:19+00:00` | `2026-04-13 00:06:19 (Lima)` | +3.25h |
| 3 | MURILLO VILCHEZ elizabeth Jessica FIR 29648813 sw 0118b815e46306a8644213bd4e72e8eb970a69c9 | 29648813 | `2026-04-13T05:06:36+00:00` | `2026-04-13 00:06:36 (Lima)` | +3.26h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051766**
2. Descargar el PDF del acta
3. Verificar SHA-256: `1c67f99f1596d1fdaab18c754b9582d9ba54e22a38e0b0f85d4e146594133e59`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
