# Mesa 056660 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.354415+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IE 126 JAVIER PEREZ DE CUELLAR (código 3425)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 236
- Votos emitidos: 200
- Votos válidos: 188
- Participación: 84.746%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:02:23+00:00` | `2026-04-12 20:02:23 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:02:23+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:02:23+00:00` | `2026-04-12 20:02:23 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:39:59+00:00` | `2026-04-13 07:39:59 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:47:03+00:00` | `2026-04-13 07:47:03 (Lima)` |
| Última firma humana | `2026-04-13T12:50:49+00:00` | `2026-04-13 07:50:49 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.74 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:02:23 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:47:03 (Lima), es decir **11.74 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:02:21+00:00` | `2026-04-12 20:02:21 (Lima)` | -0.00h |
| 1 | ALVAREZ JORGE juily FIR 41222870 sw cc4a9749b08d270e1b6bf4f77c7412dd9854be7b | 41222870 | `2026-04-13T12:47:03+00:00` | `2026-04-13 07:47:03 (Lima)` | +11.74h |
| 2 | ALTAMIRANO REA olga FIR 42274235 sw e6ca7144bc7532cd05c15f934c2e98b527953816 | 42274235 | `2026-04-13T12:48:57+00:00` | `2026-04-13 07:48:57 (Lima)` | +11.78h |
| 3 | ACO PALACIOS odalis Katy FIR 45802675 sw 86db2592d4a06d420f1fd06ea38ef07022864c25 | 45802675 | `2026-04-13T12:50:49+00:00` | `2026-04-13 07:50:49 (Lima)` | +11.81h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **056660**
2. Descargar el PDF del acta
3. Verificar SHA-256: `b4583b6f295c5f18ff4774463a827c2cdfb5aa95a078d534c25254c6f7a5e0c6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
