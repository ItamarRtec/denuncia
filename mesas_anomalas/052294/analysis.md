# Mesa 052294 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.687261+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IE 6073 JORGE BASADRE GROHMANN - SECUNDARIA (código 3256)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 242
- Votos válidos: 216
- Participación: 80.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:42:38+00:00` | `2026-04-12 20:42:38 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:42:38+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:42:38+00:00` | `2026-04-12 20:42:38 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:45:39+00:00` | `2026-04-13 00:45:39 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:46:21+00:00` | `2026-04-13 00:46:21 (Lima)` |
| Última firma humana | `2026-04-13T05:46:50+00:00` | `2026-04-13 00:46:50 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.06 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:42:38 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:46:21 (Lima), es decir **4.06 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:42:37+00:00` | `2026-04-12 20:42:37 (Lima)` | -0.00h |
| 1 | YLAQUITA BERROA cristian Luis FIR 29387762 sw 633d6e089cdfbcefceb7a259b1cfd9e8790d5f8a | 29387762 | `2026-04-13T05:46:21+00:00` | `2026-04-13 00:46:21 (Lima)` | +4.06h |
| 2 | YSLA MEDRANO freddy Marcial FIR 09704259 sw cb733e19f8feda23c97bf2159932fb9a19837162 | 09704259 | `2026-04-13T05:46:35+00:00` | `2026-04-13 00:46:35 (Lima)` | +4.07h |
| 3 | VILLALTA AGURTO karla Dayana FIR 71262693 sw 4dde2fa88b3117177baac4679554ff7cb32bb1fe | 71262693 | `2026-04-13T05:46:50+00:00` | `2026-04-13 00:46:50 (Lima)` | +4.07h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **052294**
2. Descargar el PDF del acta
3. Verificar SHA-256: `14c4545dd94c3ff49b1edbcb6e3dca50b795598dc2a1174638b0036d9f0a4ca6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
