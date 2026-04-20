# Mesa 045944 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.544556+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUEBLO LIBRE
- **Local de votación**: IESTP NACIONES UNIDAS (código 13564)
- **Ubigeo**: 140117

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 242
- Votos válidos: 218
- Participación: 80.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:02:51+00:00` | `2026-04-12 21:02:51 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:02:51+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:02:51+00:00` | `2026-04-12 21:02:51 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:26:51+00:00` | `2026-04-12 22:26:51 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:27:26+00:00` | `2026-04-12 22:27:26 (Lima)` |
| Última firma humana | `2026-04-13T03:28:13+00:00` | `2026-04-12 22:28:13 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.41 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:02:51 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:27:26 (Lima), es decir **1.41 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:02:49+00:00` | `2026-04-12 21:02:49 (Lima)` | -0.00h |
| 1 | HORNA HORNA pedro Enrique FIR 70101902 sw c816e9a3e4a368c847fac197bf59a30abfa868d5 | 70101902 | `2026-04-13T03:27:26+00:00` | `2026-04-12 22:27:26 (Lima)` | +1.41h |
| 2 | HUARI PEVES claudia Alejandra FIR 46405136 sw dee6c31f9fba2f3ae546e862f5c74aba2b3f26d4 | 46405136 | `2026-04-13T03:27:52+00:00` | `2026-04-12 22:27:52 (Lima)` | +1.42h |
| 3 | HUARACHI ALVARADO miguel Enrique FIR 76836548 sw 45cad6c7ae77a7e49f7b23b4d0467a90998bcaa2 | 76836548 | `2026-04-13T03:28:13+00:00` | `2026-04-12 22:28:13 (Lima)` | +1.42h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045944**
2. Descargar el PDF del acta
3. Verificar SHA-256: `0a9482eb73a42edadabd4fa208fc18ca878e25b410c36671d8f91bcf64e65d0c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
