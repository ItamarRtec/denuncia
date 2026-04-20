# Mesa 051323 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.187945+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: UNIVERSIDAD DE LIMA 2 (código 51521)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 185
- Votos válidos: 179
- Participación: 61.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:54:45+00:00` | `2026-04-12 21:54:45 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:54:45+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:54:45+00:00` | `2026-04-12 21:54:45 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T17:05:22+00:00` | `2026-04-13 12:05:22 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T17:05:46+00:00` | `2026-04-13 12:05:46 (Lima)` |
| Última firma humana | `2026-04-13T17:06:23+00:00` | `2026-04-13 12:06:23 (Lima)` |

**Brecha primera firma humana vs publicación:** **+14.18 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:54:45 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 12:05:46 (Lima), es decir **14.18 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:50:39+00:00` | `2026-04-12 21:50:39 (Lima)` | -0.07h |
| 1 | ZEVALLOS SALAZAR josias FIR 47280595 sw 6dea52316568aee3d91e4a7addf465317e459119 | 47280595 | `2026-04-13T17:05:46+00:00` | `2026-04-13 12:05:46 (Lima)` | +14.18h |
| 2 | YATACO HOLGUIN yojana Yanet FIR 07877618 sw b35d4bebd5a4763556718eef7cfe62cc3899640f | 07877618 | `2026-04-13T17:06:10+00:00` | `2026-04-13 12:06:10 (Lima)` | +14.19h |
| 3 | YACTAYO FELIX percy Dennis FIR 46131844 sw 7f93da0665a30aec78cfcf9264070f0e8144cce2 | 46131844 | `2026-04-13T17:06:23+00:00` | `2026-04-13 12:06:23 (Lima)` | +14.19h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051323**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c43889512ad0dcfd1f8a75cae300e02065f42f2dfac1071b96a487375294d8da`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
