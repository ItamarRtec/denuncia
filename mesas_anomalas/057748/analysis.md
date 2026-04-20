# Mesa 057748 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.115040+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IEP BENJAMIN FRANKLIN (código 18499)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 240
- Votos válidos: 205
- Participación: 80.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:44:28+00:00` | `2026-04-12 20:44:28 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:44:28+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:44:28+00:00` | `2026-04-12 20:44:28 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:23:13+00:00` | `2026-04-12 23:23:13 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:23:47+00:00` | `2026-04-12 23:23:47 (Lima)` |
| Última firma humana | `2026-04-13T04:24:10+00:00` | `2026-04-12 23:24:10 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.66 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:44:28 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:23:47 (Lima), es decir **2.66 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:44:26+00:00` | `2026-04-12 20:44:26 (Lima)` | -0.00h |
| 1 | SERRANO SALVADOR kely Bheatriz FIR 71608080 sw ee0a597b4c377c321935e371068bc60903bdef29 | 71608080 | `2026-04-13T04:23:47+00:00` | `2026-04-12 23:23:47 (Lima)` | +2.66h |
| 2 | SURCO CHURA leydi Laura FIR 80654838 sw e7073bee6942c79bebbb556e8d375ad9906e6314 | 80654838 | `2026-04-13T04:23:59+00:00` | `2026-04-12 23:23:59 (Lima)` | +2.66h |
| 3 | TERRY RECCIO lourdes Elizabeth FIR 47889788 sw eb3bfa84ee35ffce38a5cd01ab48f5255c1c6043 | 47889788 | `2026-04-13T04:24:10+00:00` | `2026-04-12 23:24:10 (Lima)` | +2.66h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **057748**
2. Descargar el PDF del acta
3. Verificar SHA-256: `51a006e450d775ed79efd8509912ff7fc2d12aab5573308eae9b19f7fbddfb82`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
