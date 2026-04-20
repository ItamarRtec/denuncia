# Mesa 057542 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:07.232772+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IEP HEROES DEL PACIFICO (código 13799)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 280
- Votos emitidos: 259
- Votos válidos: 222
- Participación: 92.5%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:17:36+00:00` | `2026-04-12 21:17:36 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:17:36+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:17:36+00:00` | `2026-04-12 21:17:36 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:51:52+00:00` | `2026-04-13 08:51:52 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:52:54+00:00` | `2026-04-13 08:52:54 (Lima)` |
| Última firma humana | `2026-04-13T13:53:06+00:00` | `2026-04-13 08:53:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.59 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:17:36 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:52:54 (Lima), es decir **11.59 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:17:33+00:00` | `2026-04-12 21:17:33 (Lima)` | -0.00h |
| 1 | ALONZO SOTO abimael Vladimir FIR 43189502 sw 5e94ade90ef234e3e23a5138863cea62edbd3560 | 43189502 | `2026-04-13T13:52:54+00:00` | `2026-04-13 08:52:54 (Lima)` | +11.59h |
| 2 | CHIPANA VELILLE rony Leoncio FIR 70184933 sw 3518b0c761b13f0cba428ea8cd223f7f3669edc6 | 70184933 | `2026-04-13T13:53:06+00:00` | `2026-04-13 08:53:06 (Lima)` | +11.59h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **057542**
2. Descargar el PDF del acta
3. Verificar SHA-256: `cec13793366b15bf744413848f639a813942c13a2b9368197dbd10568c353a8c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
