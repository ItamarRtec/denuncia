# Mesa 050946 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:09.494884+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: UNIVERSIDAD MARCELINO CHAMPAGNAT (código 3220)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 287
- Votos válidos: 284
- Participación: 95.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:47:57+00:00` | `2026-04-12 20:47:57 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:47:57+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:47:57+00:00` | `2026-04-12 20:47:57 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:50:56+00:00` | `2026-04-12 22:50:56 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:59:41+00:00` | `2026-04-12 22:59:41 (Lima)` |
| Última firma humana | `2026-04-13T04:00:23+00:00` | `2026-04-12 23:00:23 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.20 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:47:57 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:59:41 (Lima), es decir **2.20 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:47:55+00:00` | `2026-04-12 20:47:55 (Lima)` | -0.00h |
| 1 | CUADROS BOBADILLA cynthia Marleny FIR 42627351 sw ee489fb9dcd5a4504d2b228d33872d21095d10df | 42627351 | `2026-04-13T03:59:41+00:00` | `2026-04-12 22:59:41 (Lima)` | +2.20h |
| 2 | DAVILA GALLO cecilia Katherine FIR 42868560 sw cd8e31096607f08c2b8391d2457ee5154fbed223 | 42868560 | `2026-04-13T04:00:05+00:00` | `2026-04-12 23:00:05 (Lima)` | +2.20h |
| 3 | DEL AGUILA RIOS jose Alfredo FIR 07252575 sw a94e8744e4a32637f1b313396b8c4118518b91e1 | 07252575 | `2026-04-13T04:00:23+00:00` | `2026-04-12 23:00:23 (Lima)` | +2.21h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050946**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4ec869c299e597c9f393aebe135a0246016c6b2cbf79c4b1134ea8dff8f6b471`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
