# Mesa 049982 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.508519+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: IEP SANTO DOMINGO EL APOSTOL (código 3168)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 298
- Votos emitidos: 244
- Votos válidos: 224
- Participación: 81.879%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:02:03+00:00` | `2026-04-12 21:02:03 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:02:03+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:02:03+00:00` | `2026-04-12 21:02:03 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:45:40+00:00` | `2026-04-12 23:45:40 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T04:46:18+00:00` | `2026-04-12 23:46:18 (Lima)` |
| Última firma humana | `2026-04-13T04:46:34+00:00` | `2026-04-12 23:46:34 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.74 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:02:03 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 23:46:18 (Lima), es decir **2.74 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:02:01+00:00` | `2026-04-12 21:02:01 (Lima)` | -0.00h |
| 1 | NASSAR  khaled Abdelmoneim Ahmed FIR 48181780 sw 9e931902dd69a89d3fb075c30428df13f4f2e734 | 48181780 | `2026-04-13T04:46:18+00:00` | `2026-04-12 23:46:18 (Lima)` | +2.74h |
| 2 | MURO VARGAS elizabeth Julia FIR 09077587 sw e29a06ebd3b38db681a41302bad3e53db2cf1b51 | 09077587 | `2026-04-13T04:46:34+00:00` | `2026-04-12 23:46:34 (Lima)` | +2.74h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **049982**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e5e82ff5fb5e89ce2b86584d1b30482e2ec189724c1a7c4aa25a99598b7deacc`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
