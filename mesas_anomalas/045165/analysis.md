# Mesa 045165 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.934709+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: IE FEDERICO VILLARREAL (código 2989)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 208
- Votos válidos: 197
- Participación: 69.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:55:02+00:00` | `2026-04-12 20:55:02 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:55:02+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:55:02+00:00` | `2026-04-12 20:55:02 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T06:41:00+00:00` | `2026-04-13 01:41:00 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:41:23+00:00` | `2026-04-13 01:41:23 (Lima)` |
| Última firma humana | `2026-04-13T06:42:22+00:00` | `2026-04-13 01:42:22 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.77 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:55:02 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:41:23 (Lima), es decir **4.77 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:54:57+00:00` | `2026-04-12 20:54:57 (Lima)` | -0.00h |
| 1 | VASQUEZ MAYTA carmen Lucia FIR 74225854 sw 3b2c19fa94afd17f3b1ed2a41c7eae364fd36f49 | 74225854 | `2026-04-13T06:41:23+00:00` | `2026-04-13 01:41:23 (Lima)` | +4.77h |
| 2 | VALDIVIESO VIDARTE haydee Grace FIR 06790169 sw 460af453d6f2e24b85d2824df53f9ff23b05490f | 06790169 | `2026-04-13T06:41:42+00:00` | `2026-04-13 01:41:42 (Lima)` | +4.78h |
| 3 | VASQUEZ ALVAREZ luis Anthony FIR 48710273 sw b5a9f98592a329dd381362feae7ed77f23394121 | 48710273 | `2026-04-13T06:41:58+00:00` | `2026-04-13 01:41:58 (Lima)` | +4.78h |
| 4 | PERALTA QUISPE arthur Rene FIR 43307045 sw 5fb309810ded4725fd031607b57d51cf791995e4 | 43307045 | `2026-04-13T06:42:22+00:00` | `2026-04-13 01:42:22 (Lima)` | +4.79h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045165**
2. Descargar el PDF del acta
3. Verificar SHA-256: `62dc378f1f51a50c813b4d9fec9bca53931ec3b3fbdd06c0bd202e2e2cf8d071`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
