# Mesa 045158 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:53:58.933447+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: MIRAFLORES
- **Local de votación**: IE FEDERICO VILLARREAL (código 2989)
- **Ubigeo**: 140115

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 203
- Votos válidos: 196
- Participación: 67.667%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:41:39+00:00` | `2026-04-12 20:41:39 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:41:39+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:41:39+00:00` | `2026-04-12 20:41:39 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T12:43:14+00:00` | `2026-04-13 07:43:14 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T12:43:31+00:00` | `2026-04-13 07:43:31 (Lima)` |
| Última firma humana | `2026-04-13T12:44:48+00:00` | `2026-04-13 07:44:48 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.03 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:41:39 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 07:43:31 (Lima), es decir **11.03 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:41:37+00:00` | `2026-04-12 20:41:37 (Lima)` | -0.00h |
| 1 | MONAR MIGUEL DE PRIEGO camille Antoine FIR 72389975 sw c60d431e29e5b69a7fbf858f2a40d00e56675035 | 72389975 | `2026-04-13T12:43:31+00:00` | `2026-04-13 07:43:31 (Lima)` | +11.03h |
| 2 | MEHNERT SALAZAR claus Dieter FIR 10806048 sw 9effd8ea11b70b08f59195f74e56cab3c9d82d5f | 10806048 | `2026-04-13T12:43:45+00:00` | `2026-04-13 07:43:45 (Lima)` | +11.04h |
| 3 | MAYURI PIZARRO carlos Armando FIR 07860967 sw 97151df0484000d7cdee7a5f9853b99fb8c298ec | 07860967 | `2026-04-13T12:43:57+00:00` | `2026-04-13 07:43:57 (Lima)` | +11.04h |
| 4 | QUISPE CALDERON adolfo Romulo FIR 06218630 sw 1a9db1407d143b0df4a93851fbad07a8159006f8 | 06218630 | `2026-04-13T12:44:48+00:00` | `2026-04-13 07:44:48 (Lima)` | +11.05h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **045158**
2. Descargar el PDF del acta
3. Verificar SHA-256: `271d5f5743bb130180c775a37402a884dd162fcadba281789b4fa387cb171414`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **4** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
