# Mesa 055309 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.996326+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE FE Y ALEGRIA 3 (código 3376)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 222
- Votos válidos: 193
- Participación: 74.247%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:29:27+00:00` | `2026-04-12 22:29:27 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:29:27+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:29:27+00:00` | `2026-04-12 22:29:27 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:48:40+00:00` | `2026-04-13 00:48:40 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:48:58+00:00` | `2026-04-13 00:48:58 (Lima)` |
| Última firma humana | `2026-04-13T05:49:14+00:00` | `2026-04-13 00:49:14 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.33 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:29:27 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:48:58 (Lima), es decir **2.33 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:29:26+00:00` | `2026-04-12 22:29:26 (Lima)` | -0.00h |
| 1 | ANDRES JUSTO gaspar Rene FIR 08398842 sw 82cf1fdb2bb3f3fcb30c3bc807790a63d65a7fc2 | 08398842 | `2026-04-13T05:48:58+00:00` | `2026-04-13 00:48:58 (Lima)` | +2.33h |
| 2 | ARENAS CCORI carlos Alberto FIR 46600259 sw a82a2fa5db7490e71bfa49058ae36d37f1328086 | 46600259 | `2026-04-13T05:49:14+00:00` | `2026-04-13 00:49:14 (Lima)` | +2.33h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055309**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8c7336fd08cf8355aeb745195c318566106d7349972b12d4012a9d56a468bb10`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
