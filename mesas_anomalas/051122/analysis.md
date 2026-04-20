# Mesa 051122 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:57.123912+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SANTIAGO DE SURCO
- **Local de votación**: IEP CORAZON INMACULADO (código 14139)
- **Ubigeo**: 140130

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 230
- Votos emitidos: 162
- Votos válidos: 147
- Participación: 70.435%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:08:49+00:00` | `2026-04-12 21:08:49 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:08:49+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:08:49+00:00` | `2026-04-12 21:08:49 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T07:23:10+00:00` | `2026-04-13 02:23:10 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T07:23:51+00:00` | `2026-04-13 02:23:51 (Lima)` |
| Última firma humana | `2026-04-13T07:25:58+00:00` | `2026-04-13 02:25:58 (Lima)` |

**Brecha primera firma humana vs publicación:** **+5.25 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:08:49 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 02:23:51 (Lima), es decir **5.25 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:08:47+00:00` | `2026-04-12 21:08:47 (Lima)` | -0.00h |
| 1 | ABAL GIRALDO olga FIR 08883863 sw 68b809140298a5b4361d832099c79014308afbb3 | 08883863 | `2026-04-13T07:23:51+00:00` | `2026-04-13 02:23:51 (Lima)` | +5.25h |
| 2 | CARRASCO SOLORZANO virginia Magali FIR 09985662 sw 2a6b2cf8eddbc1bf9d8562c2003e8aecac53dca9 | 09985662 | `2026-04-13T07:24:13+00:00` | `2026-04-13 02:24:13 (Lima)` | +5.26h |
| 3 | CASTILLO RODRIGUEZ darielita FIR 40416489 sw 3da87b3be348257676411c176a1a6b00c757d51f | 40416489 | `2026-04-13T07:24:33+00:00` | `2026-04-13 02:24:33 (Lima)` | +5.26h |
| 4 | ARONES CCAULLA carlos FIR 10552637 sw d491dd4c169ccd21442db6d0dce5e40903388b58 | 10552637 | `2026-04-13T07:25:17+00:00` | `2026-04-13 02:25:17 (Lima)` | +5.27h |
| 5 | COAGUILA CORNEJO gilmer Victor FIR 09347595 sw 57337f6581d992b3993735379e9c9f08d5bcdcc7 | 09347595 | `2026-04-13T07:25:58+00:00` | `2026-04-13 02:25:58 (Lima)` | +5.29h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051122**
2. Descargar el PDF del acta
3. Verificar SHA-256: `3992f9aaf9740938967916fe9a66184b59dedb21e0c8cb547bbba48b5ab6dd4a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
