# Mesa 046448 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.487016+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUENTE PIEDRA
- **Local de votación**: IE AUGUSTO B. LEGUIA (código 3042)
- **Ubigeo**: 140119

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 293
- Votos emitidos: 243
- Votos válidos: 199
- Participación: 82.935%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:13:28+00:00` | `2026-04-12 21:13:28 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:13:28+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:13:28+00:00` | `2026-04-12 21:13:28 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:01:02+00:00` | `2026-04-13 08:01:02 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:16:35+00:00` | `2026-04-13 08:16:35 (Lima)` |
| Última firma humana | `2026-04-13T13:23:43+00:00` | `2026-04-13 08:23:43 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.05 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:13:28 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:16:35 (Lima), es decir **11.05 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:13:26+00:00` | `2026-04-12 21:13:26 (Lima)` | -0.00h |
| 1 | IDRUGO OSORIO carla Khatrina FIR 72029012 sw 35c5bae4f8f86116406d2b5447aa51d1f4efba17 | 72029012 | `2026-04-13T13:16:35+00:00` | `2026-04-13 08:16:35 (Lima)` | +11.05h |
| 2 | HUAMANCAJA MAURI claudia FIR 46939942 sw ad88a41ee32d07b4c89af98bc65b680bf5c0319c | 46939942 | `2026-04-13T13:18:41+00:00` | `2026-04-13 08:18:41 (Lima)` | +11.09h |
| 3 | HUAMANI VILLALOBOS john Anthony FIR 76574707 sw afceaeb0b9f46cc04782333a9c70fda7a75d5b8e | 76574707 | `2026-04-13T13:23:43+00:00` | `2026-04-13 08:23:43 (Lima)` | +11.17h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046448**
2. Descargar el PDF del acta
3. Verificar SHA-256: `d5f4b1cb635cbd5921e8a78d86f9dc156388cc5569a45c4263703927e3a67433`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
