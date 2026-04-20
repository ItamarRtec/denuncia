# Mesa 039254 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.263926+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CARABAYLLO
- **Local de votación**: IE 2080 ANDRES BELLO (código 2767)
- **Ubigeo**: 140105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 272
- Votos válidos: 240
- Participación: 90.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:28:19+00:00` | `2026-04-12 21:28:19 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:28:19+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:28:19+00:00` | `2026-04-12 21:28:19 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:15:39+00:00` | `2026-04-13 09:15:39 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:16:28+00:00` | `2026-04-13 09:16:28 (Lima)` |
| Última firma humana | `2026-04-13T14:17:00+00:00` | `2026-04-13 09:17:00 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.80 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:28:19 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:16:28 (Lima), es decir **11.80 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:28:04+00:00` | `2026-04-12 21:28:04 (Lima)` | -0.00h |
| 1 | OLLAGUE PAJUELO juan Francisco FIR 09545608 sw e4b8141d276bdea032e02b499f2a1d0f35bfdccc | 09545608 | `2026-04-13T14:16:28+00:00` | `2026-04-13 09:16:28 (Lima)` | +11.80h |
| 2 | MARCELO MALLQUI marco Antonio FIR 10880148 sw c5d8c1692d84eaa694ec8d47953a0c5b66890874 | 10880148 | `2026-04-13T14:16:45+00:00` | `2026-04-13 09:16:45 (Lima)` | +11.81h |
| 3 | NECIOSUP CHUMBES susana Elvira FIR 45977457 sw b81b5b1a620ed8ba2716d5d837da1d7dfb3c8c5d | 45977457 | `2026-04-13T14:17:00+00:00` | `2026-04-13 09:17:00 (Lima)` | +11.81h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **039254**
2. Descargar el PDF del acta
3. Verificar SHA-256: `34fe08d97de9570392022b677c912fe8a77f239e981ff958aaa59cfae1a39f7c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
