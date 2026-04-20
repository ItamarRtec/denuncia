# Mesa 050601 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.177086+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IE 6047 JOSE MARIA ARGUEDAS (código 3199)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 242
- Votos válidos: 223
- Participación: 80.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:07:50+00:00` | `2026-04-12 20:07:50 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:07:50+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:07:50+00:00` | `2026-04-12 20:07:50 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:21:03+00:00` | `2026-04-12 22:21:03 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:21:30+00:00` | `2026-04-12 22:21:30 (Lima)` |
| Última firma humana | `2026-04-13T03:22:56+00:00` | `2026-04-12 22:22:56 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.23 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:07:50 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:21:30 (Lima), es decir **2.23 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:07:48+00:00` | `2026-04-12 20:07:48 (Lima)` | -0.00h |
| 1 | DELGADO AVILA miguel Antonio FIR 46545595 sw a01a93db66423fddb70a6571b93076a6e36e10d3 | 46545595 | `2026-04-13T03:21:30+00:00` | `2026-04-12 22:21:30 (Lima)` | +2.23h |
| 2 | COSSIO VEGA milagros FIR 09877687 sw a542ee1ba44240704126dd358a449690987b217f | 09877687 | `2026-04-13T03:21:48+00:00` | `2026-04-12 22:21:48 (Lima)` | +2.23h |
| 3 | CORDOVA MONTALVAN ronald Yvan FIR 42566031 sw 874b48f2614200a3b2ae2cc52db0f4d40d13dd45 | 42566031 | `2026-04-13T03:22:10+00:00` | `2026-04-12 22:22:10 (Lima)` | +2.24h |
| 4 | ESPIRITU BACA vilma Felomina FIR 10308823 sw ea710db460e2a345e526a74d91d22cf2cbfb72a3 | 10308823 | `2026-04-13T03:22:56+00:00` | `2026-04-12 22:22:56 (Lima)` | +2.25h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050601**
2. Descargar el PDF del acta
3. Verificar SHA-256: `d3445fed8eb8655195473f6207216c8dd37604e8d2885e3514645c7cd963618c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
