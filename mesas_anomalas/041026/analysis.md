# Mesa 041026 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.472252+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IEP MARIA MONTESSORI STOPPIANI (código 32951)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 218
- Votos válidos: 189
- Participación: 72.91%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:00:25+00:00` | `2026-04-12 22:00:25 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:00:25+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:00:25+00:00` | `2026-04-12 22:00:25 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:29:29+00:00` | `2026-04-13 08:29:29 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:51:29+00:00` | `2026-04-13 08:51:29 (Lima)` |
| Última firma humana | `2026-04-13T14:00:39+00:00` | `2026-04-13 09:00:39 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.85 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:00:25 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:51:29 (Lima), es decir **10.85 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:00:23+00:00` | `2026-04-12 22:00:23 (Lima)` | -0.00h |
| 1 | GONZALES MARIN roxana FIR 43765550 sw 49882dd33a1725eb2a1545f2268dacff7ec20c02 | 43765550 | `2026-04-13T13:51:29+00:00` | `2026-04-13 08:51:29 (Lima)` | +10.85h |
| 2 | HUARANGA BANDAN donatila Eulalia FIR 09017048 sw ac4a39bac73674c59539f6e607e43ae78d754093 | 09017048 | `2026-04-13T13:56:56+00:00` | `2026-04-13 08:56:56 (Lima)` | +10.94h |
| 3 | HONORIO TIRADO juan Enrique FIR 06841503 sw 97d47e4c2626de8883ab8cc117ac4d73900c4226 | 06841503 | `2026-04-13T14:00:39+00:00` | `2026-04-13 09:00:39 (Lima)` | +11.00h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041026**
2. Descargar el PDF del acta
3. Verificar SHA-256: `7868e1d7880ffab001953a4975fb41eca7c86807f53b83f571e62fafaf9d2b68`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
