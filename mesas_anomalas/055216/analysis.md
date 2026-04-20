# Mesa 055216 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.866162+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 7087 EL NAZARENO (código 3369)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 249
- Votos válidos: 208
- Participación: 83.278%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:36:10+00:00` | `2026-04-12 20:36:10 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:36:10+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:36:10+00:00` | `2026-04-12 20:36:10 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:06:01+00:00` | `2026-04-13 00:06:01 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:06:39+00:00` | `2026-04-13 00:06:39 (Lima)` |
| Última firma humana | `2026-04-13T05:07:01+00:00` | `2026-04-13 00:07:01 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.51 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:36:10 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:06:39 (Lima), es decir **3.51 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:36:08+00:00` | `2026-04-12 20:36:08 (Lima)` | -0.00h |
| 1 | TACAS TAZA shande Jhair Antonio FIR 75261759 sw 779fbc01749b4660a992fe6b2a19faacedf63b3f | 75261759 | `2026-04-13T05:06:39+00:00` | `2026-04-13 00:06:39 (Lima)` | +3.51h |
| 2 | TINEO DURAND jacqueline Lisset FIR 44220941 sw f8836d1c969e4601e7556abb314c88559ff533ff | 44220941 | `2026-04-13T05:06:50+00:00` | `2026-04-13 00:06:50 (Lima)` | +3.51h |
| 3 | VARGAS SUAREZ DE AYALA carmen Patricia FIR 10481859 sw 18edaba68a9cebb090d7af3a1cef726017c40cd8 | 10481859 | `2026-04-13T05:07:01+00:00` | `2026-04-13 00:07:01 (Lima)` | +3.51h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055216**
2. Descargar el PDF del acta
3. Verificar SHA-256: `72fc1f9eea721a71040b27d204b029f658a291cd3c2924e8348745faf3809fd6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
