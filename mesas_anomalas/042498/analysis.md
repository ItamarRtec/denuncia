# Mesa 042498 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.714692+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: IEP INNOVA SCHOOLS - CHORRILLOS LA CAMPIÑA (código 54784)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 247
- Votos válidos: 221
- Participación: 82.609%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:33:00+00:00` | `2026-04-12 20:33:00 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:33:00+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:33:00+00:00` | `2026-04-12 20:33:00 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:08:59+00:00` | `2026-04-12 22:08:59 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:17:03+00:00` | `2026-04-12 22:17:03 (Lima)` |
| Última firma humana | `2026-04-13T03:17:32+00:00` | `2026-04-12 22:17:32 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.73 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:33:00 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:17:03 (Lima), es decir **1.73 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:32:58+00:00` | `2026-04-12 20:32:58 (Lima)` | -0.00h |
| 1 | ARROYO PORRAS valeria Marcela FIR 70836873 sw 5c6db831725429de6bdf6b94c9eb87fcd93f9405 | 70836873 | `2026-04-13T03:17:03+00:00` | `2026-04-12 22:17:03 (Lima)` | +1.73h |
| 2 | ARAJA LLAMOCCA edmundo FIR 10632966 sw 18a6f399971f90665346ed079ad42ec72e99e4ab | 10632966 | `2026-04-13T03:17:17+00:00` | `2026-04-12 22:17:17 (Lima)` | +1.74h |
| 3 | ANGELES CHIRINOS erika Julissa FIR 42224079 sw 6b29a3916ed60a378dffbf195c746ee48d342fc1 | 42224079 | `2026-04-13T03:17:32+00:00` | `2026-04-12 22:17:32 (Lima)` | +1.74h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042498**
2. Descargar el PDF del acta
3. Verificar SHA-256: `35fb0f1da97e01e4d9a34b45f3706b2f00737aa79bf5e9a2c43ef914c8d2904d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
