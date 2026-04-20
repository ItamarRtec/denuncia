# Mesa 062088 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.071767+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: IEP SAN LUIS GONZAGA (código 32227)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 264
- Votos válidos: 223
- Participación: 88.294%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:44:36+00:00` | `2026-04-12 21:44:36 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:44:36+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:44:36+00:00` | `2026-04-12 21:44:36 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:19:00+00:00` | `2026-04-13 09:19:00 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:19:41+00:00` | `2026-04-13 09:19:41 (Lima)` |
| Última firma humana | `2026-04-13T14:21:28+00:00` | `2026-04-13 09:21:28 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.58 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:44:36 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:19:41 (Lima), es decir **11.58 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:44:33+00:00` | `2026-04-12 21:44:33 (Lima)` | -0.00h |
| 1 | QUISPE SIHUINCHA DE CUYA milchora FIR 09232645 sw d27826190bace6bbfd4bd4884fdf20be344b3a2a | 09232645 | `2026-04-13T14:19:41+00:00` | `2026-04-13 09:19:41 (Lima)` | +11.58h |
| 2 | PATRICIO NIEVES soledad Eugenia FIR 10057886 sw 53d25afa7d6d049dc54ee9ccb71c65b6a38a914d | 10057886 | `2026-04-13T14:20:22+00:00` | `2026-04-13 09:20:22 (Lima)` | +11.60h |
| 3 | CAYETANO HUAMANI cesar Toribio FIR 10039790 sw 32d0cba9de79e456f4f8dffc947435b2ec4fcc4e | 10039790 | `2026-04-13T14:21:28+00:00` | `2026-04-13 09:21:28 (Lima)` | +11.61h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **062088**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8476e6a4faa67f406f1c5fbb729080bbbc8b961ca67bf6c85e110618452dba56`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
