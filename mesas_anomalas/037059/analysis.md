# Mesa 037059 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:15.135294+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: ANCÓN
- **Local de votación**: IE CARLOS GUTIERREZ MERINO (código 2680)
- **Ubigeo**: 140102

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 236
- Votos válidos: 203
- Participación: 78.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T04:45:49+00:00` | `2026-04-12 23:45:49 (Lima)` |
| `C` | Contabilizada | `2026-04-13T03:59:00+00:00` | `2026-04-12 22:59:00 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T04:45:49+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T04:45:49+00:00` | `2026-04-12 23:45:49 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T06:08:06+00:00` | `2026-04-13 01:08:06 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T06:08:21+00:00` | `2026-04-13 01:08:21 (Lima)` |
| Última firma humana | `2026-04-13T06:08:53+00:00` | `2026-04-13 01:08:53 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.38 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 23:45:49 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 01:08:21 (Lima), es decir **1.38 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:58:57+00:00` | `2026-04-12 22:58:57 (Lima)` | -0.78h |
| 1 | VIVANCO CHIPANA julio Cesar FIR 10345981 sw 14c2ec5109eb47fa6a9a0e243265bfa18738e80d | 10345981 | `2026-04-13T06:08:21+00:00` | `2026-04-13 01:08:21 (Lima)` | +1.38h |
| 2 | YENQUE PIMENTEL paula Rosa FIR 06542235 sw a36a9bde26614402b7e30fd2a1fef2bbf39c9dba | 06542235 | `2026-04-13T06:08:39+00:00` | `2026-04-13 01:08:39 (Lima)` | +1.38h |
| 3 | VICTORIA BONILLA isabel Josefina FIR 20405441 sw 51a465187d9db37b7135f4bc2b5b9ed86df7a768 | 20405441 | `2026-04-13T06:08:53+00:00` | `2026-04-13 01:08:53 (Lima)` | +1.38h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **037059**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2926552e1e8d3fb0dc1c2ca9a351337b0e090ceb18572ec2a2e792b7b50a3515`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
