# Mesa 050157 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:59.860640+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN MIGUEL
- **Local de votación**: IEP INNOVA SCHOOLS - SEDE SAN MIGUEL 2 (código 14096)
- **Ubigeo**: 140127

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 239
- Votos válidos: 220
- Participación: 79.933%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:42:13+00:00` | `2026-04-12 20:42:13 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:42:13+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:42:13+00:00` | `2026-04-12 20:42:13 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:11:17+00:00` | `2026-04-12 22:11:17 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:11:35+00:00` | `2026-04-12 22:11:35 (Lima)` |
| Última firma humana | `2026-04-13T03:12:11+00:00` | `2026-04-12 22:12:11 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.49 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:42:13 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:11:35 (Lima), es decir **1.49 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:42:11+00:00` | `2026-04-12 20:42:11 (Lima)` | -0.00h |
| 1 | ZARATE CANEPA andrea Belen FIR 80992760 sw 389ce418375fa16be735b4ce12d35fd4786224ca | 80992760 | `2026-04-13T03:11:35+00:00` | `2026-04-12 22:11:35 (Lima)` | +1.49h |
| 2 | TORRES GRANDEZ jose Eutimio FIR 09278042 sw 2e69f1932e9d950effc8088bfc6ccb473598df68 | 09278042 | `2026-04-13T03:11:58+00:00` | `2026-04-12 22:11:58 (Lima)` | +1.50h |
| 3 | VIVES HERENCIA jean Pierre FIR 76478184 sw 9cf5117c75c2d072a349bfb2e631da24ed4d874e | 76478184 | `2026-04-13T03:12:11+00:00` | `2026-04-12 22:12:11 (Lima)` | +1.50h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **050157**
2. Descargar el PDF del acta
3. Verificar SHA-256: `16640336f44a65e1d6f61a332db5d02ee47d92408050793d146114ab920b5454`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
