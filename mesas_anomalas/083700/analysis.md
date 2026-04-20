# Mesa 083700 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.865045+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: VENTANILLA
- **Local de votación**: IE 5149 (código 23241)
- **Ubigeo**: 240106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 198
- Votos válidos: 165
- Participación: 66.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:41:04+00:00` | `2026-04-12 20:41:04 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:41:04+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:41:04+00:00` | `2026-04-12 20:41:04 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:44:54+00:00` | `2026-04-12 21:44:54 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:45:43+00:00` | `2026-04-12 21:45:43 (Lima)` |
| Última firma humana | `2026-04-13T02:46:52+00:00` | `2026-04-12 21:46:52 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.08 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:41:04 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:45:43 (Lima), es decir **1.08 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:41:02+00:00` | `2026-04-12 20:41:02 (Lima)` | -0.00h |
| 1 | FIGUEROA CURO josefina FIR 09753252 sw 8ce3d68c16172489fcb58c9f80e7ee4c00aa967e | 09753252 | `2026-04-13T02:45:43+00:00` | `2026-04-12 21:45:43 (Lima)` | +1.08h |
| 2 | CUSTODIO JAVIER eliar Eli FIR 72377836 sw 7082dc1fc6c968ff0375b7f83dcf8c81e179b719 | 72377836 | `2026-04-13T02:46:00+00:00` | `2026-04-12 21:46:00 (Lima)` | +1.08h |
| 3 | CRUZ CAMONES javier Frank FIR 70512546 sw c2010ff2e12c8efd0e46c0569ee0270096509d56 | 70512546 | `2026-04-13T02:46:23+00:00` | `2026-04-12 21:46:23 (Lima)` | +1.09h |
| 4 | QUISPE GABRIEL segundo Oswaldo FIR 08860596 sw fd880b16580d15762d526c732ea82181277520f9 | 08860596 | `2026-04-13T02:46:52+00:00` | `2026-04-12 21:46:52 (Lima)` | +1.10h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083700**
2. Descargar el PDF del acta
3. Verificar SHA-256: `ca32ea07f8eebd1d4a7632744018496e1ca24716b4ae2d0ccdc6df3786a996f0`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
