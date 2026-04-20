# Mesa 038834 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.383387+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: BREÑA
- **Local de votación**: IE 0004 MARIANO MELGAR PRIMARIA (código 2744)
- **Ubigeo**: 140104

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 230
- Votos emitidos: 173
- Votos válidos: 159
- Participación: 75.217%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:01:44+00:00` | `2026-04-12 20:01:44 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:01:44+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:01:44+00:00` | `2026-04-12 20:01:44 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:43:29+00:00` | `2026-04-12 21:43:29 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T02:43:58+00:00` | `2026-04-12 21:43:58 (Lima)` |
| Última firma humana | `2026-04-13T02:44:33+00:00` | `2026-04-12 21:44:33 (Lima)` |

**Brecha primera firma humana vs publicación:** **+1.70 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:01:44 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-12 21:43:58 (Lima), es decir **1.70 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:01:42+00:00` | `2026-04-12 20:01:42 (Lima)` | -0.00h |
| 1 | ALVARADO GOICOCHEA cynthia Carol FIR 45826278 sw f2f3254f94f71c4e44c4d9e542b25b2333404f28 | 45826278 | `2026-04-13T02:43:58+00:00` | `2026-04-12 21:43:58 (Lima)` | +1.70h |
| 2 | AMACHI CARAZAS gloria FIR 40388134 sw d48a87578cf3db4dc21ffbd3867ad0f6cf1b7ca7 | 40388134 | `2026-04-13T02:44:15+00:00` | `2026-04-12 21:44:15 (Lima)` | +1.71h |
| 3 | AGUIRRE PABLO katia Yovana FIR 41066224 sw 63b91129e4e42a86b6cf066a9f2c47f7b9bd563f | 41066224 | `2026-04-13T02:44:33+00:00` | `2026-04-12 21:44:33 (Lima)` | +1.71h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **038834**
2. Descargar el PDF del acta
3. Verificar SHA-256: `6b0607f1439be1b018314847544c075a99a2a012db1f1d174b59c982025eb0f2`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
