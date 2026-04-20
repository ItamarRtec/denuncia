# Mesa 042306 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.239958+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CHORRILLOS
- **Local de votación**: COLEGIO PAMER CHORRILLOS (código 50473)
- **Ubigeo**: 140108

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 249
- Votos válidos: 223
- Participación: 83.278%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:09:33+00:00` | `2026-04-12 20:09:33 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:09:33+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:09:33+00:00` | `2026-04-12 20:09:33 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:05:46+00:00` | `2026-04-12 22:05:46 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:06:03+00:00` | `2026-04-12 22:06:03 (Lima)` |
| Última firma humana | `2026-04-13T03:06:16+00:00` | `2026-04-12 22:06:16 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.94 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:09:33 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:06:03 (Lima), es decir **1.94 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:09:31+00:00` | `2026-04-12 20:09:31 (Lima)` | -0.00h |
| 1 | PINEDO BERNDT silvina Miluska FIR 45407783 sw ffcade920977310f8cd6d5c8b136935bcb21b998 | 45407783 | `2026-04-13T03:06:03+00:00` | `2026-04-12 22:06:03 (Lima)` | +1.94h |
| 2 | PAUCAR ACHO jose Antonio FIR 09492558 sw bd8f93398a73daad27bdecefdcedb7af52de0901 | 09492558 | `2026-04-13T03:06:16+00:00` | `2026-04-12 22:06:16 (Lima)` | +1.95h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **042306**
2. Descargar el PDF del acta
3. Verificar SHA-256: `6253ca0e95a5d8083818ff906b16d069715c82830dabdeacef1f6e5528aa4910`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
