# Mesa 083583 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.555870+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: VENTANILLA
- **Local de votación**: IE 5138 (código 10027)
- **Ubigeo**: 240106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 249
- Votos válidos: 208
- Participación: 83.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:27:04+00:00` | `2026-04-12 21:27:04 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:27:04+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:27:04+00:00` | `2026-04-12 21:27:04 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:44:04+00:00` | `2026-04-13 08:44:04 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:54:45+00:00` | `2026-04-13 08:54:45 (Lima)` |
| Última firma humana | `2026-04-13T13:55:11+00:00` | `2026-04-13 08:55:11 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.46 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:27:04 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:54:45 (Lima), es decir **11.46 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:27:01+00:00` | `2026-04-12 21:27:01 (Lima)` | -0.00h |
| 1 | RAMOS GUADALUPE katherin Marilin FIR 76971788 sw 46b2af12886bf1104b633047221ab7f24c0079e1 | 76971788 | `2026-04-13T13:54:45+00:00` | `2026-04-13 08:54:45 (Lima)` | +11.46h |
| 2 | SAAVEDRA QUISPE cintia Del Rosario FIR 45359404 sw f75a19d5d3e2b66e2cc73049e45a220bc81d03ec | 45359404 | `2026-04-13T13:54:59+00:00` | `2026-04-13 08:54:59 (Lima)` | +11.47h |
| 3 | REYES VARGAS luis Armando FIR 47031396 sw cbd7b5208c089fe6d973146a049195a3be8616ce | 47031396 | `2026-04-13T13:55:11+00:00` | `2026-04-13 08:55:11 (Lima)` | +11.47h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **083583**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5dea62e608a2599329296ce5b29d7ad34f3aecc14fece286c04586957fee519e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
