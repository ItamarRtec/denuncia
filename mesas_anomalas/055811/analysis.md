# Mesa 055811 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:00.271510+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IEP SANTA URSULA (código 51182)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 237
- Votos válidos: 204
- Participación: 79.264%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:48:40+00:00` | `2026-04-12 20:48:40 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:48:40+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:48:40+00:00` | `2026-04-12 20:48:40 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:42:58+00:00` | `2026-04-12 22:42:58 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:47:16+00:00` | `2026-04-12 22:47:16 (Lima)` |
| Última firma humana | `2026-04-13T03:47:48+00:00` | `2026-04-12 22:47:48 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.98 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:48:40 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:47:16 (Lima), es decir **1.98 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:48:37+00:00` | `2026-04-12 20:48:37 (Lima)` | -0.00h |
| 1 | CHUQUIMANI ZEVALLOS antonio Manuel FIR 44986262 sw 7b8bbe11fac853ea9b67ae3d210a3636da941990 | 44986262 | `2026-04-13T03:47:16+00:00` | `2026-04-12 22:47:16 (Lima)` | +1.98h |
| 2 | CHARA CHOQUE juan Agripino FIR 09591541 sw a67c7ab399d28f4a7658596b082a420fc42c3691 | 09591541 | `2026-04-13T03:47:31+00:00` | `2026-04-12 22:47:31 (Lima)` | +1.98h |
| 3 | CHAVEZ CORAQUILLO lesly Sandy FIR 41795899 sw 37d572b4eb875be02c9d05e152e40f91644609db | 41795899 | `2026-04-13T03:47:48+00:00` | `2026-04-12 22:47:48 (Lima)` | +1.99h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055811**
2. Descargar el PDF del acta
3. Verificar SHA-256: `338ff2a8d68134208d850017c411e934ac6818a7591bcb5612f7bbbe5e213019`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
