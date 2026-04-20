# Mesa 046604 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.669610+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUENTE PIEDRA
- **Local de votación**: IEP DIVINO CORAZÓN DE JESUS (código 7655)
- **Ubigeo**: 140119

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 244
- Votos válidos: 205
- Participación: 81.333%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:31:42+00:00` | `2026-04-12 20:31:42 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:31:42+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:31:42+00:00` | `2026-04-12 20:31:42 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:12:11+00:00` | `2026-04-12 22:12:11 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T03:12:42+00:00` | `2026-04-12 22:12:42 (Lima)` |
| Última firma humana | `2026-04-13T03:13:15+00:00` | `2026-04-12 22:13:15 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.68 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:31:42 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 22:12:42 (Lima), es decir **1.68 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:31:39+00:00` | `2026-04-12 20:31:39 (Lima)` | -0.00h |
| 1 | QUISPE CUY xiomara Maritza FIR 60762809 sw 5a3258a4bc907693fa3130c317c719e1666ae2b3 | 60762809 | `2026-04-13T03:12:42+00:00` | `2026-04-12 22:12:42 (Lima)` | +1.68h |
| 2 | ORTEGA BOYER ricardo Emanuel FIR 60977531 sw 3070835146cefe97839f8014daec0e4b9beee31f | 60977531 | `2026-04-13T03:12:58+00:00` | `2026-04-12 22:12:58 (Lima)` | +1.69h |
| 3 | PINEDO APARICIO fernando Jose FIR 60762777 sw cc2a2148c36fd28161e6fb82d9640c427c40254c | 60762777 | `2026-04-13T03:13:15+00:00` | `2026-04-12 22:13:15 (Lima)` | +1.69h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046604**
2. Descargar el PDF del acta
3. Verificar SHA-256: `bc4a0dfc27cc2b19817ec0ef63acb2ea129eac5dbf6b2c16a9546b4318d0d624`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
