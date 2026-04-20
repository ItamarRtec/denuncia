# Mesa 045517 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.399859+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PACHACÁMAC
- **Local de votación**: IE 6007 (código 3001)
- **Ubigeo**: 140116

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 243
- Votos válidos: 215
- Participación: 81.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:08:35+00:00` | `2026-04-12 21:08:35 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:08:35+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:08:35+00:00` | `2026-04-12 21:08:35 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T06:11:41+00:00` | `2026-04-13 01:11:41 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:12:33+00:00` | `2026-04-13 01:12:33 (Lima)` |
| Última firma humana | `2026-04-13T06:13:02+00:00` | `2026-04-13 01:13:02 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.07 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:08:35 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:12:33 (Lima), es decir **4.07 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:08:31+00:00` | `2026-04-12 21:08:31 (Lima)` | -0.00h |
| 1 | MENDOZA BULEJE wilfredo Valentin FIR 42183919 sw c0a89197d8a5750772cc865623e3815f423ca181 | 42183919 | `2026-04-13T06:12:33+00:00` | `2026-04-13 01:12:33 (Lima)` | +4.07h |
| 2 | PALOMINO BERROSPI lucia Natividad FIR 07386387 sw ab7ad6a3d16789d08fc84a091d551f5ad2b0eb50 | 07386387 | `2026-04-13T06:12:49+00:00` | `2026-04-13 01:12:49 (Lima)` | +4.07h |
| 3 | PALOMINO CARHUAPUMA grimanex Donato FIR 70441728 sw f95b1556c2cdead676b8d2f6f72757dce97be683 | 70441728 | `2026-04-13T06:13:02+00:00` | `2026-04-13 01:13:02 (Lima)` | +4.07h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045517**
2. Descargar el PDF del acta
3. Verificar SHA-256: `046b50a2151a7a3227c293c77c2302f168cbf801eaa7e27890478f7f37130e06`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
