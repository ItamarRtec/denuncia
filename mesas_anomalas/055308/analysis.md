# Mesa 055308 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.034343+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE FE Y ALEGRIA 3 (código 3376)
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
| `C` | Contabilizada | `2026-04-13T03:28:14+00:00` | `2026-04-12 22:28:14 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T03:28:14+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T03:28:14+00:00` | `2026-04-12 22:28:14 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:53:19+00:00` | `2026-04-13 00:53:19 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T05:53:37+00:00` | `2026-04-13 00:53:37 (Lima)` |
| Última firma humana | `2026-04-13T05:54:53+00:00` | `2026-04-13 00:54:53 (Lima)` |

**Brecha primera firma humana vs publicación:** **+2.42 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 22:28:14 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 00:53:37 (Lima), es decir **2.42 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T03:28:12+00:00` | `2026-04-12 22:28:12 (Lima)` | -0.00h |
| 1 | AGUILAR BARRENECHEA hibeth Yovana FIR 09573717 sw 4d42830fdde8c106a3bb41ac6a32a237a0f8a028 | 09573717 | `2026-04-13T05:53:37+00:00` | `2026-04-13 00:53:37 (Lima)` | +2.42h |
| 2 | ALEJO GALLEGOS carmen Rosa FIR 09410542 sw 4f17837130e6b37c3ca022056f3355003f27b7e2 | 09410542 | `2026-04-13T05:53:51+00:00` | `2026-04-13 00:53:51 (Lima)` | +2.43h |
| 3 | AGUIRRE CARMONA darwin FIR 45267895 sw 63d7a09bd068d8a9ea4c4576b5d645858a784601 | 45267895 | `2026-04-13T05:54:01+00:00` | `2026-04-13 00:54:01 (Lima)` | +2.43h |
| 4 | HUAMANI FLORES amilcar FIR 10034665 sw d4e2760994939a4301ac0a2bd51cd5353dd0fd53 | 10034665 | `2026-04-13T05:54:53+00:00` | `2026-04-13 00:54:53 (Lima)` | +2.44h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055308**
2. Descargar el PDF del acta
3. Verificar SHA-256: `5ef03acfd33058c8018de27e560b4e96c1d5b69f476d47da37ae0a0d21643107`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
