# Mesa 050900 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.306348+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IEP SANTA MARIA DE SURCO (código 3215)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 247
- Votos válidos: 213
- Participación: 82.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:06:06+00:00` | `2026-04-12 20:06:06 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:06:06+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:06:06+00:00` | `2026-04-12 20:06:06 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T06:18:12+00:00` | `2026-04-13 01:18:12 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:18:42+00:00` | `2026-04-13 01:18:42 (Lima)` |
| Última firma humana | `2026-04-13T06:19:23+00:00` | `2026-04-13 01:19:23 (Lima)` |

**Brecha primera firma humana vs publicación:** **+5.21 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:06:06 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:18:42 (Lima), es decir **5.21 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:06:04+00:00` | `2026-04-12 20:06:04 (Lima)` | -0.00h |
| 1 | CORDOVA AGUILAR hugo FIR 10190061 sw 28590d931310aec0dad4a9b2aaa3d908ac7c7c39 | 10190061 | `2026-04-13T06:18:42+00:00` | `2026-04-13 01:18:42 (Lima)` | +5.21h |
| 2 | FONSECA ORBE daniela Antuaned FIR 61032473 sw c744da595d714ea051162327de13b31aebb98c27 | 61032473 | `2026-04-13T06:19:03+00:00` | `2026-04-13 01:19:03 (Lima)` | +5.22h |
| 3 | GARCIA ESPINOZA jesus Alexsi FIR 44891876 sw 4c3d9fd01e72b1a91f6ea9f5c74a49428ddd1379 | 44891876 | `2026-04-13T06:19:23+00:00` | `2026-04-13 01:19:23 (Lima)` | +5.22h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050900**
2. Descargar el PDF del acta
3. Verificar SHA-256: `d731c085f7eccc8b5ec8d0fc4e938a6f9e6565ede84e478a22d2593b99b98948`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
