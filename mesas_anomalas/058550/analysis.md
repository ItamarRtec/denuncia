# Mesa 058550 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.993251+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IEP SACO OLIVEROS SEDE EL ROSARIO (código 54494)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 225
- Votos válidos: 192
- Participación: 75.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:30:50+00:00` | `2026-04-12 20:30:50 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:30:50+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:30:50+00:00` | `2026-04-12 20:30:50 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:22:45+00:00` | `2026-04-12 21:22:45 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:24:19+00:00` | `2026-04-12 21:24:19 (Lima)` |
| Última firma humana | `2026-04-13T02:24:39+00:00` | `2026-04-12 21:24:39 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.89 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:30:50 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:24:19 (Lima), es decir **0.89 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:30:48+00:00` | `2026-04-12 20:30:48 (Lima)` | -0.00h |
| 1 | VEGA PEZUA tommy Daniel FIR 70708308 sw 617e35a019a771ac789fe245ed7363ca2197f22e | 70708308 | `2026-04-13T02:24:19+00:00` | `2026-04-12 21:24:19 (Lima)` | +0.89h |
| 2 | VARGAS RIVERA grecia Mishell FIR 60737986 sw b0fdde3661dbd73a161f77682bbdca1a0cd9696c | 60737986 | `2026-04-13T02:24:39+00:00` | `2026-04-12 21:24:39 (Lima)` | +0.90h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **058550**
2. Descargar el PDF del acta
3. Verificar SHA-256: `6ffb63e067f69acf590391b2612c33b288618a5422bba400d9796ff294fd92a3`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
