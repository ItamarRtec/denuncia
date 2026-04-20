# Mesa 040417 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.743615+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IE FE Y ALEGRIA 10 (código 2828)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 254
- Votos válidos: 226
- Participación: 84.95%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:55:35+00:00` | `2026-04-12 21:55:35 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:55:35+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:55:35+00:00` | `2026-04-12 21:55:35 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T11:17:08+00:00` | `2026-04-13 06:17:08 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T11:17:21+00:00` | `2026-04-13 06:17:21 (Lima)` |
| Última firma humana | `2026-04-13T11:17:58+00:00` | `2026-04-13 06:17:58 (Lima)` |

**Brecha primera firma humana vs publicación:** **+8.36 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:55:35 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 06:17:21 (Lima), es decir **8.36 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:51:07+00:00` | `2026-04-12 21:51:07 (Lima)` | -0.07h |
| 1 | ALFARO AROTINCO mercedes Yolanda FIR 09476927 sw 076fb58acfcbef6342844a716fbd242f3522b003 | 09476927 | `2026-04-13T11:17:21+00:00` | `2026-04-13 06:17:21 (Lima)` | +8.36h |
| 2 | AGUIRRE ELLEN piero FIR 74585310 sw e22352a26d870acd914132a0f771e62eff3bcf58 | 74585310 | `2026-04-13T11:17:45+00:00` | `2026-04-13 06:17:45 (Lima)` | +8.37h |
| 3 | APARICIO QUESADA julio Cesar FIR 41819032 sw 533bf8f295ca6d3a14ef9f5b232b5523ed133c10 | 41819032 | `2026-04-13T11:17:58+00:00` | `2026-04-13 06:17:58 (Lima)` | +8.37h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **040417**
2. Descargar el PDF del acta
3. Verificar SHA-256: `20bf1b04699676fb8d65f014f4afaffd941f345f054a34d609a3e69e85cb52d7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
