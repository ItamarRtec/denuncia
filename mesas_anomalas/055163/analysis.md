# Mesa 055163 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:06.656976+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 7079 RAMIRO PRIALE PRIALE (código 3367)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 246
- Votos válidos: 218
- Participación: 82.274%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:58:29+00:00` | `2026-04-12 21:58:29 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:58:29+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:58:29+00:00` | `2026-04-12 21:58:29 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:28:36+00:00` | `2026-04-13 09:28:36 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:28:51+00:00` | `2026-04-13 09:28:51 (Lima)` |
| Última firma humana | `2026-04-13T14:29:19+00:00` | `2026-04-13 09:29:19 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.51 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:58:29 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:28:51 (Lima), es decir **11.51 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:58:26+00:00` | `2026-04-12 21:58:26 (Lima)` | -0.00h |
| 1 | AGUILAR HERRERA elizabeth FIR 42846502 sw a8bc6f14c024c3b792f13e33675cce6c98ebcbae | 42846502 | `2026-04-13T14:28:51+00:00` | `2026-04-13 09:28:51 (Lima)` | +11.51h |
| 2 | ALMEYDA VILLANUEVA bryan Alejandro FIR 72746535 sw 123cb56396162512a74a51b61ecb3c0021b6fb03 | 72746535 | `2026-04-13T14:29:03+00:00` | `2026-04-13 09:29:03 (Lima)` | +11.51h |
| 3 | ABANTO CABANILLAS edgard Javier FIR 19337710 sw 82418bee72a08d19d424aa167352a13f874490c2 | 19337710 | `2026-04-13T14:29:19+00:00` | `2026-04-13 09:29:19 (Lima)` | +11.51h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055163**
2. Descargar el PDF del acta
3. Verificar SHA-256: `34add8791e4497735035086975ed147c6b4a581838f775957a3d97cc3baf72d7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
