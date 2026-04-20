# Mesa 051120 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.904617+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IEP COLEGIO DE LA INMACULADA JESUITAS (código 14137)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 249
- Votos válidos: 243
- Participación: 83.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:52:21+00:00` | `2026-04-12 20:52:21 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:52:21+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:52:21+00:00` | `2026-04-12 20:52:21 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:34:36+00:00` | `2026-04-12 22:34:36 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:35:21+00:00` | `2026-04-12 22:35:21 (Lima)` |
| Última firma humana | `2026-04-13T03:37:11+00:00` | `2026-04-12 22:37:11 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.72 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:52:21 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:35:21 (Lima), es decir **1.72 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:52:19+00:00` | `2026-04-12 20:52:19 (Lima)` | -0.00h |
| 1 | URDANETA ALFARO jenny Carolina FIR 49064871 sw f0a04f03439324cf4d8c6cc121d0ea3699d1e1fd | 49064871 | `2026-04-13T03:35:21+00:00` | `2026-04-12 22:35:21 (Lima)` | +1.72h |
| 2 | VERA SALAS medalit Maria FIR 04413389 sw 022ae2063ee298d979cace64a1c592254e56d1ad | 04413389 | `2026-04-13T03:35:36+00:00` | `2026-04-12 22:35:36 (Lima)` | +1.72h |
| 3 | URIBE FUENTES CASTRO aida Danire FIR 09870462 sw 8e3c4c23b8ff87e49a7c1c66ca90ce97012ebc09 | 09870462 | `2026-04-13T03:35:52+00:00` | `2026-04-12 22:35:52 (Lima)` | +1.73h |
| 4 | VELIZ VILLENA anggie Geraldine FIR 70686272 sw 81e18bbd384203b87875077923adfae073428494 | 70686272 | `2026-04-13T03:37:11+00:00` | `2026-04-12 22:37:11 (Lima)` | +1.75h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051120**
2. Descargar el PDF del acta
3. Verificar SHA-256: `0c1ef2f481b107d8c8b8d72da7a8352257b5ba518255a8036139ccb163355257`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
