# Mesa 045682 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.188789+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PACHACÁMAC
- **Local de votación**: IEP SEÑOR DE LA ASCENSION (código 13538)
- **Ubigeo**: 140116

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 245
- Votos válidos: 204
- Participación: 81.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:28:46+00:00` | `2026-04-12 20:28:46 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:28:46+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:28:46+00:00` | `2026-04-12 20:28:46 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:51:02+00:00` | `2026-04-12 22:51:02 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:51:32+00:00` | `2026-04-12 22:51:32 (Lima)` |
| Última firma humana | `2026-04-13T03:52:06+00:00` | `2026-04-12 22:52:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.38 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:28:46 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:51:32 (Lima), es decir **2.38 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:28:43+00:00` | `2026-04-12 20:28:43 (Lima)` | -0.00h |
| 1 | CHIPANA BALDEON jaime FIR 10600897 sw 56913605e0a7ab72e77bdc385f1b7ba727b03446 | 10600897 | `2026-04-13T03:51:32+00:00` | `2026-04-12 22:51:32 (Lima)` | +2.38h |
| 2 | CONDORI QUISPE richard FIR 42062854 sw ede7e3bd664a552262499956887695487388fee2 | 42062854 | `2026-04-13T03:51:49+00:00` | `2026-04-12 22:51:49 (Lima)` | +2.38h |
| 3 | COTERA SEGURA vanessa Amelia FIR 46469989 sw 6b7a4d18eb989d32f16efaa62c50f6954d355385 | 46469989 | `2026-04-13T03:52:06+00:00` | `2026-04-12 22:52:06 (Lima)` | +2.39h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045682**
2. Descargar el PDF del acta
3. Verificar SHA-256: `af950e7e7bdf6fccd6537cf92f6c5d5fc342bc4da5da0c08cfe1e033c5ebf1b7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
