# Mesa 054846 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.932000+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 7211 VIRGEN INMACULADA (código 3346)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 260
- Votos válidos: 219
- Participación: 86.957%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:32:56+00:00` | `2026-04-12 20:32:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:32:56+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:32:56+00:00` | `2026-04-12 20:32:56 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:31:01+00:00` | `2026-04-12 21:31:01 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:31:27+00:00` | `2026-04-12 21:31:27 (Lima)` |
| Última firma humana | `2026-04-13T02:32:04+00:00` | `2026-04-12 21:32:04 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.98 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:32:56 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:31:27 (Lima), es decir **0.98 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:32:54+00:00` | `2026-04-12 20:32:54 (Lima)` | -0.00h |
| 1 | CHAVEZ GUEVARA marco Antonio FIR 10472302 sw f4265914d6fc0c91ec97df19958da601ed24ce2b | 10472302 | `2026-04-13T02:31:27+00:00` | `2026-04-12 21:31:27 (Lima)` | +0.98h |
| 2 | CONDORI HUAYHUA magdalena Maria FIR 09587390 sw 66ff91fe4b8c494a5b49a741f9545a5c534bc5d8 | 09587390 | `2026-04-13T02:31:48+00:00` | `2026-04-12 21:31:48 (Lima)` | +0.98h |
| 3 | CASTRO QUINTANILLA vladimir Bona FIR 42772117 sw 159d835ca07a41ce7d1266793c4f31c27b680e0c | 42772117 | `2026-04-13T02:32:04+00:00` | `2026-04-12 21:32:04 (Lima)` | +0.99h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054846**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4253504b6e89327276a74327e0a5f70b24d7a67713bdbfe06dc595937398d789`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
