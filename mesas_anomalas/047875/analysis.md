# Mesa 047875 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.929302+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN ISIDRO
- **Local de votación**: IE EMBLEMATICA ALFONSO UGARTE - ESTADIO (código 53857)
- **Ubigeo**: 140124

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 297
- Votos emitidos: 202
- Votos válidos: 199
- Participación: 68.013%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:09:26+00:00` | `2026-04-12 20:09:26 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:09:26+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:09:26+00:00` | `2026-04-12 20:09:26 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:04:21+00:00` | `2026-04-12 22:04:21 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:05:15+00:00` | `2026-04-12 22:05:15 (Lima)` |
| Última firma humana | `2026-04-13T03:05:40+00:00` | `2026-04-12 22:05:40 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.93 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:09:26 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:05:15 (Lima), es decir **1.93 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:09:25+00:00` | `2026-04-12 20:09:25 (Lima)` | -0.00h |
| 1 | LUNA GUERRA maria Del Rocio FIR 10220151 sw 87e36005110d6d82e93c7a6d8a10f42d0c640a35 | 10220151 | `2026-04-13T03:05:15+00:00` | `2026-04-12 22:05:15 (Lima)` | +1.93h |
| 2 | LUNA HORNA camila FIR 73351446 sw 716e46349a695942e4a665a88b1c88f0fcc52686 | 73351446 | `2026-04-13T03:05:28+00:00` | `2026-04-12 22:05:28 (Lima)` | +1.93h |
| 3 | LUNA MEYZEN cesar Arturo FIR 42616895 sw eed515f2b703713939a19295e401c549e07dbca2 | 42616895 | `2026-04-13T03:05:40+00:00` | `2026-04-12 22:05:40 (Lima)` | +1.94h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **047875**
2. Descargar el PDF del acta
3. Verificar SHA-256: `851f27adf5a735b92cb2bbe7e10845192cb3514bbe27fa4194b8953eb36649c4`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
