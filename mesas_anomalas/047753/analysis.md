# Mesa 047753 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.583988+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN ISIDRO
- **Local de votación**: IE EMBLEMATICA ALFONSO UGARTE (código 3074)
- **Ubigeo**: 140124

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 214
- Votos válidos: 204
- Participación: 71.572%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T07:12:40+00:00` | `2026-04-13 02:12:40 (Lima)` |
| `C` | Contabilizada | `2026-04-13T01:56:19+00:00` | `2026-04-12 20:56:19 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T07:12:40+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T07:12:40+00:00` | `2026-04-13 02:12:40 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:58:05+00:00` | `2026-04-13 07:58:05 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:58:24+00:00` | `2026-04-13 07:58:24 (Lima)` |
| Última firma humana | `2026-04-13T12:58:52+00:00` | `2026-04-13 07:58:52 (Lima)` |

**Brecha primera firma humana vs publicación:** **+5.76 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-13 02:12:40 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:58:24 (Lima), es decir **5.76 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:56:16+00:00` | `2026-04-12 20:56:16 (Lima)` | -5.27h |
| 1 | DEL NEGRO GARCIA michele Antonio FIR 10225089 sw a89ca19d7b427c50d0b031ed39b2f8f175ddf03a | 10225089 | `2026-04-13T12:58:24+00:00` | `2026-04-13 07:58:24 (Lima)` | +5.76h |
| 2 | DIAZ MACETAS vilma Telesfora FIR 08266345 sw e579c3c38ebcde607d732c6adaf8393642215e86 | 08266345 | `2026-04-13T12:58:40+00:00` | `2026-04-13 07:58:40 (Lima)` | +5.77h |
| 3 | DIAS LEON alberto Jose FIR 09336523 sw 6d3bcbc9aba494d2ef60f8309e1264ad09278dbf | 09336523 | `2026-04-13T12:58:52+00:00` | `2026-04-13 07:58:52 (Lima)` | +5.77h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **047753**
2. Descargar el PDF del acta
3. Verificar SHA-256: `7f1212306de69b56542e413dc2646c8b1a53e40c5c6a900e13dcc5a84609a3e6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
