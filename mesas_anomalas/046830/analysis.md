# Mesa 046830 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.586693+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: PUENTE PIEDRA
- **Local de votación**: IEP JULIO RAMON RIBEYRO (código 13641)
- **Ubigeo**: 140119

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 269
- Votos válidos: 242
- Participación: 89.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:44:11+00:00` | `2026-04-12 21:44:11 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:44:11+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:44:11+00:00` | `2026-04-12 21:44:11 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:25:14+00:00` | `2026-04-13 00:25:14 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:26:05+00:00` | `2026-04-13 00:26:05 (Lima)` |
| Última firma humana | `2026-04-13T05:27:01+00:00` | `2026-04-13 00:27:01 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.70 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:44:11 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:26:05 (Lima), es decir **2.70 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:39:02+00:00` | `2026-04-12 21:39:02 (Lima)` | -0.09h |
| 1 | SOPLA CHIGNE jhon Eystein FIR 45654553 sw 41e9a70c563c0c68abc686e8e893603c72ea5db5 | 45654553 | `2026-04-13T05:26:05+00:00` | `2026-04-13 00:26:05 (Lima)` | +2.70h |
| 2 | SEBASTIAN HUATAY jennifer Lizeth FIR 77017176 sw 037c3c1fed72b454b7d6414d5790f1da3e64fe2f | 77017176 | `2026-04-13T05:26:43+00:00` | `2026-04-13 00:26:43 (Lima)` | +2.71h |
| 3 | SIFUENTES OLIVEROS nestor Ricardo FIR 20034941 sw 0ee6507fdc5e8460f20ed8f74c73b7c00eb2fd1e | 20034941 | `2026-04-13T05:27:01+00:00` | `2026-04-13 00:27:01 (Lima)` | +2.71h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **046830**
2. Descargar el PDF del acta
3. Verificar SHA-256: `d5ebaec1ac41bb521ce9ad5c741585c03e9445fbc9c420987576ba52b97ee17a`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
