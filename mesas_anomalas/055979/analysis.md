# Mesa 055979 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.161772+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IE 0045 SAN ANTONIO (código 3388)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 256
- Votos válidos: 214
- Participación: 85.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:01:09+00:00` | `2026-04-12 21:01:09 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:01:09+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:01:09+00:00` | `2026-04-12 21:01:09 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:43:00+00:00` | `2026-04-13 08:43:00 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:43:19+00:00` | `2026-04-13 08:43:19 (Lima)` |
| Última firma humana | `2026-04-13T13:43:47+00:00` | `2026-04-13 08:43:47 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.70 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:01:09 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:43:19 (Lima), es decir **11.70 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:00:58+00:00` | `2026-04-12 21:00:58 (Lima)` | -0.00h |
| 1 | POMA ZAIRE gloria Estefani FIR 77667177 sw 266ff1e406b3a9384f94a9384a5865aaf3fb8ec5 | 77667177 | `2026-04-13T13:43:19+00:00` | `2026-04-13 08:43:19 (Lima)` | +11.70h |
| 2 | REYES BLAS rocio Del Carmen FIR 46554062 sw 7d0cbeb316d0b6ed5866b83cd67519aa69afd185 | 46554062 | `2026-04-13T13:43:34+00:00` | `2026-04-13 08:43:34 (Lima)` | +11.71h |
| 3 | POZO LOPEZ laura Rosalia FIR 44562888 sw ccf3b8a081e73c2540f904bc962edcd98321e05b | 44562888 | `2026-04-13T13:43:47+00:00` | `2026-04-13 08:43:47 (Lima)` | +11.71h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055979**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4c8d1ee9bef3b59a8305e436fa38146d4dbe070620b74fc05b5c29e823be5a5a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
