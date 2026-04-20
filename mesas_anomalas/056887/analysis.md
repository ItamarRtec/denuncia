# Mesa 056887 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:04.823741+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IE 149 CAPITAN PNP JORGE CIEZA LACHOS (código 3441)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 261
- Votos válidos: 235
- Participación: 87.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:40:39+00:00` | `2026-04-12 20:40:39 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:40:39+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:40:39+00:00` | `2026-04-12 20:40:39 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:20:36+00:00` | `2026-04-12 22:20:36 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:20:51+00:00` | `2026-04-12 22:20:51 (Lima)` |
| Última firma humana | `2026-04-13T03:21:15+00:00` | `2026-04-12 22:21:15 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.67 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:40:39 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:20:51 (Lima), es decir **1.67 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:40:37+00:00` | `2026-04-12 20:40:37 (Lima)` | -0.00h |
| 1 | MEDINA NAVARRO felipe Augusto FIR 09328399 sw cbc0a87f83f5e91b6e592d95e9ffa0fa8b64246d | 09328399 | `2026-04-13T03:20:51+00:00` | `2026-04-12 22:20:51 (Lima)` | +1.67h |
| 2 | LOPEZ NAUPAY fabrizzio FIR 60942219 sw 1f1d8bc721dfa038a20c94dd1c5345b62b7feb63 | 60942219 | `2026-04-13T03:21:04+00:00` | `2026-04-12 22:21:04 (Lima)` | +1.67h |
| 3 | LUCANA QUISPE bridney FIR 60722271 sw d770df9571e4bd808881c7dfcde43dc75b4727fd | 60722271 | `2026-04-13T03:21:15+00:00` | `2026-04-12 22:21:15 (Lima)` | +1.68h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **056887**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8138f16f8757c86e487ae0b1334019353926acaf28e5a18ba3e62bf53a337ad3`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
