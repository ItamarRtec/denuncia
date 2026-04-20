# Mesa 036069 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.908345+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE 1001 JOSE JIMENEZ BORJA (código 2642)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 245
- Votos válidos: 221
- Participación: 81.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:40:31+00:00` | `2026-04-12 20:40:31 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:40:31+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:40:31+00:00` | `2026-04-12 20:40:31 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:15:18+00:00` | `2026-04-12 22:15:18 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:15:49+00:00` | `2026-04-12 22:15:49 (Lima)` |
| Última firma humana | `2026-04-13T03:16:07+00:00` | `2026-04-12 22:16:07 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.59 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:40:31 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:15:49 (Lima), es decir **1.59 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:40:28+00:00` | `2026-04-12 20:40:28 (Lima)` | -0.00h |
| 1 | DEL VALLE MENDOZA gonzalo Fernando FIR 08027400 sw 5fe45a07bebb3c6acd6c0096ecdca050b06d3712 | 08027400 | `2026-04-13T03:15:49+00:00` | `2026-04-12 22:15:49 (Lima)` | +1.59h |
| 2 | CORTEZ MEZA zaida Lisbeidy FIR 45759996 sw a6c2bda9e87a4c6674331d431394d07c322bff00 | 45759996 | `2026-04-13T03:16:07+00:00` | `2026-04-12 22:16:07 (Lima)` | +1.59h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036069**
2. Descargar el PDF del acta
3. Verificar SHA-256: `014da70fdcba54b0d197f84e3262086d2b0dd48329f71e001be8519958c0e24e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
