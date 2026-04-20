# Mesa 058788 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.987377+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN LUIS
- **Local de votación**: IE 1216 MIGUEL GRAU SEMINARIO (código 3481)
- **Ubigeo**: 140138

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 259
- Votos válidos: 242
- Participación: 86.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:12:43+00:00` | `2026-04-12 21:12:43 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:12:43+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:12:43+00:00` | `2026-04-12 21:12:43 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T09:45:50+00:00` | `2026-04-13 04:45:50 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T09:46:06+00:00` | `2026-04-13 04:46:06 (Lima)` |
| Última firma humana | `2026-04-13T09:48:56+00:00` | `2026-04-13 04:48:56 (Lima)` |

**Brecha primera firma humana vs publicación:** **+7.56 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:12:43 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 04:46:06 (Lima), es decir **7.56 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:12:41+00:00` | `2026-04-12 21:12:41 (Lima)` | -0.00h |
| 1 | ARIAS VELASQUEZ aurora Noemi FIR 40235386 sw be484ea334c4ce4ac8edcc32c5cca68379cfcf1b | 40235386 | `2026-04-13T09:46:06+00:00` | `2026-04-13 04:46:06 (Lima)` | +7.56h |
| 2 | CABREJOS CORDOVA silvia Soledad FIR 10180065 sw c51cf501c7cb32fc5fb5e66eaa1523610e3f46d3 | 10180065 | `2026-04-13T09:46:32+00:00` | `2026-04-13 04:46:32 (Lima)` | +7.56h |
| 3 | BURGA PAUCAR flor FIR 19336427 sw 113ff63a3ccd6cbebe27338d5ab5126fe703421e | 19336427 | `2026-04-13T09:47:20+00:00` | `2026-04-13 04:47:20 (Lima)` | +7.58h |
| 4 | CABELLO TINCO maria Soledad FIR 15429746 sw 057fd21ca52f0dec3c7b02d747c2e2df280e45a0 | 15429746 | `2026-04-13T09:48:56+00:00` | `2026-04-13 04:48:56 (Lima)` | +7.60h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **058788**
2. Descargar el PDF del acta
3. Verificar SHA-256: `f946646a0c897ee1187167aff069216a5f4e0bebe41837ca3ef0d4378580c98a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
