# Mesa 051301 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.916832+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: UNIVERSIDAD DE LIMA 2 (código 51521)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 183
- Votos válidos: 174
- Participación: 61.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:26:05+00:00` | `2026-04-12 20:26:05 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:26:05+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:26:05+00:00` | `2026-04-12 20:26:05 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:50:27+00:00` | `2026-04-13 07:50:27 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:50:45+00:00` | `2026-04-13 07:50:45 (Lima)` |
| Última firma humana | `2026-04-13T12:51:49+00:00` | `2026-04-13 07:51:49 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.41 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:26:05 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:50:45 (Lima), es decir **11.41 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:26:02+00:00` | `2026-04-12 20:26:02 (Lima)` | -0.00h |
| 1 | GAYOSO KEMPNY rodolfo Samir FIR 10064501 sw 2283fa6370effaae7056d076c214c46aaab0208a | 10064501 | `2026-04-13T12:50:45+00:00` | `2026-04-13 07:50:45 (Lima)` | +11.41h |
| 2 | GOYCOCHEA ESTRADA mirtha Mercedes FIR 08137231 sw 44d13e1afa3ed11ba3034b3c5bd33829d1814dd2 | 08137231 | `2026-04-13T12:51:03+00:00` | `2026-04-13 07:51:03 (Lima)` | +11.42h |
| 3 | GONZALES CALLE luisa Marleny FIR 02659088 sw f647b35ba0cfa1eb483bfe6f8a56f077a1a14827 | 02659088 | `2026-04-13T12:51:24+00:00` | `2026-04-13 07:51:24 (Lima)` | +11.42h |
| 4 | MARQUEZ CONDESO fernando Luis FIR 44791420 sw 203ce01518b8bc461770a0edd2f42e9b64650d85 | 44791420 | `2026-04-13T12:51:49+00:00` | `2026-04-13 07:51:49 (Lima)` | +11.43h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051301**
2. Descargar el PDF del acta
3. Verificar SHA-256: `6c6c8d3a56024360e94d37623017c641097aa48c5d3cb164d0f524099a6e62f6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
