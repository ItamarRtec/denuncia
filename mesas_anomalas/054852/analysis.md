# Mesa 054852 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.641187+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 7211 VIRGEN INMACULADA (código 3346)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 263
- Votos válidos: 229
- Participación: 87.96%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:44:15+00:00` | `2026-04-12 20:44:15 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:44:15+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:44:15+00:00` | `2026-04-12 20:44:15 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T06:05:32+00:00` | `2026-04-13 01:05:32 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:05:47+00:00` | `2026-04-13 01:05:47 (Lima)` |
| Última firma humana | `2026-04-13T06:07:06+00:00` | `2026-04-13 01:07:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.36 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:44:15 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:05:47 (Lima), es decir **4.36 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:44:12+00:00` | `2026-04-12 20:44:12 (Lima)` | -0.00h |
| 1 | YPANAQUE SANDOVAL karen Elizabeth FIR 72454320 sw 83d43a459784f07ab6ab633386a77c9590dabdd6 | 72454320 | `2026-04-13T06:05:47+00:00` | `2026-04-13 01:05:47 (Lima)` | +4.36h |
| 2 | VASQUEZ CHUQUIMANTARI jackeline Tabata FIR 40004512 sw b1f0d47d32aa7e9886b341df5499b9391997c2f7 | 40004512 | `2026-04-13T06:06:03+00:00` | `2026-04-13 01:06:03 (Lima)` | +4.36h |
| 3 | SOSA CUELLAR lucero Janeth FIR 72692456 sw 22695407aac12adea4266aa606c68b3322e6d855 | 72692456 | `2026-04-13T06:06:21+00:00` | `2026-04-13 01:06:21 (Lima)` | +4.37h |
| 4 | EUSEBIO DANIEL margarita FIR 43387477 sw 3a879e994b27fab04b9180428b9c35fc7a1a5bd8 | 43387477 | `2026-04-13T06:06:42+00:00` | `2026-04-13 01:06:42 (Lima)` | +4.37h |
| 5 | HUARACA ESPINOZA justo Agapo FIR 08832431 sw 42f5665106fd6be3939cb30e403ef712ac144ba0 | 08832431 | `2026-04-13T06:07:06+00:00` | `2026-04-13 01:07:06 (Lima)` | +4.38h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054852**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5c95c7143429ee181fbbed9568f3da53d20f17581165d8639102301503e043e7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
