# Mesa 082928 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:56.687832+00:00_

## Ubicación
- **Departamento**: CALLAO
- **Provincia**: CALLAO
- **Distrito**: LA PERLA
- **Local de votación**: IE PARROQUIAL SAN JOSE (código 4854)
- **Ubigeo**: 240105

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 279
- Votos válidos: 270
- Participación: 93.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:42:45+00:00` | `2026-04-12 21:42:45 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:42:45+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:42:45+00:00` | `2026-04-12 21:42:45 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:06:02+00:00` | `2026-04-13 09:06:02 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:06:13+00:00` | `2026-04-13 09:06:13 (Lima)` |
| Última firma humana | `2026-04-13T14:07:20+00:00` | `2026-04-13 09:07:20 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.39 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:42:45 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:06:13 (Lima), es decir **11.39 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:42:39+00:00` | `2026-04-12 21:42:39 (Lima)` | -0.00h |
| 1 | POLO MEDINA juana Margarita FIR 25598767 sw 1ce313e7d4a6d569f74fba99ae3972170868e3d2 | 25598767 | `2026-04-13T14:06:13+00:00` | `2026-04-13 09:06:13 (Lima)` | +11.39h |
| 2 | QUISPE QUENALLATA efrain Leoncio FIR 25741481 sw 23c23ea56c699d504506662b68552a68027098c6 | 25741481 | `2026-04-13T14:06:26+00:00` | `2026-04-13 09:06:26 (Lima)` | +11.39h |
| 3 | PORRAS SANCHEZ eduardo Raul FIR 08560445 sw 72a85a2994d54e47bba92d85f44d71cfc49527fc | 08560445 | `2026-04-13T14:06:39+00:00` | `2026-04-13 09:06:39 (Lima)` | +11.40h |
| 4 | RAMOS MORALES fernando Lucio FIR 76305362 sw 78c40cf52e2f8b84bf2d36b2fcac87365061110c | 76305362 | `2026-04-13T14:07:06+00:00` | `2026-04-13 09:07:06 (Lima)` | +11.41h |
| 5 | RESASCO SATALAYA sara Elke FIR 44088368 sw b51dde8ba23e89627ac62531f8acdfb817c87943 | 44088368 | `2026-04-13T14:07:20+00:00` | `2026-04-13 09:07:20 (Lima)` | +11.41h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **082928**
2. Descargar el PDF del acta
3. Verificar SHA-256: `48d229ad293b2992368aee175562ff0223342b443ec66de2523deeca3b1275d7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **5** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
