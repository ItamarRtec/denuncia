# Mesa 054357 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.732078+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: EL AGUSTINO
- **Local de votación**: IE 1044 MARIA REICHE NEWMANN (código 3328)
- **Ubigeo**: 140135

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 250
- Votos válidos: 223
- Participación: 83.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:01:43+00:00` | `2026-04-12 22:01:43 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:01:43+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:01:43+00:00` | `2026-04-12 22:01:43 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:25:55+00:00` | `2026-04-13 08:25:55 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:26:13+00:00` | `2026-04-13 08:26:13 (Lima)` |
| Última firma humana | `2026-04-13T13:27:15+00:00` | `2026-04-13 08:27:15 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.41 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:01:43 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:26:13 (Lima), es decir **10.41 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:01:41+00:00` | `2026-04-12 22:01:41 (Lima)` | -0.00h |
| 1 | LOYOLA GIRALDO grease Maryori FIR 72817445 sw 22080cbafd8440fe78428c56699ad67a32a29756 | 72817445 | `2026-04-13T13:26:13+00:00` | `2026-04-13 08:26:13 (Lima)` | +10.41h |
| 2 | LOPEZ YAYA paulina Maria FIR 09503057 sw e41c5fdd6c0b4cd0af21fc8970b2d9be8e243d46 | 09503057 | `2026-04-13T13:27:01+00:00` | `2026-04-13 08:27:01 (Lima)` | +10.42h |
| 3 | LAZARTE SANTOS melfi Klaribel FIR 45669180 sw 09c989cc81a07b4e33775120e231b323ca4e492b | 45669180 | `2026-04-13T13:27:15+00:00` | `2026-04-13 08:27:15 (Lima)` | +10.43h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **054357**
2. Descargar el PDF del acta
3. Verificar SHA-256: `07b803c4c863aced326df3f3e8fe4ab28a06ead603da8d6cf91b5af2fd65c6da`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
