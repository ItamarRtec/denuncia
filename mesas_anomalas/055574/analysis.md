# Mesa 055574 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:10.035116+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 6045 DOLORES CAVERO DE GRAU (código 7437)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 233
- Votos válidos: 209
- Participación: 77.926%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:41:36+00:00` | `2026-04-12 20:41:36 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:41:36+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:41:36+00:00` | `2026-04-12 20:41:36 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:39:42+00:00` | `2026-04-13 00:39:42 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:41:14+00:00` | `2026-04-13 00:41:14 (Lima)` |
| Última firma humana | `2026-04-13T05:41:52+00:00` | `2026-04-13 00:41:52 (Lima)` |

**Brecha primera firma humana vs publicación:** **+3.99 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:41:36 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:41:14 (Lima), es decir **3.99 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:41:33+00:00` | `2026-04-12 20:41:33 (Lima)` | -0.00h |
| 1 | QUISPE HERRERA sofia Fernanda FIR 71331902 sw 2bcf2922db4fa630e690d5a11a89fbb0bc812e62 | 71331902 | `2026-04-13T05:41:14+00:00` | `2026-04-13 00:41:14 (Lima)` | +3.99h |
| 2 | REYES NEYRA dilma Cynthia FIR 44250430 sw abfdfec15c1d141d3614dbcbbcfed9e8ec24463c | 44250430 | `2026-04-13T05:41:26+00:00` | `2026-04-13 00:41:26 (Lima)` | +4.00h |
| 3 | QUISPE CCOA jose Luis FIR 42722683 sw 7bbe03baa3edec35c3421e3f621c973015c734f4 | 42722683 | `2026-04-13T05:41:35+00:00` | `2026-04-13 00:41:35 (Lima)` | +4.00h |
| 4 | INCIO BERMUDEZ corina Esther FIR 08399368 sw edf117be60dcdac375b3aed2fd6b3e6dc2734fe2 | 08399368 | `2026-04-13T05:41:52+00:00` | `2026-04-13 00:41:52 (Lima)` | +4.00h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055574**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2e741583a88e6cdb777ed279ccf6874364c81650ecfe660f020ac9367120996d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
