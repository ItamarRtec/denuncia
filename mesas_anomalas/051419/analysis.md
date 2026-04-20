# Mesa 051419 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.671855+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IEP ST GOSPA SCHOOL (código 52942)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 250
- Votos válidos: 234
- Participación: 83.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:59:34+00:00` | `2026-04-12 21:59:34 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:59:34+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:59:34+00:00` | `2026-04-12 21:59:34 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:29:43+00:00` | `2026-04-13 09:29:43 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:34:14+00:00` | `2026-04-13 09:34:14 (Lima)` |
| Última firma humana | `2026-04-13T14:39:33+00:00` | `2026-04-13 09:39:33 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.58 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:59:34 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:34:14 (Lima), es decir **11.58 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:59:32+00:00` | `2026-04-12 21:59:32 (Lima)` | -0.00h |
| 1 | KLEEBERG SALAZAR gerardo Enrique FIR 40750590 sw 5b94f682dbae8d30a0b4f53628a9f79f397af2ca | 40750590 | `2026-04-13T14:34:14+00:00` | `2026-04-13 09:34:14 (Lima)` | +11.58h |
| 2 | GUZMAN CASTILLO oscar Alfonso FIR 08759116 sw 9505b0b55dfeb4cb2719a3096fc2270d3ca77c42 | 08759116 | `2026-04-13T14:36:45+00:00` | `2026-04-13 09:36:45 (Lima)` | +11.62h |
| 3 | HUAPAYA LOAYZA jessica Margarita FIR 44976440 sw c9f5119f3e2f77198331bcb078dc8f81364fccab | 44976440 | `2026-04-13T14:39:33+00:00` | `2026-04-13 09:39:33 (Lima)` | +11.67h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051419**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e071111e21146de12a9e1cc5c4666b2b2087e94401268ba36db12d3522fb3fb3`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
