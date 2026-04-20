# Mesa 059099 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:05.782886+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN BORJA
- **Local de votación**: IE 7089 ROMEO LUNA VICTORIA (código 3496)
- **Ubigeo**: 140140

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 229
- Votos válidos: 215
- Participación: 76.589%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:44:10+00:00` | `2026-04-12 21:44:10 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:44:10+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:44:10+00:00` | `2026-04-12 21:44:10 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:07:39+00:00` | `2026-04-13 08:07:39 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:09:23+00:00` | `2026-04-13 08:09:23 (Lima)` |
| Última firma humana | `2026-04-13T13:10:07+00:00` | `2026-04-13 08:10:07 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.42 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:44:10 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:09:23 (Lima), es decir **10.42 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:38:36+00:00` | `2026-04-12 21:38:36 (Lima)` | -0.09h |
| 1 | ITAKURA TAMAKI hitomi FIR 10609444 sw 6f2f68ead954b441558632ee52c336f6976a96a6 | 10609444 | `2026-04-13T13:09:23+00:00` | `2026-04-13 08:09:23 (Lima)` | +10.42h |
| 2 | KANASHIRO YAMANIHA alejandro FIR 40738512 sw 972d18a92bc263998fe3c0c1b9bf6a721e78b82c | 40738512 | `2026-04-13T13:09:51+00:00` | `2026-04-13 08:09:51 (Lima)` | +10.43h |
| 3 | KAMISATO GUSHI iris Cristina FIR 09533340 sw ced5c6f7daf2e4f31bd9a7a3f7df248336e11650 | 09533340 | `2026-04-13T13:10:07+00:00` | `2026-04-13 08:10:07 (Lima)` | +10.43h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **059099**
2. Descargar el PDF del acta
3. Verificar SHA-256: `7d1dc7923ca0bf4c63501b25944ee2878751b92a45adc0b350d476a03fc6d940`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
