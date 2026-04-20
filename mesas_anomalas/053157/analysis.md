# Mesa 053157 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.206934+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IE PARROQUIAL NUESTRO SALVADOR (código 18293)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 296
- Votos emitidos: 228
- Votos válidos: 196
- Participación: 77.027%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:55:01+00:00` | `2026-04-12 20:55:01 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:55:01+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:55:01+00:00` | `2026-04-12 20:55:01 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:44:42+00:00` | `2026-04-13 00:44:42 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:44:57+00:00` | `2026-04-13 00:44:57 (Lima)` |
| Última firma humana | `2026-04-13T05:45:32+00:00` | `2026-04-13 00:45:32 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.83 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:55:01 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:44:57 (Lima), es decir **3.83 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:54:59+00:00` | `2026-04-12 20:54:59 (Lima)` | -0.00h |
| 1 | NEIRA GARCIA franklin Zidani FIR 76114916 sw d0092473fd12a002bf5f5f5abfcc6acd2e4acea2 | 76114916 | `2026-04-13T05:44:57+00:00` | `2026-04-13 00:44:57 (Lima)` | +3.83h |
| 2 | OCAMPO PAREDES kathery FIR 72381802 sw 6f5b831de76e7b7e6b0116ca6b5b1693bcdebd38 | 72381802 | `2026-04-13T05:45:14+00:00` | `2026-04-13 00:45:14 (Lima)` | +3.84h |
| 3 | NAVAS YACHI natiniel Naomi FIR 72566582 sw 489264068c21586ddb7afd8b1283fcad2f19b51b | 72566582 | `2026-04-13T05:45:32+00:00` | `2026-04-13 00:45:32 (Lima)` | +3.84h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **053157**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4ae552500ffe6298d0c8765a0bd3de978346cb440bd2fffc0c4950a74453d706`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
