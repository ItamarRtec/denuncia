# Mesa 057325 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.864165+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IEI 0079 CUNA JARDIN (código 13724)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 208
- Votos válidos: 171
- Participación: 69.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:43:43+00:00` | `2026-04-12 20:43:43 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:43:43+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:43:43+00:00` | `2026-04-12 20:43:43 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:59:57+00:00` | `2026-04-13 00:59:57 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:00:19+00:00` | `2026-04-13 01:00:19 (Lima)` |
| Última firma humana | `2026-04-13T06:00:57+00:00` | `2026-04-13 01:00:57 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.28 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:43:43 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:00:19 (Lima), es decir **4.28 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:43:41+00:00` | `2026-04-12 20:43:41 (Lima)` | -0.00h |
| 1 | VILA LIVIAS gian Pool Alexander FIR 76276707 sw d5372b9528e2543f87b3dbf9e647f9ac439aa599 | 76276707 | `2026-04-13T06:00:19+00:00` | `2026-04-13 01:00:19 (Lima)` | +4.28h |
| 2 | SILVERA PAREDES claudia Fabiola FIR 75539416 sw 52c9aa98792eeee39c1120156aae7dbc58617137 | 75539416 | `2026-04-13T06:00:31+00:00` | `2026-04-13 01:00:31 (Lima)` | +4.28h |
| 3 | TINEO HUAMANI juan Carlos FIR 06284382 sw c7fd329a22510fd8c57dd9b135ec86d4cf3fb8f3 | 06284382 | `2026-04-13T06:00:43+00:00` | `2026-04-13 01:00:43 (Lima)` | +4.28h |
| 4 | DIONICIO FABIAN wilde Gustavo FIR 10657238 sw 81b2edea0c8acce4ed50f35e2ed62df53d2b57dd | 10657238 | `2026-04-13T06:00:57+00:00` | `2026-04-13 01:00:57 (Lima)` | +4.29h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **057325**
2. Descargar el PDF del acta
3. Verificar SHA-256: `eb45196f3b355231fb13f091fdf4b1021813c8ee1edab06882bb8ac2ff2a9330`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
