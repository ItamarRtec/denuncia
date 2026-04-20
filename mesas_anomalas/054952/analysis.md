# Mesa 054952 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.199490+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 6089 JORGE BASADRE GROHMANN (código 3354)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 215
- Votos válidos: 177
- Participación: 71.906%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:05:09+00:00` | `2026-04-12 21:05:09 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:01:37+00:00` | `2026-04-12 21:01:37 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:05:09+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:05:09+00:00` | `2026-04-12 21:05:09 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T06:35:58+00:00` | `2026-04-13 01:35:58 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:36:11+00:00` | `2026-04-13 01:36:11 (Lima)` |
| Última firma humana | `2026-04-13T06:36:46+00:00` | `2026-04-13 01:36:46 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.52 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:05:09 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:36:11 (Lima), es decir **4.52 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:01:35+00:00` | `2026-04-12 21:01:35 (Lima)` | -0.06h |
| 1 | CONTRERAS DIAZ heidi Carola FIR 48942684 sw b8ba8aa843422b9be8373657ebc6c5286e455238 | 48942684 | `2026-04-13T06:36:11+00:00` | `2026-04-13 01:36:11 (Lima)` | +4.52h |
| 2 | COSEATADO MIRANDA yuli Felicitas FIR 40252024 sw b6046629a53a968079c98c3b416fb300a4e03e58 | 40252024 | `2026-04-13T06:36:23+00:00` | `2026-04-13 01:36:23 (Lima)` | +4.52h |
| 3 | COLOS GOMEZ jazmin Nicole FIR 71701896 sw 70fae283a703dde816a9cd4c112e822232e9eee1 | 71701896 | `2026-04-13T06:36:32+00:00` | `2026-04-13 01:36:32 (Lima)` | +4.52h |
| 4 | RODRIGUEZ ROMERO jimena Patricia FIR 74876169 sw ef7f8bd6428eafc4ab1e34e9d0ec19904fdb48d6 | 74876169 | `2026-04-13T06:36:46+00:00` | `2026-04-13 01:36:46 (Lima)` | +4.53h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054952**
2. Descargar el PDF del acta
3. Verificar SHA-256: `dddeb6d9a93bb7609ec3d52591a5d60c3e0bdc9bc46b091707bbfdb2ae44d221`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
