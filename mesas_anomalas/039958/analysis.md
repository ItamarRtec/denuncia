# Mesa 039958 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.304508+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CARABAYLLO
- **Local de votación**: IEP JUAN PABLO II (código 52888)
- **Ubigeo**: 140105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 219
- Votos válidos: 191
- Participación: 73.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:18:55+00:00` | `2026-04-12 22:18:55 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:18:55+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:18:55+00:00` | `2026-04-12 22:18:55 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:46:09+00:00` | `2026-04-13 09:46:09 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:47:05+00:00` | `2026-04-13 09:47:05 (Lima)` |
| Última firma humana | `2026-04-13T14:47:32+00:00` | `2026-04-13 09:47:32 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.47 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:18:55 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:47:05 (Lima), es decir **11.47 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:18:52+00:00` | `2026-04-12 22:18:52 (Lima)` | -0.00h |
| 1 | ILQUIN LOPEZ jefferson Jeanpierre FIR 73988626 sw 3715372fea256d59110560f84049510450aa6395 | 73988626 | `2026-04-13T14:47:05+00:00` | `2026-04-13 09:47:05 (Lima)` | +11.47h |
| 2 | JUNCO PALOMINO anais Mariel FIR 73747067 sw 7e996854329b748d7c3447f0999a2edb7a84b51d | 73747067 | `2026-04-13T14:47:17+00:00` | `2026-04-13 09:47:17 (Lima)` | +11.47h |
| 3 | LAZO PAREDES giancarlo Junior FIR 70157560 sw 2a2249a56dc25709c1ec4df0ddcdf585c61b432c | 70157560 | `2026-04-13T14:47:32+00:00` | `2026-04-13 09:47:32 (Lima)` | +11.48h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **039958**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4652ceb507b5833395891a038889d57042d10cc63c32247d8a410eb764a92031`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
