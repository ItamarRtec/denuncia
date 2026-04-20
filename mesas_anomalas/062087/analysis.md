# Mesa 062087 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.112669+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IEP SAN LUIS GONZAGA (código 32227)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 261
- Votos válidos: 235
- Participación: 87.291%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:51:19+00:00` | `2026-04-12 21:51:19 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:51:19+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:51:19+00:00` | `2026-04-12 21:51:19 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:16:18+00:00` | `2026-04-13 09:16:18 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:20:33+00:00` | `2026-04-13 09:20:33 (Lima)` |
| Última firma humana | `2026-04-13T14:24:06+00:00` | `2026-04-13 09:24:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.49 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:51:19 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:20:33 (Lima), es decir **11.49 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:46:51+00:00` | `2026-04-12 21:46:51 (Lima)` | -0.07h |
| 1 | HUAYTA QUISPE humberto FIR 10696237 sw d2dc8eefa89838d659e9c2482cc55a6b8539ec72 | 10696237 | `2026-04-13T14:20:33+00:00` | `2026-04-13 09:20:33 (Lima)` | +11.49h |
| 2 | JESUS ZAMUDIO rosa Luz FIR 09780727 sw f66db9e803494dbeab982996557189704cb4043f | 09780727 | `2026-04-13T14:21:55+00:00` | `2026-04-13 09:21:55 (Lima)` | +11.51h |
| 3 | HURTADO TITO felicitas FIR 07536843 sw 87829836ab5c1b4617550fbddacb9d4b6ffd6ef0 | 07536843 | `2026-04-13T14:23:14+00:00` | `2026-04-13 09:23:14 (Lima)` | +11.53h |
| 4 | CCAMACCA LLIUYACC israel FIR 78731487 sw b7dc75d3d841741511409902326f51300c1f1d93 | 78731487 | `2026-04-13T14:23:47+00:00` | `2026-04-13 09:23:47 (Lima)` | +11.54h |
| 5 | PRADO ANCHAYHUA felix FIR 07080207 sw b92412ed64812182d106ce0d822f535b19607ba4 | 07080207 | `2026-04-13T14:24:06+00:00` | `2026-04-13 09:24:06 (Lima)` | +11.55h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **062087**
2. Descargar el PDF del acta
3. Verificar SHA-256: `14cae3c916a5d903ca42e21d0882728cfeba8518e94981fc08739ac6e3a1d9ff`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
