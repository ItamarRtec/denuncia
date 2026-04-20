# Mesa 051056 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.099359+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IE 6097 MATEO PUMACAHUA (código 5120)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 220
- Votos válidos: 199
- Participación: 73.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:46:10+00:00` | `2026-04-12 20:46:10 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:46:10+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:46:10+00:00` | `2026-04-12 20:46:10 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:38:20+00:00` | `2026-04-13 07:38:20 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:39:02+00:00` | `2026-04-13 07:39:02 (Lima)` |
| Última firma humana | `2026-04-13T12:39:39+00:00` | `2026-04-13 07:39:39 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.88 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:46:10 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:39:02 (Lima), es decir **10.88 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:46:08+00:00` | `2026-04-12 20:46:08 (Lima)` | -0.00h |
| 1 | BALTAZAR DURAN carlos Wilmer FIR 10553322 sw d08b0693e0192b987136ebfb488c38f7e9032818 | 10553322 | `2026-04-13T12:39:02+00:00` | `2026-04-13 07:39:02 (Lima)` | +10.88h |
| 2 | AYBAR QUISPE dina Marisol FIR 40863713 sw c2349261aacabd6988f5a10cb1fc28e40afa5e92 | 40863713 | `2026-04-13T12:39:23+00:00` | `2026-04-13 07:39:23 (Lima)` | +10.89h |
| 3 | ASTO GUILLERMO reyna Marleny FIR 09881147 sw bf67f8a62c24acb1401ad3517a7561d40dfc3c52 | 09881147 | `2026-04-13T12:39:39+00:00` | `2026-04-13 07:39:39 (Lima)` | +10.89h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051056**
2. Descargar el PDF del acta
3. Verificar SHA-256: `7fafd4d4b7a85ba39e1ec766a6a77dadafe70d5c3a27db8ee155fad3a4722696`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
