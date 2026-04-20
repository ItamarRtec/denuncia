# Mesa 055164 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.521164+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 7079 RAMIRO PRIALE PRIALE (código 3367)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 243
- Votos válidos: 209
- Participación: 81.271%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:52:26+00:00` | `2026-04-12 20:52:26 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:52:26+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:52:26+00:00` | `2026-04-12 20:52:26 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:30:48+00:00` | `2026-04-13 08:30:48 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:31:10+00:00` | `2026-04-13 08:31:10 (Lima)` |
| Última firma humana | `2026-04-13T13:31:38+00:00` | `2026-04-13 08:31:38 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.65 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:52:26 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:31:10 (Lima), es decir **11.65 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:52:23+00:00` | `2026-04-12 20:52:23 (Lima)` | -0.00h |
| 1 | ANTAURCO INTI sergio Bryan FIR 74092274 sw 71864b18b022059a0997157472ae978c5d890f5a | 74092274 | `2026-04-13T13:31:10+00:00` | `2026-04-13 08:31:10 (Lima)` | +11.65h |
| 2 | AQUINO VELASQUEZ lizbeth Paola FIR 60759816 sw 51a2d97b4c2e889efaaa5106129830d88a5464c4 | 60759816 | `2026-04-13T13:31:25+00:00` | `2026-04-13 08:31:25 (Lima)` | +11.65h |
| 3 | AMARU HUAMANI jose David FIR 74178072 sw 9161356df0a73c69761c39755cf0ecee22873436 | 74178072 | `2026-04-13T13:31:38+00:00` | `2026-04-13 08:31:38 (Lima)` | +11.65h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055164**
2. Descargar el PDF del acta
3. Verificar SHA-256: `dda65648dfc37a4fd31074a9c282574f24c28b3c1cf1d2d3cd16384ec8f4efa2`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
