# Mesa 039560 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:08.875179+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: CARABAYLLO
- **Local de votación**: IE 8188 FE Y ESPERANZA (código 5093)
- **Ubigeo**: 140105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 243
- Votos válidos: 221
- Participación: 81.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:43:22+00:00` | `2026-04-12 20:43:22 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:43:22+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:43:22+00:00` | `2026-04-12 20:43:22 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:47:18+00:00` | `2026-04-13 00:47:18 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:47:48+00:00` | `2026-04-13 00:47:48 (Lima)` |
| Última firma humana | `2026-04-13T05:50:43+00:00` | `2026-04-13 00:50:43 (Lima)` |

**Brecha primera firma humana vs publicación:** **+4.07 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:43:22 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:47:48 (Lima), es decir **4.07 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:43:20+00:00` | `2026-04-12 20:43:20 (Lima)` | -0.00h |
| 1 | HUAMAN HUGO iris FIR 40437025 sw 7d7ef96e30e1a4c1d82ddaa2f4272da544a673e5 | 40437025 | `2026-04-13T05:47:48+00:00` | `2026-04-13 00:47:48 (Lima)` | +4.07h |
| 2 | KOR  nathan Thomas FIR 46740013 sw 4bcea40d08cfca85092976097872d02d725d275e | 46740013 | `2026-04-13T05:48:06+00:00` | `2026-04-13 00:48:06 (Lima)` | +4.08h |
| 3 | LEYVA BARZOLA genoveva Regina FIR 45467095 sw 94887587b79c4022b225ff1ba53bf24d19139732 | 45467095 | `2026-04-13T05:48:23+00:00` | `2026-04-13 00:48:23 (Lima)` | +4.08h |
| 4 | FERNANDEZ CAMPOS julia Rumalda FIR 10207276 sw 546060d237f86c468c82d8bffb419611324a14ae | 10207276 | `2026-04-13T05:50:43+00:00` | `2026-04-13 00:50:43 (Lima)` | +4.12h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **039560**
2. Descargar el PDF del acta
3. Verificar SHA-256: `1b0e2fbb9042fd5e1789ea29b07f846fd1f5f33ac9d66b76d19db1ff56878245`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
