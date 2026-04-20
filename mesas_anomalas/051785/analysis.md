# Mesa 051785 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.426403+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: IE NUESTRA SEÑORA DE LOURDES (código 3233)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 219
- Votos válidos: 201
- Participación: 73.244%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:57:20+00:00` | `2026-04-12 19:57:20 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:57:20+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:57:20+00:00` | `2026-04-12 19:57:20 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:00:22+00:00` | `2026-04-12 22:00:22 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:00:52+00:00` | `2026-04-12 22:00:52 (Lima)` |
| Última firma humana | `2026-04-13T03:01:10+00:00` | `2026-04-12 22:01:10 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.06 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:57:20 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:00:52 (Lima), es decir **2.06 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:57:18+00:00` | `2026-04-12 19:57:18 (Lima)` | -0.00h |
| 1 | CASTRO CHUNGA joshua Emanuel FIR 61106969 sw 5fe230a4114eb9219d36be1a5e9134a61b442cf5 | 61106969 | `2026-04-13T03:00:52+00:00` | `2026-04-12 22:00:52 (Lima)` | +2.06h |
| 2 | CHURATA PAUCAR marcelino FIR 21866774 sw 8ac49f127c5d4d364b514b93ff0555e0e631ad35 | 21866774 | `2026-04-13T03:01:01+00:00` | `2026-04-12 22:01:01 (Lima)` | +2.06h |
| 3 | CHIPAO PUMACAYO kelvin Felix FIR 43053383 sw 57976731c004c7c77402d52e2020fb620f588d42 | 43053383 | `2026-04-13T03:01:10+00:00` | `2026-04-12 22:01:10 (Lima)` | +2.06h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051785**
2. Descargar el PDF del acta
3. Verificar SHA-256: `021ddda8e5567ae37166bac4ca5ff1edf96558c1a8f87516d826a978f00a1133`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
