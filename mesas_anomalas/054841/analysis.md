# Mesa 054841 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.384457+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: EL AGUSTINO
- **Local de votación**: IE 048 SAN JUAN BOSCO (código 55416)
- **Ubigeo**: 140135

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 219
- Votos válidos: 195
- Participación: 73.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:19:32+00:00` | `2026-04-12 22:19:32 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:19:32+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:19:32+00:00` | `2026-04-12 22:19:32 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:42:13+00:00` | `2026-04-13 07:42:13 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:50:51+00:00` | `2026-04-13 07:50:51 (Lima)` |
| Última firma humana | `2026-04-13T12:55:26+00:00` | `2026-04-13 07:55:26 (Lima)` |

**Brecha primera firma humana vs publicación:** **+9.52 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:19:32 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:50:51 (Lima), es decir **9.52 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:19:31+00:00` | `2026-04-12 22:19:31 (Lima)` | -0.00h |
| 1 | ROJAS PANDO edynson Rafael FIR 73970962 sw 603930bdd3cce17ef4054b6b3d83c7e5e4f1bdf3 | 73970962 | `2026-04-13T12:50:51+00:00` | `2026-04-13 07:50:51 (Lima)` | +9.52h |
| 2 | RISCO MIRANO julio David FIR 45368302 sw 4219cfe4d2776dc9896f1500da303320e4c3faa8 | 45368302 | `2026-04-13T12:53:48+00:00` | `2026-04-13 07:53:48 (Lima)` | +9.57h |
| 3 | RODRIGUEZ ALEJOS nicholl Antuannete FIR 78632777 sw 9afd8a1ae6d4258738fb401ef977d91433c96d65 | 78632777 | `2026-04-13T12:55:26+00:00` | `2026-04-13 07:55:26 (Lima)` | +9.60h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054841**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e2a06f1d15f16a98074dab7a04f2b657090c0ad33f0c0cbc42213c62ae62eb8f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
