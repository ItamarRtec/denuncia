# Mesa 083302 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.762780+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: VENTANILLA
- **Local de votación**: IE 5122 JOSE ANDRES RAZURI ESTEVEZ (código 4876)
- **Ubigeo**: 240106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 234
- Votos válidos: 203
- Participación: 78.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:59:00+00:00` | `2026-04-12 21:59:00 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:59:00+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:59:00+00:00` | `2026-04-12 21:59:00 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:16:43+00:00` | `2026-04-13 08:16:43 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:17:02+00:00` | `2026-04-13 08:17:02 (Lima)` |
| Última firma humana | `2026-04-13T13:17:17+00:00` | `2026-04-13 08:17:17 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.30 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:59:00 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:17:02 (Lima), es decir **10.30 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:58:58+00:00` | `2026-04-12 21:58:58 (Lima)` | -0.00h |
| 1 | PADILLA QUISPE vila Aurora FIR 77178207 sw 345067690dcf63278bdeb63bb84276e0456018b5 | 77178207 | `2026-04-13T13:17:02+00:00` | `2026-04-13 08:17:02 (Lima)` | +10.30h |
| 2 | OBREGON TINCOPA miguel Angel FIR 77505131 sw 7482dc7db5225b4cdc212938593ea4ed08b5cc0d | 77505131 | `2026-04-13T13:17:17+00:00` | `2026-04-13 08:17:17 (Lima)` | +10.30h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083302**
2. Descargar el PDF del acta
3. Verificar SHA-256: `29067c624f6e1094c08f5e90d97db57e0e2d93caf79d872b016bef4981e2705a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
