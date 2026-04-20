# Mesa 047922 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.603207+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN ISIDRO
- **Local de votación**: ESTACIONAMIENTO PETROPERU (código 54844)
- **Ubigeo**: 140124

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 184
- Votos válidos: 177
- Participación: 61.538%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:24:15+00:00` | `2026-04-12 21:24:15 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:24:15+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:24:15+00:00` | `2026-04-12 21:24:15 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:49:41+00:00` | `2026-04-13 07:49:41 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:14:55+00:00` | `2026-04-13 08:14:55 (Lima)` |
| Última firma humana | `2026-04-13T13:24:30+00:00` | `2026-04-13 08:24:30 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.84 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:24:15 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:14:55 (Lima), es decir **10.84 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:24:11+00:00` | `2026-04-12 21:24:11 (Lima)` | -0.00h |
| 1 | DIAZ MONTEOLIVO sonia FIR 09884422 sw 2852ecdf91ad53c1f228ebcc22bff9a7dd68291d | 09884422 | `2026-04-13T13:14:55+00:00` | `2026-04-13 08:14:55 (Lima)` | +10.84h |
| 2 | DELGADO LOAYZA rafaela Del Carmen FIR 26717953 sw 653b3662134a86a3a68362875e29fae24bf33f64 | 26717953 | `2026-04-13T13:17:59+00:00` | `2026-04-13 08:17:59 (Lima)` | +10.90h |
| 3 | DELGADO SANTOLALLA patricia Josefina FIR 07773193 sw 247556ab58dcfa4f1d5eab7487a70ab92f393896 | 07773193 | `2026-04-13T13:24:30+00:00` | `2026-04-13 08:24:30 (Lima)` | +11.00h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **047922**
2. Descargar el PDF del acta
3. Verificar SHA-256: `e67ea6b417d5479f7630fe4c6a5ddcca4e246750d9cb81c972ddd9f5958ac07d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
