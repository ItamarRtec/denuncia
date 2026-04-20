# Mesa 050833 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.255851+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IEI 086 NUESTRA SEÑORA DEL CARMEN (código 3210)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 253
- Votos válidos: 229
- Participación: 84.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:36:22+00:00` | `2026-04-12 20:36:22 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:36:22+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:36:22+00:00` | `2026-04-12 20:36:22 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:55:15+00:00` | `2026-04-13 07:55:15 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:56:27+00:00` | `2026-04-13 07:56:27 (Lima)` |
| Última firma humana | `2026-04-13T12:57:07+00:00` | `2026-04-13 07:57:07 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.33 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:36:22 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:56:27 (Lima), es decir **11.33 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:36:20+00:00` | `2026-04-12 20:36:20 (Lima)` | -0.00h |
| 1 | GODINEZ VILLALOBOS melisa Del Carmen FIR 10810124 sw 9a4a79637a8b9697ede2a9609b1a0df69e0c584e | 10810124 | `2026-04-13T12:56:27+00:00` | `2026-04-13 07:56:27 (Lima)` | +11.33h |
| 2 | OROZCO TOMAYLLA yuliano FIR 10434300 sw a69eac00112ca7a46a3e4065a1effaaab8cd8b5b | 10434300 | `2026-04-13T12:56:47+00:00` | `2026-04-13 07:56:47 (Lima)` | +11.34h |
| 3 | HEREDIA CALVERA giomar David FIR 07446849 sw edf14cf78c4a59fd2869b3092c5903294d88077a | 07446849 | `2026-04-13T12:57:07+00:00` | `2026-04-13 07:57:07 (Lima)` | +11.35h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050833**
2. Descargar el PDF del acta
3. Verificar SHA-256: `acd8afeaccaafce8cc476c4a7e56fa6a3a1a87d6c3f2dcd1e5f41c21f5b5d058`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
