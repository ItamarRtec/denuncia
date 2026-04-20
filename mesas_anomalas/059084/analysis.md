# Mesa 059084 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.321229+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN BORJA
- **Local de votación**: IE 7083 MANUEL GONZALES PRADA - SECUNDARIA (código 3495)
- **Ubigeo**: 140140

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 231
- Votos válidos: 216
- Participación: 77.258%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:59:48+00:00` | `2026-04-12 19:59:48 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:59:48+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:59:48+00:00` | `2026-04-12 19:59:48 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:10:37+00:00` | `2026-04-12 22:10:37 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:18:08+00:00` | `2026-04-12 22:18:08 (Lima)` |
| Última firma humana | `2026-04-13T03:18:41+00:00` | `2026-04-12 22:18:41 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.31 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:59:48 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:18:08 (Lima), es decir **2.31 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:59:46+00:00` | `2026-04-12 19:59:46 (Lima)` | -0.00h |
| 1 | RUIZ RAMIREZ evelin Yessennia FIR 23020943 sw bc6fc495696a15b07d971029a2c58ccc63d5431e | 23020943 | `2026-04-13T03:18:08+00:00` | `2026-04-12 22:18:08 (Lima)` | +2.31h |
| 2 | RODRIGUEZ VIZARES rossana Olga FIR 10004151 sw 655cd361008604b6a456bef944c4a8c7e5a94f50 | 10004151 | `2026-04-13T03:18:21+00:00` | `2026-04-12 22:18:21 (Lima)` | +2.31h |
| 3 | SAAVEDRA ROJAS franck Juvenal FIR 42855444 sw ecb6ebfb1905b2025b4c71dd7ff93690419c766d | 42855444 | `2026-04-13T03:18:41+00:00` | `2026-04-12 22:18:41 (Lima)` | +2.31h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **059084**
2. Descargar el PDF del acta
3. Verificar SHA-256: `d72459de0328bd2c33cddea77cb54e7ba8969d20cc59dc3c83a2e2da65dc772e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
