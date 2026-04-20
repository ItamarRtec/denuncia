# Mesa 051802 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.948509+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: IE LA DIVINA PROVIDENCIA (código 3235)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 226
- Votos válidos: 215
- Participación: 75.585%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:52:07+00:00` | `2026-04-12 20:52:07 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:52:07+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:52:07+00:00` | `2026-04-12 20:52:07 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T08:19:50+00:00` | `2026-04-13 03:19:50 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T08:20:07+00:00` | `2026-04-13 03:20:07 (Lima)` |
| Última firma humana | `2026-04-13T08:20:38+00:00` | `2026-04-13 03:20:38 (Lima)` |

**Brecha primera firma humana vs publicación:** **+6.47 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:52:07 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 03:20:07 (Lima), es decir **6.47 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:52:05+00:00` | `2026-04-12 20:52:05 (Lima)` | -0.00h |
| 1 | CRIADO RODRIGUEZ jerusalem Marian FIR 60851422 sw 54150d10d504b167f0cdd445fcebc53122dd4256 | 60851422 | `2026-04-13T08:20:07+00:00` | `2026-04-13 03:20:07 (Lima)` | +6.47h |
| 2 | CUADROS MAYTA jeriel Jeremias FIR 60892683 sw c5ee4fbebc7f52192d7f2b40463f2dc75fb282a5 | 60892683 | `2026-04-13T08:20:21+00:00` | `2026-04-13 03:20:21 (Lima)` | +6.47h |
| 3 | DAMACEN BILLADONI jane Fabiola FIR 49049621 sw c53e1f1842c5b69c260edb98c1c6013795c216d9 | 49049621 | `2026-04-13T08:20:38+00:00` | `2026-04-13 03:20:38 (Lima)` | +6.48h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051802**
2. Descargar el PDF del acta
3. Verificar SHA-256: `385547bdd4432239e644ce2dea2441ac3c6f17ad2af1862ff032003cb89c41e7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
