# Mesa 045842 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.531860+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUEBLO LIBRE
- **Local de votación**: IE 0014 ANDRES BELLO (código 3013)
- **Ubigeo**: 140117

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 215
- Votos válidos: 199
- Participación: 71.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:42:59+00:00` | `2026-04-12 20:42:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:42:59+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:42:59+00:00` | `2026-04-12 20:42:59 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:17:17+00:00` | `2026-04-13 08:17:17 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:17:34+00:00` | `2026-04-13 08:17:34 (Lima)` |
| Última firma humana | `2026-04-13T13:18:32+00:00` | `2026-04-13 08:18:32 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.58 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:42:59 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:17:34 (Lima), es decir **11.58 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:42:56+00:00` | `2026-04-12 20:42:56 (Lima)` | -0.00h |
| 1 | IPARRAGUIRRE PACHECO frieda Margot Idelsa FIR 09457149 sw 3dd053ac97d9430c8d4023f161e61b6c92311a0d | 09457149 | `2026-04-13T13:17:34+00:00` | `2026-04-13 08:17:34 (Lima)` | +11.58h |
| 2 | KRUGER BOZA carlos Alberto FIR 06389580 sw ae5e49cdc718acbb58459f6d30fef883ac72c426 | 06389580 | `2026-04-13T13:18:11+00:00` | `2026-04-13 08:18:11 (Lima)` | +11.59h |
| 3 | LACUTA FLORES beatriz Sofia FIR 61391594 sw 2c5740bda2b06dc9e482177935a70334dcccb0db | 61391594 | `2026-04-13T13:18:32+00:00` | `2026-04-13 08:18:32 (Lima)` | +11.59h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045842**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3f98f3c3b659f53e6f096fe7cc31602c1369e99ab25f7e7c7bea147d7592da19`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
