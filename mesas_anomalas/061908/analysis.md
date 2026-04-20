# Mesa 061908 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.983237+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTA ANITA
- **Local de votación**: UNIVERSIDAD SAN MARTIN DE PORRES (código 3595)
- **Ubigeo**: 140143

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 243
- Votos válidos: 216
- Participación: 81.271%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:24:24+00:00` | `2026-04-12 22:24:24 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:24:24+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:24:24+00:00` | `2026-04-12 22:24:24 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:58:10+00:00` | `2026-04-13 09:58:10 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:58:35+00:00` | `2026-04-13 09:58:35 (Lima)` |
| Última firma humana | `2026-04-13T14:59:09+00:00` | `2026-04-13 09:59:09 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.57 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:24:24 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:58:35 (Lima), es decir **11.57 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:24:22+00:00` | `2026-04-12 22:24:22 (Lima)` | -0.00h |
| 1 | HUANUCO HUAMAN edith Marilyn FIR 72279557 sw 5fa5b6602b23fc8afd0f4fb9628d4296c02ad4b1 | 72279557 | `2026-04-13T14:58:35+00:00` | `2026-04-13 09:58:35 (Lima)` | +11.57h |
| 2 | HUAYNAPOMAS LAURENTE juan Carlos FIR 10054440 sw 62a5a710eec8ad8d1380f1b13223f2ca979e499c | 10054440 | `2026-04-13T14:58:53+00:00` | `2026-04-13 09:58:53 (Lima)` | +11.57h |
| 3 | HUAPAYA RODRIGUEZ carmen Rosa FIR 09314698 sw e340b772bc0a203450db422f3f4356d600229ab1 | 09314698 | `2026-04-13T14:59:09+00:00` | `2026-04-13 09:59:09 (Lima)` | +11.58h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **061908**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8538e768d14740579b58a00f1604cd52def033817ad04334f1c6aaee99555eac`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
