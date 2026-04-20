# Mesa 039032 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.347461+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: BREÑA
- **Local de votación**: IEP ESPAÑA ADVENTISTA (código 2756)
- **Ubigeo**: 140104

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 251
- Votos válidos: 231
- Participación: 83.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:28:49+00:00` | `2026-04-12 20:28:49 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:28:49+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:28:49+00:00` | `2026-04-12 20:28:49 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:09:21+00:00` | `2026-04-13 08:09:21 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:09:44+00:00` | `2026-04-13 08:09:44 (Lima)` |
| Última firma humana | `2026-04-13T13:10:05+00:00` | `2026-04-13 08:10:05 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.68 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:28:49 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:09:44 (Lima), es decir **11.68 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:28:47+00:00` | `2026-04-12 20:28:47 (Lima)` | -0.00h |
| 1 | VILLANUEVA BASAURI rafael Eduardo FIR 09644957 sw 97b3afef9529fd13cc8f78f8dfef2487f44b3e93 | 09644957 | `2026-04-13T13:09:44+00:00` | `2026-04-13 08:09:44 (Lima)` | +11.68h |
| 2 | ZAVALA KONG jesus Ricardo FIR 06768210 sw 1862e18bb72b4fee341598f40202deefc1fbd5cb | 06768210 | `2026-04-13T13:10:05+00:00` | `2026-04-13 08:10:05 (Lima)` | +11.69h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **039032**
2. Descargar el PDF del acta
3. Verificar SHA-256: `9d6415a55399a402b8f8a3a8921c622b5264ebcfea818983d0e0df1763261dae`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
