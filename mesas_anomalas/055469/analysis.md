# Mesa 055469 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.218869+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IEP SACO OLIVEROS (código 3384)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 261
- Votos válidos: 224
- Participación: 87.291%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:29:57+00:00` | `2026-04-12 21:29:57 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:29:57+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:29:57+00:00` | `2026-04-12 21:29:57 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:28:04+00:00` | `2026-04-12 22:28:04 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:28:14+00:00` | `2026-04-12 22:28:14 (Lima)` |
| Última firma humana | `2026-04-13T03:28:35+00:00` | `2026-04-12 22:28:35 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.97 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:29:57 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:28:14 (Lima), es decir **0.97 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:24:13+00:00` | `2026-04-12 21:24:13 (Lima)` | -0.10h |
| 1 | CARHUAY ZARZOSA guisela Margarita FIR 40240556 sw 57e38b38fecdb36a4adf5ebc4fcdbaa853542e13 | 40240556 | `2026-04-13T03:28:14+00:00` | `2026-04-12 22:28:14 (Lima)` | +0.97h |
| 2 | CERRON GALVAN obdulia FIR 20097655 sw 4703eabe57ad59073895e6cff1e5149a84fbe841 | 20097655 | `2026-04-13T03:28:25+00:00` | `2026-04-12 22:28:25 (Lima)` | +0.97h |
| 3 | CHAVEZ SALAZAR arnold Fores FIR 75441254 sw de030fadabd6aff68a6701c2f7def21ccb2dccd8 | 75441254 | `2026-04-13T03:28:35+00:00` | `2026-04-12 22:28:35 (Lima)` | +0.98h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055469**
2. Descargar el PDF del acta
3. Verificar SHA-256: `b4bb6825fa34d1eeadb8f4a853509368d02cebf7810338a2f6916b9edc706bf4`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
