# Mesa 040976 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.302613+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IEP AL GORE (código 17984)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 235
- Votos válidos: 209
- Participación: 78.595%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:23:10+00:00` | `2026-04-12 22:23:10 (Lima)` |
| `C` | Contabilizada | `2026-04-13T01:54:05+00:00` | `2026-04-12 20:54:05 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:23:10+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:23:10+00:00` | `2026-04-12 22:23:10 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:48:49+00:00` | `2026-04-12 22:48:49 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:49:19+00:00` | `2026-04-12 22:49:19 (Lima)` |
| Última firma humana | `2026-04-13T03:49:57+00:00` | `2026-04-12 22:49:57 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.44 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:23:10 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:49:19 (Lima), es decir **0.44 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:54:03+00:00` | `2026-04-12 20:54:03 (Lima)` | -1.49h |
| 1 | BELTRAN ALBERCA jose Alfredo FIR 06885253 sw 27f6a70cb7416cc72040657da7cfba8a411c34fc | 06885253 | `2026-04-13T03:49:19+00:00` | `2026-04-12 22:49:19 (Lima)` | +0.44h |
| 2 | ALVILDO PACHECO marco Antonio FIR 42396925 sw 530fd625cfb0b7f573112e5de8fe67b043ba8d4e | 42396925 | `2026-04-13T03:49:37+00:00` | `2026-04-12 22:49:37 (Lima)` | +0.44h |
| 3 | GUERRERO VIDAL clara Zenaida FIR 06106532 sw ff30e70933d0e9261e72828a0646435f9e231349 | 06106532 | `2026-04-13T03:49:57+00:00` | `2026-04-12 22:49:57 (Lima)` | +0.45h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **040976**
2. Descargar el PDF del acta
3. Verificar SHA-256: `40a699d52d059d1349cbb3cb2545521b6a7eb2dd57f6e90077f8916c59d435ab`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
