# Mesa 058203 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.903466+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IEP SAN FELIPE (código 51854)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 230
- Votos emitidos: 151
- Votos válidos: 118
- Participación: 65.652%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:33:59+00:00` | `2026-04-12 20:33:59 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:33:59+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:33:59+00:00` | `2026-04-12 20:33:59 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:12:54+00:00` | `2026-04-12 21:12:54 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:13:23+00:00` | `2026-04-12 21:13:23 (Lima)` |
| Última firma humana | `2026-04-13T02:16:19+00:00` | `2026-04-12 21:16:19 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.66 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:33:59 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:13:23 (Lima), es decir **0.66 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:33:57+00:00` | `2026-04-12 20:33:57 (Lima)` | -0.00h |
| 1 | ARIZAGA HUAMAN javier Eduardo FIR 10673566 sw 7aee38f258ee9828935f08205bcea071b8f0bd11 | 10673566 | `2026-04-13T02:13:23+00:00` | `2026-04-12 21:13:23 (Lima)` | +0.66h |
| 2 | APAZA HUANCA martin FIR 10352724 sw 33f7ab60ffaae1c2749d14c2bafe7d1dbe767944 | 10352724 | `2026-04-13T02:13:35+00:00` | `2026-04-12 21:13:35 (Lima)` | +0.66h |
| 3 | ALTAMIRANO ROCA yadira Yasei FIR 71285097 sw a0a8d9c72b406731edf365fe67cc37367b134c95 | 71285097 | `2026-04-13T02:16:19+00:00` | `2026-04-12 21:16:19 (Lima)` | +0.71h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **058203**
2. Descargar el PDF del acta
3. Verificar SHA-256: `57833a5441c65db60d59046d7d0b37e7bc98729d19755c92457e3ae1cc2389e2`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
