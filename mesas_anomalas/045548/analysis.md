# Mesa 045548 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.137001+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PACHACÁMAC
- **Local de votación**: IE ACCION CONJUNTA SAN SALVADOR (código 3005)
- **Ubigeo**: 140116

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 238
- Votos válidos: 212
- Participación: 79.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:39:15+00:00` | `2026-04-12 21:39:15 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:39:15+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:39:15+00:00` | `2026-04-12 21:39:15 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:25:57+00:00` | `2026-04-13 08:25:57 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:44:05+00:00` | `2026-04-13 08:44:05 (Lima)` |
| Última firma humana | `2026-04-13T13:44:57+00:00` | `2026-04-13 08:44:57 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.08 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:39:15 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:44:05 (Lima), es decir **11.08 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:34:48+00:00` | `2026-04-12 21:34:48 (Lima)` | -0.07h |
| 1 | SILVERIO SILVERIO henry Candelario FIR 40676438 sw 002560d79d773e8205397e134ed7e82440b756af | 40676438 | `2026-04-13T13:44:05+00:00` | `2026-04-13 08:44:05 (Lima)` | +11.08h |
| 2 | SILVA RIVAS bertha Gisel FIR 40124539 sw 2e59bdc2785fa52597bafd3786cac69a682d22fd | 40124539 | `2026-04-13T13:44:23+00:00` | `2026-04-13 08:44:23 (Lima)` | +11.09h |
| 3 | SIHUE ARROYO ronald John FIR 44090691 sw c21a94a7bf6dd9deb773a264312e1084bda5f500 | 44090691 | `2026-04-13T13:44:57+00:00` | `2026-04-13 08:44:57 (Lima)` | +11.10h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045548**
2. Descargar el PDF del acta
3. Verificar SHA-256: `b12ec4131e76db626ea8b546f3f45be288bcdc6a842415089d1c9bb86321d67d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
