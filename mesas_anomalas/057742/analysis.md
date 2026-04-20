# Mesa 057742 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:16.592676+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE LURIGANCHO
- **Local de votación**: IEP BENJAMIN FRANKLIN (código 18499)
- **Ubigeo**: 140137

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 239
- Votos válidos: 218
- Participación: 79.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T04:12:45+00:00` | `2026-04-12 23:12:45 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T04:12:45+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T04:12:45+00:00` | `2026-04-12 23:12:45 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T11:55:43+00:00` | `2026-04-13 06:55:43 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T11:56:35+00:00` | `2026-04-13 06:56:35 (Lima)` |
| Última firma humana | `2026-04-13T11:56:59+00:00` | `2026-04-13 06:56:59 (Lima)` |

**Brecha primera firma humana vs publicación:** **+7.73 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 23:12:45 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 06:56:35 (Lima), es decir **7.73 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T04:12:42+00:00` | `2026-04-12 23:12:42 (Lima)` | -0.00h |
| 1 | GONZALEZ CASACHAGUA maricielo FIR 70726660 sw 694460e5353f127ad49c95863eaa4894018507ad | 70726660 | `2026-04-13T11:56:35+00:00` | `2026-04-13 06:56:35 (Lima)` | +7.73h |
| 2 | HORNA HUARCAYA leonardo FIR 48398698 sw 4d42dffd6ebcc24dea3c330f495f0c4a0dd510df | 48398698 | `2026-04-13T11:56:48+00:00` | `2026-04-13 06:56:48 (Lima)` | +7.73h |
| 3 | HUACHO CUEVA tracy Francis FIR 60773047 sw 5618ed232e009508a9e4367a97c6f677da871b8a | 60773047 | `2026-04-13T11:56:59+00:00` | `2026-04-13 06:56:59 (Lima)` | +7.74h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **057742**
2. Descargar el PDF del acta
3. Verificar SHA-256: `05767799127959cb6f7000c85a7392f457734bcdc337f69e9658bc60da2648e7`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
