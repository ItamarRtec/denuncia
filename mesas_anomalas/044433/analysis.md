# Mesa 044433 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.184221+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LURIGANCHO
- **Local de votación**: IEP FRANCOIS VIETE (código 13462)
- **Ubigeo**: 140112

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 231
- Votos válidos: 192
- Participación: 77.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:59:20+00:00` | `2026-04-12 19:59:20 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:59:20+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:59:20+00:00` | `2026-04-12 19:59:20 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T01:55:55+00:00` | `2026-04-12 20:55:55 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T01:56:32+00:00` | `2026-04-12 20:56:32 (Lima)` |
| Última firma humana | `2026-04-13T01:57:06+00:00` | `2026-04-12 20:57:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.95 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:59:20 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 20:56:32 (Lima), es decir **0.95 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:59:18+00:00` | `2026-04-12 19:59:18 (Lima)` | -0.00h |
| 1 | YUPANQUI SINCHE raul FIR 42280656 sw ef1f7a2f023a23aca913917848faf2c9d4f9b632 | 42280656 | `2026-04-13T01:56:32+00:00` | `2026-04-12 20:56:32 (Lima)` | +0.95h |
| 2 | VALER HUARANGA ariana Amy FIR 61342618 sw 2acc463de0179301b48eb3ba9086cdb96e93097e | 61342618 | `2026-04-13T01:56:51+00:00` | `2026-04-12 20:56:51 (Lima)` | +0.96h |
| 3 | VILLALVA MORENO flavio FIR 74241840 sw 7a3591875ff6965f1b8cfe3581f199affe26c8e6 | 74241840 | `2026-04-13T01:57:06+00:00` | `2026-04-12 20:57:06 (Lima)` | +0.96h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **044433**
2. Descargar el PDF del acta
3. Verificar SHA-256: `7429f76d5c46af0159cada5caf8381cb990aa6bfd5cb7dde45421b7b23158602`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
