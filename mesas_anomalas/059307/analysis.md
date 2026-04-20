# Mesa 059307 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.099590+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN BORJA
- **Local de votación**: IEP AMADO DE DIOS - PRIMARIA (código 53289)
- **Ubigeo**: 140140

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 217
- Votos válidos: 206
- Participación: 72.575%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:02:55+00:00` | `2026-04-12 20:02:55 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:02:55+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:02:55+00:00` | `2026-04-12 20:02:55 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:44:22+00:00` | `2026-04-12 22:44:22 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:44:38+00:00` | `2026-04-12 22:44:38 (Lima)` |
| Última firma humana | `2026-04-13T03:45:19+00:00` | `2026-04-12 22:45:19 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.70 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:02:55 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:44:38 (Lima), es decir **2.70 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:02:53+00:00` | `2026-04-12 20:02:53 (Lima)` | -0.00h |
| 1 | CALDERON CUSIMAYTA rodrigo FIR 23943965 sw 07d9547fac59e36540b911efaad17bfcf412f533 | 23943965 | `2026-04-13T03:44:38+00:00` | `2026-04-12 22:44:38 (Lima)` | +2.70h |
| 2 | CHAVEZ NAVARRO milton Enrique FIR 07474426 sw 955da5d6c5fe6c6ee5f2fbb69a8c782be8d3ae56 | 07474426 | `2026-04-13T03:44:51+00:00` | `2026-04-12 22:44:51 (Lima)` | +2.70h |
| 3 | CHIA ARAUCO edith Karin FIR 10023443 sw a12fda034b53c41107e94bdda7e2c0ae907c3606 | 10023443 | `2026-04-13T03:45:03+00:00` | `2026-04-12 22:45:03 (Lima)` | +2.70h |
| 4 | CHAPILLIQUEN MIROQUESADA flor Maria FIR 10000499 sw 99640d743d9f654268d0cf29e0c4332894eba530 | 10000499 | `2026-04-13T03:45:19+00:00` | `2026-04-12 22:45:19 (Lima)` | +2.71h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **059307**
2. Descargar el PDF del acta
3. Verificar SHA-256: `f1487b87ce61dcc708f983c10900274bf0cf16463b1a5ee25cab37357b547f4c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
