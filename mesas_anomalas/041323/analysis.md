# Mesa 041323 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.981300+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IEP SACO OLIVEROS (código 52737)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 226
- Votos válidos: 197
- Participación: 75.585%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:08:44+00:00` | `2026-04-12 22:08:44 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:08:44+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:08:44+00:00` | `2026-04-12 22:08:44 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:44:39+00:00` | `2026-04-13 09:44:39 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:47:11+00:00` | `2026-04-13 09:47:11 (Lima)` |
| Última firma humana | `2026-04-13T14:50:03+00:00` | `2026-04-13 09:50:03 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.64 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:08:44 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:47:11 (Lima), es decir **11.64 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:08:42+00:00` | `2026-04-12 22:08:42 (Lima)` | -0.00h |
| 1 | RAYMUNDEZ FABIAN sebastian Diego FIR 70592329 sw 4d70da3aa09d89c8c4f06cd78a8bf6fd91f8280e | 70592329 | `2026-04-13T14:47:11+00:00` | `2026-04-13 09:47:11 (Lima)` | +11.64h |
| 2 | RAMIREZ ANGULO frank Marcos FIR 62969412 sw 7c93f3504caecffb078ab480fe1bc787791ea7da | 62969412 | `2026-04-13T14:49:34+00:00` | `2026-04-13 09:49:34 (Lima)` | +11.68h |
| 3 | QUISPE ZEVALLOS yamilley Solange FIR 74641487 sw 51b84bfe0ccfdc060f1a06e80b4ff6d27688517d | 74641487 | `2026-04-13T14:50:03+00:00` | `2026-04-13 09:50:03 (Lima)` | +11.69h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **041323**
2. Descargar el PDF del acta
3. Verificar SHA-256: `08d838577f3ccbde436815debd439c804c958290175b4dcd8d345b6fc1dd6509`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
