# Mesa 040583 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.669758+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IESTP CARLOS CUETO FERNANDINI (código 2846)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 239
- Votos válidos: 217
- Participación: 79.933%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T04:50:55+00:00` | `2026-04-12 23:50:55 (Lima)` |
| `C` | Contabilizada | `2026-04-13T01:36:26+00:00` | `2026-04-12 20:36:26 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T04:50:55+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T04:50:55+00:00` | `2026-04-12 23:50:55 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:03:28+00:00` | `2026-04-13 08:03:28 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:05:54+00:00` | `2026-04-13 08:05:54 (Lima)` |
| Última firma humana | `2026-04-13T13:07:23+00:00` | `2026-04-13 08:07:23 (Lima)` |

**Brecha primera firma humana vs publicación:** **+8.25 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 23:50:55 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:05:54 (Lima), es decir **8.25 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:36:24+00:00` | `2026-04-12 20:36:24 (Lima)` | -3.24h |
| 1 | BRAVO MORENO renzo Joseph FIR 74854645 sw 6e78357e8e9070badab88a9d78035c3c3615e75d | 74854645 | `2026-04-13T13:05:54+00:00` | `2026-04-13 08:05:54 (Lima)` | +8.25h |
| 2 | AYRA GONZALES DE INGOL armida Yulissa FIR 44522344 sw 4aa4ad7a8352d484f668dc5c611798798f8d9df7 | 44522344 | `2026-04-13T13:06:11+00:00` | `2026-04-13 08:06:11 (Lima)` | +8.25h |
| 3 | AVILA CLEMENTE kevin Aaron FIR 74712393 sw b027cb975e9ec4effefbdc54d0cdb54c8edcac91 | 74712393 | `2026-04-13T13:07:23+00:00` | `2026-04-13 08:07:23 (Lima)` | +8.27h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **040583**
2. Descargar el PDF del acta
3. Verificar SHA-256: `888e5d8293b71d8e189e8380e7943a5f1e08dd3f557388ca295c78d8999c085e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
