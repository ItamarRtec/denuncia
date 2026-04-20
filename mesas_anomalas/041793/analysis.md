# Mesa 041793 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.168985+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: IE 7042 SANTA TERESA DE VILLA (código 2866)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 241
- Votos válidos: 213
- Participación: 80.602%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:01:34+00:00` | `2026-04-12 22:01:34 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:01:34+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:01:34+00:00` | `2026-04-12 22:01:34 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:27:22+00:00` | `2026-04-13 09:27:22 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:27:54+00:00` | `2026-04-13 09:27:54 (Lima)` |
| Última firma humana | `2026-04-13T14:28:27+00:00` | `2026-04-13 09:28:27 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.44 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:01:34 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:27:54 (Lima), es decir **11.44 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:01:32+00:00` | `2026-04-12 22:01:32 (Lima)` | -0.00h |
| 1 | LEON GUEVARA maria Rosario FIR 07132038 sw d51c0cffd359950c5ab5f5f4885de1baaf5303b3 | 07132038 | `2026-04-13T14:27:54+00:00` | `2026-04-13 09:27:54 (Lima)` | +11.44h |
| 2 | LEON TAPIA maria Del Rosario FIR 20438175 sw 0575d31cba338dbf1c46142a40c37ff4a445af37 | 20438175 | `2026-04-13T14:28:14+00:00` | `2026-04-13 09:28:14 (Lima)` | +11.44h |
| 3 | IBARRA FRIAS roberto Andre FIR 73349472 sw 540a45f4de22f1f2d3c67d9e89d966e378804d3d | 73349472 | `2026-04-13T14:28:27+00:00` | `2026-04-13 09:28:27 (Lima)` | +11.45h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041793**
2. Descargar el PDF del acta
3. Verificar SHA-256: `83a2fc475b345d601818a91235ec7207e5c2df1be2f6dd833ada3f759f110976`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
