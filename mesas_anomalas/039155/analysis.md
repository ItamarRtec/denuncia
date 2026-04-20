# Mesa 039155 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.860591+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: BREÑA
- **Local de votación**: IEP ALBERT EINSTEIN  I (código 52922)
- **Ubigeo**: 140104

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 232
- Votos válidos: 212
- Participación: 77.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:33:19+00:00` | `2026-04-12 20:33:19 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:33:19+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:33:19+00:00` | `2026-04-12 20:33:19 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:36:03+00:00` | `2026-04-12 21:36:03 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:36:17+00:00` | `2026-04-12 21:36:17 (Lima)` |
| Última firma humana | `2026-04-13T02:36:41+00:00` | `2026-04-12 21:36:41 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.05 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:33:19 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:36:17 (Lima), es decir **1.05 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:33:17+00:00` | `2026-04-12 20:33:17 (Lima)` | -0.00h |
| 1 | CUEVA PEREZ monick D'alexis FIR 77351103 sw bfef85af1f1635b2afe3648dc547c4a2abcbbde7 | 77351103 | `2026-04-13T02:36:17+00:00` | `2026-04-12 21:36:17 (Lima)` | +1.05h |
| 2 | FASABI TAPULLIMA mariela FIR 45559625 sw f4d1d15f672bdefee62ba5831293bf7869ff58ce | 45559625 | `2026-04-13T02:36:30+00:00` | `2026-04-12 21:36:30 (Lima)` | +1.05h |
| 3 | GODOY ZEGARRA luis Miguel FIR 70206379 sw 093f59324a66598e7533dd3a4c32fa63b5bd8121 | 70206379 | `2026-04-13T02:36:41+00:00` | `2026-04-12 21:36:41 (Lima)` | +1.06h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **039155**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c9bd23ed6b84a2979d0462309ecbacc0737fa745f9c57f3b3488c06af70e0d44`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
