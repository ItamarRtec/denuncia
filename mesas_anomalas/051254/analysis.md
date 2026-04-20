# Mesa 051254 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.748202+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: ESTACIONAMIENTO 2 - UNIVERSIDAD DE LIMA (código 35748)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 171
- Votos válidos: 158
- Participación: 57.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:31:59+00:00` | `2026-04-12 20:31:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:31:59+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:31:59+00:00` | `2026-04-12 20:31:59 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T06:06:41+00:00` | `2026-04-13 01:06:41 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:08:03+00:00` | `2026-04-13 01:08:03 (Lima)` |
| Última firma humana | `2026-04-13T06:08:48+00:00` | `2026-04-13 01:08:48 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.60 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:31:59 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:08:03 (Lima), es decir **4.60 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:31:57+00:00` | `2026-04-12 20:31:57 (Lima)` | -0.00h |
| 1 | DEGGIMENA CRESPO jose Antonio FIR 46533107 sw 6547a0ca074f2e8e27a0687a58b9920b0611922a | 46533107 | `2026-04-13T06:08:03+00:00` | `2026-04-13 01:08:03 (Lima)` | +4.60h |
| 2 | DELGADO CASTRO cecilia Yngrid FIR 16466743 sw 7739a055def5e31ce1e7864b94f4fa90da2a4de8 | 16466743 | `2026-04-13T06:08:48+00:00` | `2026-04-13 01:08:48 (Lima)` | +4.61h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051254**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2b4003e624ae5ddc45baf68fa7b2fac2902e5f2d8d6e20f1ac7eda7cd3d05a17`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
