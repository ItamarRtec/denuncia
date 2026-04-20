# Mesa 055444 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.193914+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IEP MANUEL ANTONIO RAMIREZ BARINAGA (código 3382)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 228
- Votos válidos: 199
- Participación: 76.254%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:54:15+00:00` | `2026-04-12 21:54:15 (Lima)` |
| `C` | Contabilizada | `2026-04-13T02:51:02+00:00` | `2026-04-12 21:51:02 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:54:15+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:54:15+00:00` | `2026-04-12 21:54:15 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:57:53+00:00` | `2026-04-13 07:57:53 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:59:55+00:00` | `2026-04-13 07:59:55 (Lima)` |
| Última firma humana | `2026-04-13T13:00:06+00:00` | `2026-04-13 08:00:06 (Lima)` |

**Brecha primera firma humana vs publicación:** **+10.09 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:54:15 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:59:55 (Lima), es decir **10.09 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:45:39+00:00` | `2026-04-12 21:45:39 (Lima)` | -0.14h |
| 1 | FERNANDEZ GARAYAR arleny Del Rocio FIR 10643069 sw 15ddb345a04168879f6bd7dae2e054d9daed5116 | 10643069 | `2026-04-13T12:59:55+00:00` | `2026-04-13 07:59:55 (Lima)` | +10.09h |
| 2 | FERNANDEZ LAVA vilma Rosa FIR 15428391 sw e49a49ca2a8509c08e79e2ceaf7806ade79faf61 | 15428391 | `2026-04-13T13:00:06+00:00` | `2026-04-13 08:00:06 (Lima)` | +10.10h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **055444**
2. Descargar el PDF del acta
3. Verificar SHA-256: `2720e8e74cceaa0496f787542722815c2df77f26ab316100da48e3e0d746aa0e`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **2** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
