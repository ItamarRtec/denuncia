# Mesa 035986 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.321739+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: UNIVERSIDAD NACIONAL FEDERICO VILLARREAL ESCUELA DE POST GRADO (código 2636)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 233
- Votos válidos: 197
- Participación: 77.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:02:21+00:00` | `2026-04-12 21:02:21 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:02:21+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:02:21+00:00` | `2026-04-12 21:02:21 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:19:38+00:00` | `2026-04-12 23:19:38 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:19:58+00:00` | `2026-04-12 23:19:58 (Lima)` |
| Última firma humana | `2026-04-13T04:20:27+00:00` | `2026-04-12 23:20:27 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.29 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:02:21 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:19:58 (Lima), es decir **2.29 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:02:19+00:00` | `2026-04-12 21:02:19 (Lima)` | -0.00h |
| 1 | GUANILO UPIACHIHUA cesar Augusto FIR 09803225 sw e31d50b91d15f10f3ff8c17094253196fe43d3dd | 09803225 | `2026-04-13T04:19:58+00:00` | `2026-04-12 23:19:58 (Lima)` | +2.29h |
| 2 | HILARIO MINAYA jhon Jhomar FIR 72846981 sw e0addb37fa92703035103561748983d4c8e3467c | 72846981 | `2026-04-13T04:20:09+00:00` | `2026-04-12 23:20:09 (Lima)` | +2.30h |
| 3 | HASTAHUAMAN LLANCO carlos FIR 41545826 sw 0607a42844f7f736298ce55bbaa5f6f8cb03e4ce | 41545826 | `2026-04-13T04:20:27+00:00` | `2026-04-12 23:20:27 (Lima)` | +2.30h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **035986**
2. Descargar el PDF del acta
3. Verificar SHA-256: `61450e0dcbc1095e16881e50876feee5d6fcd36bb1d87c13392d1236b7812811`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
