# Mesa 082851 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.876093+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: CARMEN DE LA LEGUA - REYNOSO
- **Local de votación**: IEP ANTON COLLEGE (código 50399)
- **Ubigeo**: 240104

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 228
- Votos válidos: 195
- Participación: 76.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:54:55+00:00` | `2026-04-12 21:54:55 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:54:55+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:54:55+00:00` | `2026-04-12 21:54:55 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:38:40+00:00` | `2026-04-12 23:38:40 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:38:53+00:00` | `2026-04-12 23:38:53 (Lima)` |
| Última firma humana | `2026-04-13T04:40:50+00:00` | `2026-04-12 23:40:50 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.73 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:54:55 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:38:53 (Lima), es decir **1.73 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:54:52+00:00` | `2026-04-12 21:54:52 (Lima)` | -0.00h |
| 1 | ZAPATA RIVASPLATA hanssen David FIR 72884949 sw 6f7089163359b98aa2df4a8ab1b9e5e07b5eb306 | 72884949 | `2026-04-13T04:38:53+00:00` | `2026-04-12 23:38:53 (Lima)` | +1.73h |
| 2 | ZEVALLOS VINATEA giuliano Paul FIR 25775012 sw a0eb25568cbc23797caeddeb9fcb756f3a78453c | 25775012 | `2026-04-13T04:39:04+00:00` | `2026-04-12 23:39:04 (Lima)` | +1.74h |
| 3 | ZARATE CANELAO janck Carlos FIR 47731644 sw ac98d9521efff2062e0a6ac8eadabd01b9402382 | 47731644 | `2026-04-13T04:39:14+00:00` | `2026-04-12 23:39:14 (Lima)` | +1.74h |
| 4 | VASQUEZ POVEA diana Carolina FIR 47885446 sw feb2cdd733936eba57b042838c8f830502afda4f | 47885446 | `2026-04-13T04:39:59+00:00` | `2026-04-12 23:39:59 (Lima)` | +1.75h |
| 5 | MONTEDORO BERNAOLA alfredo Manuel FIR 25700700 sw fe4f7aeea3c75d32fc423c7e3b5794cd40e9e553 | 25700700 | `2026-04-13T04:40:50+00:00` | `2026-04-12 23:40:50 (Lima)` | +1.77h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082851**
2. Descargar el PDF del acta
3. Verificar SHA-256: `99e424f9bd5e03ac23b3fa20fa61426beea8f5ca4dbe9c4f88cbb22a5082091b`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
