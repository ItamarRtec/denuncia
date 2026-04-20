# Mesa 050290 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.054834+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: COLEGIO SACO OLIVEROS DE SAN MIGUEL (código 52595)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 227
- Votos válidos: 212
- Participación: 75.92%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:33:36+00:00` | `2026-04-12 20:33:36 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:33:36+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:33:36+00:00` | `2026-04-12 20:33:36 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:05:18+00:00` | `2026-04-13 00:05:18 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:06:01+00:00` | `2026-04-13 00:06:01 (Lima)` |
| Última firma humana | `2026-04-13T05:06:37+00:00` | `2026-04-13 00:06:37 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.54 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:33:36 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:06:01 (Lima), es decir **3.54 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:33:33+00:00` | `2026-04-12 20:33:33 (Lima)` | -0.00h |
| 1 | CARCAMO CONDORI raquel Erica FIR 09862185 sw d32394a9e45543384d12c7261b6eb3f849322085 | 09862185 | `2026-04-13T05:06:01+00:00` | `2026-04-13 00:06:01 (Lima)` | +3.54h |
| 2 | CANALES ESPINOLA mirella FIR 18167539 sw 4607c8ec62594cb334874a1772d9373be443069c | 18167539 | `2026-04-13T05:06:22+00:00` | `2026-04-13 00:06:22 (Lima)` | +3.55h |
| 3 | CADENA MATIAS ximena FIR 76569347 sw 3debab2e40da1ab72c98efc974e2ee8c9a025b1d | 76569347 | `2026-04-13T05:06:37+00:00` | `2026-04-13 00:06:37 (Lima)` | +3.55h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050290**
2. Descargar el PDF del acta
3. Verificar SHA-256: `63708522ba89478fc86a71db65d7acac22ab27aa82e238c4b1bda54df31c4a4a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
