# Mesa 051909 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:13.976232+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SURQUILLO
- **Local de votación**: ESTADIO MUNICIPAL CARLOS A. MOSCOSO 2 (código 40995)
- **Ubigeo**: 140131

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 200
- Votos válidos: 191
- Participación: 66.89%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:50:00+00:00` | `2026-04-12 21:50:00 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:50:00+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:50:00+00:00` | `2026-04-12 21:50:00 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T14:06:54+00:00` | `2026-04-13 09:06:54 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T14:07:35+00:00` | `2026-04-13 09:07:35 (Lima)` |
| Última firma humana | `2026-04-13T14:09:02+00:00` | `2026-04-13 09:09:02 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.29 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:50:00 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 09:07:35 (Lima), es decir **11.29 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:44:12+00:00` | `2026-04-12 21:44:12 (Lima)` | -0.10h |
| 1 | MUNAYCO PEREZ mariela Aurelia FIR 08885295 sw f9eaa9c4a2162a9c3de3a65c91a5ee3b4211938b | 08885295 | `2026-04-13T14:07:35+00:00` | `2026-04-13 09:07:35 (Lima)` | +11.29h |
| 2 | NAMUCHE REYES walter Jorge FIR 08817866 sw a26e8070ed4cfac73ef7e7b1d2825fabbbac58b2 | 08817866 | `2026-04-13T14:07:51+00:00` | `2026-04-13 09:07:51 (Lima)` | +11.30h |
| 3 | DELGADO HERNANDEZ DE SARMIENTO matilde FIR 42242659 sw ef06da4b4ec4a905f20405789245c3dcde4a0dfe | 42242659 | `2026-04-13T14:09:02+00:00` | `2026-04-13 09:09:02 (Lima)` | +11.32h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **051909**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8bbe3c2a2765fe544cf49d2349173550af52d1991d5a8daa029c894dc217ad47`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
