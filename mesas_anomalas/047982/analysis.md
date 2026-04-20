# Mesa 047982 — evidencia de firma post-publicación

_Capturado: 2026-04-19T22:54:14.971784+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: BARRANCO
- **Local de votación**: IE 7049 CAP FAP JOSE ABELARDO QUIÑONES GONZALES (código 3079)
- **Ubigeo**: 140125

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 300
- Votos emitidos: 240
- Votos válidos: 222
- Participación: 80.0%

## Línea de tiempo según ONPE (campo `lineaTiempo` de su API)

| Estado | Descripción | UTC | Hora Perú (UTC-5) |
|---|---|---|---|
| `C` | Contabilizada | `2026-04-13T01:33:56+00:00` | `2026-04-12 20:33:56 (Lima)` |

**Momento de publicación pública (estado C — Contabilizada):** `2026-04-13T01:33:56+00:00`

## La inconsistencia

| Evento | UTC | Hora Perú |
|---|---|---|
| ONPE marcó la mesa Contabilizada (`fechaRegistro`) | `2026-04-13T01:33:56+00:00` | `2026-04-12 20:33:56 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T13:13:14+00:00` | `2026-04-13 08:13:14 (Lima)` |
| Primera firma humana (DNI peruano) | `2026-04-13T13:14:11+00:00` | `2026-04-13 08:14:11 (Lima)` |
| Última firma humana | `2026-04-13T13:14:35+00:00` | `2026-04-13 08:14:35 (Lima)` |

**Brecha primera firma humana vs publicación:** **+11.67 horas** (DESPUÉS de la publicación).

En palabras simples: ONPE marcó esta mesa como **Contabilizada y publicó su resultado** el 2026-04-12 20:33:56 (Lima). Los miembros de mesa firmaron digitalmente el acta el 2026-04-13 08:14:11 (Lima), es decir **11.67 horas DESPUÉS** de que el resultado ya estaba publicado.

## Firmas digitales del PDF (cripto-verificables)

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs publicación |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE, no documentado en cartilla) | — | `2026-04-13T01:33:54+00:00` | `2026-04-12 20:33:54 (Lima)` | -0.00h |
| 1 | ATARAMA ROMERO dany Francisco FIR 40172286 sw 9aaddf0363cfa448aff42f6a0da427cbe622f5b4 | 40172286 | `2026-04-13T13:14:11+00:00` | `2026-04-13 08:14:11 (Lima)` | +11.67h |
| 2 | CAPPILLO SALAZAR marco Antonio Carlos FIR 10550253 sw ad5d075d26f079235d011bd4d0436d2786682a19 | 10550253 | `2026-04-13T13:14:22+00:00` | `2026-04-13 08:14:22 (Lima)` | +11.67h |
| 3 | CAMPOS PONCE willy FIR 10549827 sw 22bbcb0e85cd52fe9c4579d4898b7921c8805bdf | 10549827 | `2026-04-13T13:14:35+00:00` | `2026-04-13 08:14:35 (Lima)` | +11.68h |

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar mesa **047982**
2. Descargar el PDF del acta
3. Verificar SHA-256: `9fc0caf64e08b886dfcbe588e44cb320031ab064b49c36cb98c2f4d448dcfc28`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las firmas: vas a ver **3** firmas humanas con DNI + firma del Agente Automatizado STAE
7. Cada firma humana muestra timestamp (`/M`) — comparar con el campo `fechaRegistro` del estado `C` (Contabilizada) en `lineaTiempo` de la API
