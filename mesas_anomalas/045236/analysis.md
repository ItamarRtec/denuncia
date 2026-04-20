# Mesa 045236 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.303912+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: IEP SANTA RITA DE CASIA (código 2996)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 230
- Votos emitidos: 174
- Votos válidos: 163
- Participación: 75.652%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:45:48+00:00` | `2026-04-12 20:45:48 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:45:48+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:45:48+00:00` | `2026-04-12 20:45:48 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:38:42+00:00` | `2026-04-13 07:38:42 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:39:18+00:00` | `2026-04-13 07:39:18 (Lima)` |
| Última firma humana | `2026-04-13T12:40:13+00:00` | `2026-04-13 07:40:13 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.89 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:45:48 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:39:18 (Lima), es decir **10.89 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:45:46+00:00` | `2026-04-12 20:45:46 (Lima)` | -0.00h |
| 1 | APARICIO SALCEDO bruno Sebastian FIR 71245010 sw 0d6af066b3a70c2ce0e7a1781f29af0f39dbbffe | 71245010 | `2026-04-13T12:39:18+00:00` | `2026-04-13 07:39:18 (Lima)` | +10.89h |
| 2 | ALEJOS MORALES viviana Guadalupe FIR 09339509 sw 2ecc207427ede5ca0f3e099bb18880c9a99b880b | 09339509 | `2026-04-13T12:39:47+00:00` | `2026-04-13 07:39:47 (Lima)` | +10.90h |
| 3 | GAGO CARTULIN guillermo Rafael FIR 10553916 sw d833beff152affb27a4687b79e68831c120dd136 | 10553916 | `2026-04-13T12:40:13+00:00` | `2026-04-13 07:40:13 (Lima)` | +10.91h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045236**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c548b0a8552fb35d95f443ab7cc6cddfac0a7414e404785b896ad6963fc7f565`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
