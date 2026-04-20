# Mesa 083898 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.418128+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: VENTANILLA
- **Local de votación**: IEP SAN JUAN DE DIOS TODOPODEROSO (código 54284)
- **Ubigeo**: 240106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 243
- Votos válidos: 220
- Participación: 81.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:09:29+00:00` | `2026-04-12 22:09:29 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:09:29+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:09:29+00:00` | `2026-04-12 22:09:29 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:07:15+00:00` | `2026-04-13 09:07:15 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:07:28+00:00` | `2026-04-13 09:07:28 (Lima)` |
| Última firma humana | `2026-04-13T14:07:52+00:00` | `2026-04-13 09:07:52 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.97 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:09:29 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:07:28 (Lima), es decir **10.97 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:09:28+00:00` | `2026-04-12 22:09:28 (Lima)` | -0.00h |
| 1 | DIAPIZ CHUQUIZUTA gianella FIR 73434270 sw 81dfb4284453fb8190a6709d66a06e27bfc2c5b2 | 73434270 | `2026-04-13T14:07:28+00:00` | `2026-04-13 09:07:28 (Lima)` | +10.97h |
| 2 | ERAZO BENITES DE LIMO flor Yolanda FIR 25691221 sw 8deb5a368251687ba4f7a96b5825757b6ec6302c | 25691221 | `2026-04-13T14:07:40+00:00` | `2026-04-13 09:07:40 (Lima)` | +10.97h |
| 3 | GAMARRA RAMIREZ roxana FIR 40909323 sw fc1aef9fcfe189acf58998552cc9a61e0cffa6b9 | 40909323 | `2026-04-13T14:07:52+00:00` | `2026-04-13 09:07:52 (Lima)` | +10.97h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083898**
2. Descargar el PDF del acta
3. Verificar SHA-256: `12fd4457db8301d7d5f5ef08f9d04fd0086e70d4dac169f15328ac8087b6b0ef`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
