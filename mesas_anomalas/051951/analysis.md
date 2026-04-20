# Mesa 051951 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:12.438266+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: IEP INICIAL LUZ Y VIDA (código 50555)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 258
- Votos válidos: 246
- Participación: 86.288%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T03:08:09+00:00` | `2026-04-12 22:08:09 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:08:09+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:08:09+00:00` | `2026-04-12 22:08:09 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:11:41+00:00` | `2026-04-13 08:11:41 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:12:38+00:00` | `2026-04-13 08:12:38 (Lima)` |
| Última firma humana | `2026-04-13T13:13:46+00:00` | `2026-04-13 08:13:46 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.07 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:08:09 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:12:38 (Lima), es decir **10.07 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:08:07+00:00` | `2026-04-12 22:08:07 (Lima)` | -0.00h |
| 1 | MARTINEZ CERON adriana FIR 49090579 sw 205d16de26450b0764e4ed9bdbbac93973f77fee | 49090579 | `2026-04-13T13:12:38+00:00` | `2026-04-13 08:12:38 (Lima)` | +10.07h |
| 2 | JIBAJA VIGO carlos Esteban FIR 71150198 sw 6f53e95c390df15d3893b792f679d718364d24ca | 71150198 | `2026-04-13T13:12:59+00:00` | `2026-04-13 08:12:59 (Lima)` | +10.08h |
| 3 | GALLARDO NORDMAN karen Alicia Graciela FIR 43756036 sw fefb61bfe0bc588982cb6bd3106c67bfa7c753e9 | 43756036 | `2026-04-13T13:13:46+00:00` | `2026-04-13 08:13:46 (Lima)` | +10.09h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051951**
2. Descargar el PDF del acta
3. Verificar SHA-256: `4212501692f7a933c81129cc0d16259f8d5b1db1173762980ac4f1d4ff1f8d86`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
