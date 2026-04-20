# Mesa 052667 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:03.574246+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: VILLA MARÍA DEL TRIUNFO
- **Local de votación**: IE TUPAC AMARU (código 3275)
- **Ubigeo**: 140132

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 245
- Votos válidos: 213
- Participación: 81.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:37:31+00:00` | `2026-04-12 20:37:31 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:37:31+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:37:31+00:00` | `2026-04-12 20:37:31 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:50:37+00:00` | `2026-04-12 22:50:37 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:51:22+00:00` | `2026-04-12 22:51:22 (Lima)` |
| Última firma humana | `2026-04-13T03:51:53+00:00` | `2026-04-12 22:51:53 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.23 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:37:31 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:51:22 (Lima), es decir **2.23 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:37:29+00:00` | `2026-04-12 20:37:29 (Lima)` | -0.00h |
| 1 | MARTINEZ MEDRANO vladimir Joel FIR 42875899 sw 6c5cfb6c41df58579855146950d0674f70af98f5 | 42875899 | `2026-04-13T03:51:22+00:00` | `2026-04-12 22:51:22 (Lima)` | +2.23h |
| 2 | MAMANI CANGRE rocio Danicsa FIR 43985773 sw 8b0118d46bd86f32f51d8b5b0a8f636f535b8bc5 | 43985773 | `2026-04-13T03:51:38+00:00` | `2026-04-12 22:51:38 (Lima)` | +2.24h |
| 3 | MACHA MASLUCAN maricielo FIR 73239818 sw 53d9badff99631a8e7b0078f28fa11d4d37f4568 | 73239818 | `2026-04-13T03:51:53+00:00` | `2026-04-12 22:51:53 (Lima)` | +2.24h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **052667**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5b4a0274c3eb6d3cb159a4aa7b36e194351b50890fe344e20c918639bd1ba331`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
