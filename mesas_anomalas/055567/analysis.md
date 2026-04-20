# Mesa 055567 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.417959+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 6045 DOLORES CAVERO DE GRAU (código 7437)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 223
- Votos válidos: 204
- Participación: 74.582%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:11:05+00:00` | `2026-04-12 22:11:05 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:11:05+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:11:05+00:00` | `2026-04-12 22:11:05 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:40:26+00:00` | `2026-04-13 00:40:26 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:40:46+00:00` | `2026-04-13 00:40:46 (Lima)` |
| Última firma humana | `2026-04-13T05:41:23+00:00` | `2026-04-13 00:41:23 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.49 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:11:05 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:40:46 (Lima), es decir **2.49 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:11:04+00:00` | `2026-04-12 22:11:04 (Lima)` | -0.00h |
| 1 | ESTRADA CLEMENTE melissa Zulema FIR 42953268 sw 2464e4140fa7b93bf364052f5f3a4cd89e9360b0 | 42953268 | `2026-04-13T05:40:46+00:00` | `2026-04-13 00:40:46 (Lima)` | +2.49h |
| 2 | DIAZ OROS marco FIR 42449591 sw 2ae19fd07950f25f1d468ea9ac448cb2c15d3504 | 42449591 | `2026-04-13T05:41:07+00:00` | `2026-04-13 00:41:07 (Lima)` | +2.50h |
| 3 | FERNANDEZ PAMPA jose Antonio FIR 42825429 sw 6c29d9672d63a9c837f74d316ba76a7698f3c480 | 42825429 | `2026-04-13T05:41:23+00:00` | `2026-04-13 00:41:23 (Lima)` | +2.50h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055567**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3465df27787c8e504d2ecdc70bf2e1c20c04f6f94f8cfeabb2b2c608854c9ae2`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
