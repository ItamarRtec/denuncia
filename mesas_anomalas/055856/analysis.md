# Mesa 055856 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.860861+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IEP SACO OLIVEROS SEDE JULIO BELLIDO (código 52453)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 221
- Votos válidos: 198
- Participación: 73.913%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:41:38+00:00` | `2026-04-12 21:41:38 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:41:38+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:41:38+00:00` | `2026-04-12 21:41:38 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:18:35+00:00` | `2026-04-13 09:18:35 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:19:03+00:00` | `2026-04-13 09:19:03 (Lima)` |
| Última firma humana | `2026-04-13T14:19:27+00:00` | `2026-04-13 09:19:27 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.62 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:41:38 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:19:03 (Lima), es decir **11.62 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:41:36+00:00` | `2026-04-12 21:41:36 (Lima)` | -0.00h |
| 1 | ORE LIPE maria Lucia FIR 61173380 sw 3fbffaa66f3a3346ac6dbf831374ba858daf0015 | 61173380 | `2026-04-13T14:19:03+00:00` | `2026-04-13 09:19:03 (Lima)` | +11.62h |
| 2 | ORTEGA HURTADO michael Teodosio FIR 71910950 sw 330c7f6930c1b20020645c10830a6ff917b38a87 | 71910950 | `2026-04-13T14:19:15+00:00` | `2026-04-13 09:19:15 (Lima)` | +11.63h |
| 3 | MIRANDA SILVESTRE estefani Carolina FIR 72299506 sw f768da1281997051e3a6d768e3487a7bf303deb1 | 72299506 | `2026-04-13T14:19:27+00:00` | `2026-04-13 09:19:27 (Lima)` | +11.63h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055856**
2. Descargar el PDF del acta
3. Verificar SHA-256: `d8d864f133ccec0ae1f88ca67349f967febcdc8c406d1943eb2956bfd5c40f70`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
