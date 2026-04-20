# Mesa 055295 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:02.802973+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE DE ACCION CONJUNTA PADRE ILUMINATO (código 3375)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 240
- Votos válidos: 212
- Participación: 80.268%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:05:21+00:00` | `2026-04-12 21:05:21 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:05:21+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:05:21+00:00` | `2026-04-12 21:05:21 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T06:01:38+00:00` | `2026-04-13 01:01:38 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:01:55+00:00` | `2026-04-13 01:01:55 (Lima)` |
| Última firma humana | `2026-04-13T06:03:51+00:00` | `2026-04-13 01:03:51 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.94 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:05:21 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:01:55 (Lima), es decir **3.94 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:05:18+00:00` | `2026-04-12 21:05:18 (Lima)` | -0.00h |
| 1 | LOPEZ CARRASCO celia FIR 43152614 sw c19bef110c4b1ad22e18c6ffd722f9e9cfa492fb | 43152614 | `2026-04-13T06:01:55+00:00` | `2026-04-13 01:01:55 (Lima)` | +3.94h |
| 2 | LOPEZ LINO pedro Luis FIR 09589071 sw db6500b3ff77143f68ef280c54212bbcd7c75898 | 09589071 | `2026-04-13T06:02:06+00:00` | `2026-04-13 01:02:06 (Lima)` | +3.95h |
| 3 | LEGUIA MAITAN alejandro FIR 31182149 sw 16602637ea8e638d7c70c52a9e0a25a884ef79d5 | 31182149 | `2026-04-13T06:02:17+00:00` | `2026-04-13 01:02:17 (Lima)` | +3.95h |
| 4 | NOVELLA DUCOS manuel FIR 07460575 sw b651a5e13b89276aec1075a0f78d2fd68a6aedf4 | 07460575 | `2026-04-13T06:02:59+00:00` | `2026-04-13 01:02:59 (Lima)` | +3.96h |
| 5 | MIRANDA HUAMAN rafael FIR 10567928 sw 84e379400837b20fcfe010f5d998342b53c2802e | 10567928 | `2026-04-13T06:03:51+00:00` | `2026-04-13 01:03:51 (Lima)` | +3.98h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055295**
2. Descargar el PDF del acta
3. Verificar SHA-256: `05b24a8ee83699b6ead0a29dbadfc5b83243b8f224111d198c45552b55b80bf6`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
