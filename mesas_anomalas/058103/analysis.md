# Mesa 058103 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.622305+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IEP FEDERICO VILLARREAL (código 51129)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 262
- Votos emitidos: 202
- Votos válidos: 158
- Participación: 77.099%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T06:17:29+00:00` | `2026-04-13 01:17:29 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T06:17:29+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T06:17:29+00:00` | `2026-04-13 01:17:29 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T17:52:41+00:00` | `2026-04-13 12:52:41 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T17:54:01+00:00` | `2026-04-13 12:54:01 (Lima)` |
| Última firma humana | `2026-04-13T17:54:30+00:00` | `2026-04-13 12:54:30 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.61 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-13 01:17:29 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 12:54:01 (Lima), es decir **11.61 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T06:16:09+00:00` | `2026-04-13 01:16:09 (Lima)` | -0.02h |
| 1 | AGUERO LOPEZ luz Celestina FIR 10358652 sw 527af3b0d3e2d18fbb1e57983a24243a82af0e15 | 10358652 | `2026-04-13T17:54:01+00:00` | `2026-04-13 12:54:01 (Lima)` | +11.61h |
| 2 | ASILLO BALCAZAR henry FIR 40692227 sw 834c8c1becc8a45be2729b05abe0c863e029febb | 40692227 | `2026-04-13T17:54:30+00:00` | `2026-04-13 12:54:30 (Lima)` | +11.62h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **058103**
2. Descargar el PDF del acta
3. Verificar SHA-256: `1797237dd9b161e184852a9bdf7503dc7c65960bd8b90f40742ba07320f0079a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
