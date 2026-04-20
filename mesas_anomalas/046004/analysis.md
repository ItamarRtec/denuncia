# Mesa 046004 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.254784+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUEBLO LIBRE
- **Local de votación**: IE 04 NIÑO JESUS DE PRAGA (código 50932)
- **Ubigeo**: 140117

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 230
- Votos emitidos: 171
- Votos válidos: 164
- Participación: 74.348%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:47:15+00:00` | `2026-04-12 21:47:15 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:47:15+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:47:15+00:00` | `2026-04-12 21:47:15 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:36:16+00:00` | `2026-04-13 07:36:16 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:49:29+00:00` | `2026-04-13 07:49:29 (Lima)` |
| Última firma humana | `2026-04-13T12:55:00+00:00` | `2026-04-13 07:55:00 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.04 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:47:15 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:49:29 (Lima), es decir **10.04 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:47:13+00:00` | `2026-04-12 21:47:13 (Lima)` | -0.00h |
| 1 | ALTUNA DIAZ sergio Daniel FIR 41561701 sw e0375b7b725ffb36165883ec16a0aa0ff97e6682 | 41561701 | `2026-04-13T12:49:29+00:00` | `2026-04-13 07:49:29 (Lima)` | +10.04h |
| 2 | ARAUJO ROJAS jack Manuel FIR 09465008 sw 4a990e16c894a316b93e9e3144efc853c5b23e89 | 09465008 | `2026-04-13T12:52:27+00:00` | `2026-04-13 07:52:27 (Lima)` | +10.09h |
| 3 | ALVARADO LINARES angela Maria FIR 41181600 sw 881184e9df3b1dd0c2ded8c3b31e1e3e0d06a721 | 41181600 | `2026-04-13T12:55:00+00:00` | `2026-04-13 07:55:00 (Lima)` | +10.13h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046004**
2. Descargar el PDF del acta
3. Verificar SHA-256: `28a8d5cf0f345a49b8d5a5e397035e60540bf96c868b9efc828f8963ae67e3ea`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
