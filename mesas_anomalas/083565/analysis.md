# Mesa 083565 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.099466+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: VENTANILLA
- **Local de votación**: IE 5130  3 VICTOR RAUL HAYA DE LA TORRE (código 10024)
- **Ubigeo**: 240106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 242
- Votos válidos: 213
- Participación: 80.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:24:50+00:00` | `2026-04-12 22:24:50 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:24:50+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:24:50+00:00` | `2026-04-12 22:24:50 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T06:00:21+00:00` | `2026-04-13 01:00:21 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:00:33+00:00` | `2026-04-13 01:00:33 (Lima)` |
| Última firma humana | `2026-04-13T06:01:30+00:00` | `2026-04-13 01:01:30 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.60 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:24:50 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:00:33 (Lima), es decir **2.60 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:24:47+00:00` | `2026-04-12 22:24:47 (Lima)` | -0.00h |
| 1 | CHAVEZ TITO jorge Edgar FIR 08665856 sw 153a88e48e9f50b0115ae32ef342826b891e8eba | 08665856 | `2026-04-13T06:00:33+00:00` | `2026-04-13 01:00:33 (Lima)` | +2.60h |
| 2 | CHAMBI QUISPE gualberto FIR 07432589 sw 096bf86766816250dae2092cd461f006c2195e3e | 07432589 | `2026-04-13T06:01:06+00:00` | `2026-04-13 01:01:06 (Lima)` | +2.60h |
| 3 | CONDORI MACHACA giovana Isabel FIR 42429247 sw 59f49ceec5f70fb74c3be308169705f2af22ee23 | 42429247 | `2026-04-13T06:01:17+00:00` | `2026-04-13 01:01:17 (Lima)` | +2.61h |
| 4 | MARTEL LOZANO candy Mayra FIR 45277965 sw 89ff18fcd4b5e86529e52d26075be0ca39828025 | 45277965 | `2026-04-13T06:01:30+00:00` | `2026-04-13 01:01:30 (Lima)` | +2.61h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083565**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5cca4d798f4da40f6bf118dc9893b3e4bd906e3ffeb5f83cde5a2b2089466e45`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
