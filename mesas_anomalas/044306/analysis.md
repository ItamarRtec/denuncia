# Mesa 044306 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.559157+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LURIGANCHO
- **Local de votación**: IE 1224 (código 13431)
- **Ubigeo**: 140112

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 217
- Votos válidos: 189
- Participación: 72.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:45:00+00:00` | `2026-04-12 20:45:00 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:45:00+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:45:00+00:00` | `2026-04-12 20:45:00 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:18:30+00:00` | `2026-04-13 08:18:30 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:19:14+00:00` | `2026-04-13 08:19:14 (Lima)` |
| Última firma humana | `2026-04-13T13:21:11+00:00` | `2026-04-13 08:21:11 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.57 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:45:00 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:19:14 (Lima), es decir **11.57 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:44:58+00:00` | `2026-04-12 20:44:58 (Lima)` | -0.00h |
| 1 | CANCHANYA TACAS luis Miguel FIR 80070869 sw 82c8f944aaa8d17d5206616cfaaf91865796697c | 80070869 | `2026-04-13T13:19:14+00:00` | `2026-04-13 08:19:14 (Lima)` | +11.57h |
| 2 | CONTRERAS PALOMINO yenny FIR 43421153 sw 92a58182e05477a51f8a5649a3d870ffe678f8dc | 43421153 | `2026-04-13T13:19:33+00:00` | `2026-04-13 08:19:33 (Lima)` | +11.58h |
| 3 | CHAVEZ MOLEROS gladys FIR 10297328 sw 3b261a869a2b0f2e73958f8eb1de81eb35706482 | 10297328 | `2026-04-13T13:19:49+00:00` | `2026-04-13 08:19:49 (Lima)` | +11.58h |
| 4 | CARHUA JULCA humberto Magno FIR 71303942 sw 48b50bee6b045d4beb86b8207549de308b50406c | 71303942 | `2026-04-13T13:20:48+00:00` | `2026-04-13 08:20:48 (Lima)` | +11.60h |
| 5 | VALDIVIA VILCA santa Eulalia FIR 41757562 sw fb1f3d0d8314849c92ca5b37b9b9e31a735d6e32 | 41757562 | `2026-04-13T13:21:11+00:00` | `2026-04-13 08:21:11 (Lima)` | +11.60h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **044306**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3a016e940c216aca631e5dc14d8fd385d8b6d398e35233c7b197db7d52e329a7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
