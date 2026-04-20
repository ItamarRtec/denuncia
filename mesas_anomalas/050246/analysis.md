# Mesa 050246 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.917247+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: IEP INMACULADO CORAZON DE MARIA (código 50538)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 237
- Votos válidos: 221
- Participación: 79.264%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:39:01+00:00` | `2026-04-12 22:39:01 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:39:01+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:39:01+00:00` | `2026-04-12 22:39:01 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:16:47+00:00` | `2026-04-13 09:16:47 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:17:33+00:00` | `2026-04-13 09:17:33 (Lima)` |
| Última firma humana | `2026-04-13T14:18:06+00:00` | `2026-04-13 09:18:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.64 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:39:01 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:17:33 (Lima), es decir **10.64 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:38:59+00:00` | `2026-04-12 22:38:59 (Lima)` | -0.00h |
| 1 | PEREZ CHANDUVI paula Patricia FIR 40887140 sw d551ec88d5cca7a58f10feac77e99e13b56f5501 | 40887140 | `2026-04-13T14:17:33+00:00` | `2026-04-13 09:17:33 (Lima)` | +10.64h |
| 2 | PAZ JARA martha Violeta FIR 09276568 sw 493353f5ed5641607ae6d0e7a3db1ad6dc31cebf | 09276568 | `2026-04-13T14:17:43+00:00` | `2026-04-13 09:17:43 (Lima)` | +10.64h |
| 3 | CESPEDES TELLO sorina Del Carmen FIR 08564227 sw 0e77f96da5e0db99ecbbbc993b4d4ce1154beb39 | 08564227 | `2026-04-13T14:18:06+00:00` | `2026-04-13 09:18:06 (Lima)` | +10.65h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050246**
2. Descargar el PDF del acta
3. Verificar SHA-256: `db7043a9b1e29a16d6a6c31282618d72b6d5d6a7649e9f7f4af62e715e8a652d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
