# Mesa 045177 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:17.606390+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: COLEGIO INMACULADO CORAZON (código 2991)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 216
- Votos válidos: 207
- Participación: 72.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T02:08:21+00:00` | `2026-04-12 21:08:21 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T02:08:21+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T02:08:21+00:00` | `2026-04-12 21:08:21 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T11:22:57+00:00` | `2026-04-13 06:22:57 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T11:23:48+00:00` | `2026-04-13 06:23:48 (Lima)` |
| Última firma humana | `2026-04-13T11:24:25+00:00` | `2026-04-13 06:24:25 (Lima)` |

**Brecha primera firma humana vs publicación:** **+9.26 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 21:08:21 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 06:23:48 (Lima), es decir **9.26 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T02:08:19+00:00` | `2026-04-12 21:08:19 (Lima)` | -0.00h |
| 1 | FLORES MORENO jackeline Rossin FIR 44360471 sw 354bbd9ac8faa49f049770ba1c181b4af21a32f0 | 44360471 | `2026-04-13T11:23:48+00:00` | `2026-04-13 06:23:48 (Lima)` | +9.26h |
| 2 | FLORES CASTRO nicolas Elias FIR 76333926 sw ba642f000786dcd9991ec0d76003748decab177c | 76333926 | `2026-04-13T11:24:07+00:00` | `2026-04-13 06:24:07 (Lima)` | +9.26h |
| 3 | FLORES MAYER vanessa Yovanna FIR 40275580 sw e45b09b1858934b964f035b31c800a7109a5064c | 40275580 | `2026-04-13T11:24:25+00:00` | `2026-04-13 06:24:25 (Lima)` | +9.27h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045177**
2. Descargar el PDF del acta
3. Verificar SHA-256: `105d41582a8279c09d75cd29a864e8b802e514bc0a66536539b952945de98434`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
