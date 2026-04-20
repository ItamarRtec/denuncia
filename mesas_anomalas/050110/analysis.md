# Mesa 050110 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.241792+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: IESTP MARIA ROSARIO ARAOZ PINTO (código 3181)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 247
- Votos válidos: 228
- Participación: 82.609%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:09:10+00:00` | `2026-04-12 21:09:10 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:09:10+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:09:10+00:00` | `2026-04-12 21:09:10 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:39:10+00:00` | `2026-04-13 08:39:10 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:39:22+00:00` | `2026-04-13 08:39:22 (Lima)` |
| Última firma humana | `2026-04-13T13:39:49+00:00` | `2026-04-13 08:39:49 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.50 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:09:10 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:39:22 (Lima), es decir **11.50 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:09:08+00:00` | `2026-04-12 21:09:08 (Lima)` | -0.00h |
| 1 | LINARES JAMIS haila Jahmil FIR 70898876 sw 0b14a89a28ada3bb6dcf4169c18ecce5aea23c7b | 70898876 | `2026-04-13T13:39:22+00:00` | `2026-04-13 08:39:22 (Lima)` | +11.50h |
| 2 | LAZARTE HAYASHI ana Maria FIR 07259616 sw 959761ad09fefbd72bf900d0d06f25c4dd068e01 | 07259616 | `2026-04-13T13:39:41+00:00` | `2026-04-13 08:39:41 (Lima)` | +11.51h |
| 3 | LEDESMA DAVALOS silvia Nancy FIR 07595982 sw 6aafa85dcd95a24333a5693c413160ef697247a0 | 07595982 | `2026-04-13T13:39:49+00:00` | `2026-04-13 08:39:49 (Lima)` | +11.51h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050110**
2. Descargar el PDF del acta
3. Verificar SHA-256: `be85640caf701cf2a3e52590b4bdc2abb49cd186a8c328a1f9061de3ff1efbc0`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
