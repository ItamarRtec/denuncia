# Mesa 036052 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.370534+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IE 0035 NUESTRA SEÑORA DE LA VISITACION (código 2640)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 241
- Votos válidos: 219
- Participación: 80.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T00:54:10+00:00` | `2026-04-12 19:54:10 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T00:54:10+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T00:54:10+00:00` | `2026-04-12 19:54:10 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T01:59:39+00:00` | `2026-04-12 20:59:39 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T01:59:56+00:00` | `2026-04-12 20:59:56 (Lima)` |
| Última firma humana | `2026-04-13T02:00:31+00:00` | `2026-04-12 21:00:31 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.10 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 19:54:10 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 20:59:56 (Lima), es decir **1.10 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T00:54:08+00:00` | `2026-04-12 19:54:08 (Lima)` | -0.00h |
| 1 | QUIROGA GIRON maria De Jesus FIR 09464589 sw b6683681af85bcbd1daeb66b8e1b56dab8808aab | 09464589 | `2026-04-13T01:59:56+00:00` | `2026-04-12 20:59:56 (Lima)` | +1.10h |
| 2 | RAMOS AGUILAR lucy Liliam FIR 70864950 sw eacf0461959fe29a2912ee64246fe8726e73eb44 | 70864950 | `2026-04-13T02:00:14+00:00` | `2026-04-12 21:00:14 (Lima)` | +1.10h |
| 3 | RIOS MELGAREJO elian Samir FIR 73195592 sw 1b96e633caee1ecebfccc43aae4b35bb48ba3518 | 73195592 | `2026-04-13T02:00:31+00:00` | `2026-04-12 21:00:31 (Lima)` | +1.11h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036052**
2. Descargar el PDF del acta
3. Verificar SHA-256: `af1921d87f0a20e2835dd5eb88fb2a8ea305c7140f98276c12b4176a1d91b93f`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
