# Mesa 036046 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.542754+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE 0035 NUESTRA SEÑORA DE LA VISITACION (código 2640)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 233
- Votos válidos: 217
- Participación: 77.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:09:16+00:00` | `2026-04-12 20:09:16 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:09:16+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:09:16+00:00` | `2026-04-12 20:09:16 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T08:24:42+00:00` | `2026-04-13 03:24:42 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T08:25:21+00:00` | `2026-04-13 03:25:21 (Lima)` |
| Última firma humana | `2026-04-13T08:26:08+00:00` | `2026-04-13 03:26:08 (Lima)` |

**Brecha primera firma humana vs publicación:** **+7.27 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:09:16 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 03:25:21 (Lima), es decir **7.27 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:09:14+00:00` | `2026-04-12 20:09:14 (Lima)` | -0.00h |
| 1 | FLORES QUISPE edwin FIR 09795488 sw 38f83ebcb788867a9c11c27583529dc85c315225 | 09795488 | `2026-04-13T08:25:21+00:00` | `2026-04-13 03:25:21 (Lima)` | +7.27h |
| 2 | ESPINO ROJAS luis Alberto FIR 06188677 sw 330dd95a125b52acfe5b22f3f9328496cb4c9b07 | 06188677 | `2026-04-13T08:25:54+00:00` | `2026-04-13 03:25:54 (Lima)` | +7.28h |
| 3 | FARFAN COLOS franco Alfredo FIR 61294979 sw 4436833679fc6252d51f024de402f1a4e294fc85 | 61294979 | `2026-04-13T08:26:08+00:00` | `2026-04-13 03:26:08 (Lima)` | +7.28h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036046**
2. Descargar el PDF del acta
3. Verificar SHA-256: `590fbeba8cd09fe855469e1eadc40bf65e9c7adea122fd12536750c8461a9ad6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
