# Mesa 051920 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.497600+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: ESTADIO MUNICIPAL CARLOS A. MOSCOSO 2 (código 40995)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 221
- Votos válidos: 203
- Participación: 73.913%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T04:08:53+00:00` | `2026-04-12 23:08:53 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T04:08:53+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T04:08:53+00:00` | `2026-04-12 23:08:53 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:42:52+00:00` | `2026-04-13 08:42:52 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:43:22+00:00` | `2026-04-13 08:43:22 (Lima)` |
| Última firma humana | `2026-04-13T13:44:05+00:00` | `2026-04-13 08:44:05 (Lima)` |

**Brecha primera firma humana vs publicación:** **+9.57 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 23:08:53 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:43:22 (Lima), es decir **9.57 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T04:08:50+00:00` | `2026-04-12 23:08:50 (Lima)` | -0.00h |
| 1 | RETO MAURICIO carolina Magdalena FIR 77144877 sw 9e0e538c31ac1036bcc770c8283df96ace88e6f6 | 77144877 | `2026-04-13T13:43:22+00:00` | `2026-04-13 08:43:22 (Lima)` | +9.57h |
| 2 | RAMOS MORALES wilmer Demetrio FIR 32392642 sw ce38061e4eb306164860e2047b0f743cf57dd9b0 | 32392642 | `2026-04-13T13:43:53+00:00` | `2026-04-13 08:43:53 (Lima)` | +9.58h |
| 3 | RENDON CACERES manuel Enrique FIR 10342911 sw 002560d79d773e8205397e134ed7e82440b756af | 10342911 | `2026-04-13T13:44:05+00:00` | `2026-04-13 08:44:05 (Lima)` | +9.59h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051920**
2. Descargar el PDF del acta
3. Verificar SHA-256: `383bd15ddce3fabce85b3ff45827ea5d4f54210867046f1456718633677902c5`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
