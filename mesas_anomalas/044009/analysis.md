# Mesa 044009 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.967605+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LINCE
- **Local de votación**: PARQUE SANTOS DUMONT (código 53022)
- **Ubigeo**: 140111

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 250
- Votos válidos: 238
- Participación: 83.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:38:43+00:00` | `2026-04-12 20:38:43 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:38:43+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:38:43+00:00` | `2026-04-12 20:38:43 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:57:09+00:00` | `2026-04-12 21:57:09 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:57:38+00:00` | `2026-04-12 21:57:38 (Lima)` |
| Última firma humana | `2026-04-13T02:58:42+00:00` | `2026-04-12 21:58:42 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.32 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:38:43 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:57:38 (Lima), es decir **1.32 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:38:41+00:00` | `2026-04-12 20:38:41 (Lima)` | -0.00h |
| 1 | ORELLANO ESPINOZA lizbeth Esther FIR 76745726 sw d2cb7d597df623cd8742c89a85dfd3d706f08f2b | 76745726 | `2026-04-13T02:57:38+00:00` | `2026-04-12 21:57:38 (Lima)` | +1.32h |
| 2 | ORTIZ SUAREZ vladimir Oscar FIR 07611594 sw 68bfb84e77f31bec00c5dce76b9f829b2a55e98b | 07611594 | `2026-04-13T02:57:57+00:00` | `2026-04-12 21:57:57 (Lima)` | +1.32h |
| 3 | MIRANDA YAMAMOTO ana Maria FIR 07628752 sw 840b182fc56734ed41dccddc2938a82022ed4caa | 07628752 | `2026-04-13T02:58:07+00:00` | `2026-04-12 21:58:07 (Lima)` | +1.32h |
| 4 | FLORES RAMIREZ jorge Alberto FIR 08884187 sw eaa22fcfa2ee8530693c9af8b14a8ba8e1d73d19 | 08884187 | `2026-04-13T02:58:25+00:00` | `2026-04-12 21:58:25 (Lima)` | +1.33h |
| 5 | GAVINO ROMERO maria Isabel FIR 42558785 sw 1e1bf725901174ace2c3ea9b45f3bc931658e4b7 | 42558785 | `2026-04-13T02:58:42+00:00` | `2026-04-12 21:58:42 (Lima)` | +1.33h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **044009**
2. Descargar el PDF del acta
3. Verificar SHA-256: `884b8b334b60f80d8eaf005200801b4dfd92ac3819faa50301a6caaa0fb572a0`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
