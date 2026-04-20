# Mesa 037103 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:11.387205+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: ANCÓN
- **Local de votación**: IE NUESTRA SEÑORA DE LA PAZ (código 27077)
- **Ubigeo**: 140102

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 230
- Votos emitidos: 163
- Votos válidos: 131
- Participación: 70.87%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:34:30+00:00` | `2026-04-12 20:34:30 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:34:30+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:34:30+00:00` | `2026-04-12 20:34:30 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:17:05+00:00` | `2026-04-12 22:17:05 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:17:18+00:00` | `2026-04-12 22:17:18 (Lima)` |
| Última firma humana | `2026-04-13T03:18:35+00:00` | `2026-04-12 22:18:35 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.71 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:34:30 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:17:18 (Lima), es decir **1.71 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:34:27+00:00` | `2026-04-12 20:34:27 (Lima)` | -0.00h |
| 1 | ADAUTO DELGADO johnny Andoni FIR 75481195 sw 92d80639e9881c2e3d2e9847ec720a0a1609cbdc | 75481195 | `2026-04-13T03:17:18+00:00` | `2026-04-12 22:17:18 (Lima)` | +1.71h |
| 2 | ALTAMIRANO ROJAS yoni FIR 60154375 sw e3bb85acb3e1be1f216ab57ca1d1d1d4d1a4b1b1 | 60154375 | `2026-04-13T03:17:36+00:00` | `2026-04-12 22:17:36 (Lima)` | +1.72h |
| 3 | ALEJOS LEON nilton Joel FIR 73662971 sw c9ad1946fe288965f13275264b16ea871e2cecec | 73662971 | `2026-04-13T03:17:48+00:00` | `2026-04-12 22:17:48 (Lima)` | +1.72h |
| 4 | GUTIERREZ QUISPE janeth Maribel FIR 44525939 sw 5e8426267f92e8590f24bcd2ed1484b9d0cebe64 | 44525939 | `2026-04-13T03:18:23+00:00` | `2026-04-12 22:18:23 (Lima)` | +1.73h |
| 5 | ABANTO DIAZ kenn Robinson FIR 74064419 sw ff9b7d695d1f054ad6d625a95b832a6b0dd33845 | 74064419 | `2026-04-13T03:18:35+00:00` | `2026-04-12 22:18:35 (Lima)` | +1.73h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **037103**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8080ef7e7deeb0d3fbec70c44a8f8a4f1a696b626e5728388e6481f9abbc003f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
