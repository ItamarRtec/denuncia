# Mesa 052379 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.884778+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IE 6152 STELLA MARIS (código 3260)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 243
- Votos válidos: 211
- Participación: 81.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:48:50+00:00` | `2026-04-12 20:48:50 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:48:50+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:48:50+00:00` | `2026-04-12 20:48:50 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:41:32+00:00` | `2026-04-12 21:41:32 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:43:23+00:00` | `2026-04-12 21:43:23 (Lima)` |
| Última firma humana | `2026-04-13T02:45:33+00:00` | `2026-04-12 21:45:33 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.91 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:48:50 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:43:23 (Lima), es decir **0.91 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:48:48+00:00` | `2026-04-12 20:48:48 (Lima)` | -0.00h |
| 1 | VASQUEZ ROJAS catalina FIR 09938694 sw 0a2fa5cab2af7fc90f6b36a50e5548fd3e64b522 | 09938694 | `2026-04-13T02:43:23+00:00` | `2026-04-12 21:43:23 (Lima)` | +0.91h |
| 2 | VELASCO ASCONA willian Marcos FIR 10429539 sw 1daa5956db4abe6bf97721644ec82576c98fe24b | 10429539 | `2026-04-13T02:45:17+00:00` | `2026-04-12 21:45:17 (Lima)` | +0.94h |
| 3 | VASQUEZ PALOMINO jean Pieer FIR 47204701 sw 0dd35b240d301e3beb969fbef4d5a19d5531c258 | 47204701 | `2026-04-13T02:45:33+00:00` | `2026-04-12 21:45:33 (Lima)` | +0.95h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **052379**
2. Descargar el PDF del acta
3. Verificar SHA-256: `87d2dccda26eb38dd9af2f34fc63a3f93715deffd678d5d52c60696b31579d77`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
