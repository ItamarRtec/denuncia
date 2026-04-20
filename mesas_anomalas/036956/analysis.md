# Mesa 036956 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:01.401641+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: LIMA
- **Local de votación**: IEP INNOVA SCHOOLS CERCADO (código 54800)
- **Ubigeo**: 140101

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 224
- Votos válidos: 198
- Participación: 74.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:02:35+00:00` | `2026-04-12 20:02:35 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:02:35+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:02:35+00:00` | `2026-04-12 20:02:35 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T01:46:45+00:00` | `2026-04-12 20:46:45 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T01:47:03+00:00` | `2026-04-12 20:47:03 (Lima)` |
| Última firma humana | `2026-04-13T01:47:27+00:00` | `2026-04-12 20:47:27 (Lima)` |

**Brecha primera firma humana vs publicación:** **+0.74 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:02:35 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 20:47:03 (Lima), es decir **0.74 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:02:33+00:00` | `2026-04-12 20:02:33 (Lima)` | -0.00h |
| 1 | MELENDEZ PEREZ areli FIR 08179143 sw 75c8ae640fab132e93d6be29fe0e01767ee89d4d | 08179143 | `2026-04-13T01:47:03+00:00` | `2026-04-12 20:47:03 (Lima)` | +0.74h |
| 2 | MARTINEZ ZURITA jesus Antolin FIR 40209935 sw 41ffc6066958a728ed0967cdcaa642865de467ab | 40209935 | `2026-04-13T01:47:14+00:00` | `2026-04-12 20:47:14 (Lima)` | +0.74h |
| 3 | MENDOZA SOTELO mario Enrique FIR 09920419 sw dea97ff21164579564cc4eb7043413e242646f78 | 09920419 | `2026-04-13T01:47:27+00:00` | `2026-04-12 20:47:27 (Lima)` | +0.75h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **036956**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8ee2669993eec756e441ca022ca5f3c557748a0f52ca28b18e7a3cf5cbe9ac0c`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
