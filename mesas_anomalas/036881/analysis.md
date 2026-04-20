# Mesa 036881 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.618822+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: UNIVERSIDAD NACIONAL FEDERICO VILLARREAL SEDE LOCAL 07 (código 34867)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 242
- Votos válidos: 223
- Participación: 80.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:23:04+00:00` | `2026-04-12 22:23:04 (Lima)` |
| `C` | Contabilizada | `2026-04-13T03:22:11+00:00` | `2026-04-12 22:22:11 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:23:04+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:23:04+00:00` | `2026-04-12 22:23:04 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:52:51+00:00` | `2026-04-13 09:52:51 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:53:09+00:00` | `2026-04-13 09:53:09 (Lima)` |
| Última firma humana | `2026-04-13T14:53:34+00:00` | `2026-04-13 09:53:34 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.50 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:23:04 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:53:09 (Lima), es decir **11.50 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:22:08+00:00` | `2026-04-12 22:22:08 (Lima)` | -0.02h |
| 1 | VASQUEZ FERNANDEZ markos FIR 40688753 sw ea9ac8af260731c6bbaa65c56fb9d2b0d908aee5 | 40688753 | `2026-04-13T14:53:09+00:00` | `2026-04-13 09:53:09 (Lima)` | +11.50h |
| 2 | VARGAS CARPIO edgar Martin FIR 43226734 sw e7a1064ae0602e0b6f71509f128efd1880b44fc2 | 43226734 | `2026-04-13T14:53:22+00:00` | `2026-04-13 09:53:22 (Lima)` | +11.51h |
| 3 | ULLOA CRUZADO consuelo Rosa FIR 43670401 sw 69e3fabae4b8a6710df2ca01bad4f97688f3c5c9 | 43670401 | `2026-04-13T14:53:34+00:00` | `2026-04-13 09:53:34 (Lima)` | +11.51h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036881**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3e235790e34f2d83662c8bbe238ed50065046d674f0643e453ae82886c6cbb95`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
