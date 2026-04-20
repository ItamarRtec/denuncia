# Mesa 040113 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.351385+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IE 2077 SAN MARTIN DE PORRES (código 2799)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 253
- Votos válidos: 216
- Participación: 84.615%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T04:33:58+00:00` | `2026-04-12 23:33:58 (Lima)` |
| `C` | Contabilizada | `2026-04-13T01:32:00+00:00` | `2026-04-12 20:32:00 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T04:33:58+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T04:33:58+00:00` | `2026-04-12 23:33:58 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:12:20+00:00` | `2026-04-13 08:12:20 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:13:06+00:00` | `2026-04-13 08:13:06 (Lima)` |
| Última firma humana | `2026-04-13T13:13:31+00:00` | `2026-04-13 08:13:31 (Lima)` |

**Brecha primera firma humana vs publicación:** **+8.65 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 23:33:58 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:13:06 (Lima), es decir **8.65 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:31:58+00:00` | `2026-04-12 20:31:58 (Lima)` | -3.03h |
| 1 | BAYONA VILCHEZ cristina Olivia FIR 80521454 sw 07a891abfdd92573a36f8cc9d12a6c05f2e2ae47 | 80521454 | `2026-04-13T13:13:06+00:00` | `2026-04-13 08:13:06 (Lima)` | +8.65h |
| 2 | BRAVO CASTREJON dimicia Luzmila FIR 09476384 sw e2b9267ff7b2f2392387f8fa89324983ceb03164 | 09476384 | `2026-04-13T13:13:31+00:00` | `2026-04-13 08:13:31 (Lima)` | +8.66h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **040113**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3f3bc1dac28c13a54bbe06c0a604acf2a1634129a5d5de73149ab3f2d2c68459`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
