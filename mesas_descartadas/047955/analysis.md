# Mesa 047955 — evidencia Nivel 2 (digital)

_Capturado: 2026-04-19T22:54:14.368745+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN ISIDRO
- **Local de votación**: ESTACIONAMIENTO PETROPERU (código 54844)
- **Ubigeo**: 140124

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 206
- Votos válidos: 200
- Participación: 68.896%

## Los dos timestamps clave

| Evento | UTC | Hora Perú (UTC-5) |
|---|---|---|
| ONPE registró el voto (`daudFechaCreacion`) | `2026-04-13T04:33:04.044000+00:00` | `2026-04-12 23:33:04 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T05:36:30+00:00` | `2026-04-13 00:36:30 (Lima)` |

**Brecha:** PDF creado **1.06 horas DESPUÉS del upload** (0.04 días).

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar la mesa **047955**
2. Descargar el PDF del acta
3. Verificar SHA-256: `af24d5f011f07c5c68eba2be9c19ce37a04c8388763bb1a89d48cf02ad2cbcdd`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las 5 firmas: **4** humanas + **1** "AGENTE AUTOMATIZADO STAE"

## Firmas extraídas del PDF

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs upload |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE) | — | `2026-04-13T03:05:22+00:00` | `2026-04-12 22:05:22 (Lima)` | -1.46h |
| 1 | TAMAYO LECCA hernan Reynaldo FIR 07928984 sw 1b6de0467314f4a39708985045b0c7052c6a84ac | 07928984 | `2026-04-13T05:36:48+00:00` | `2026-04-13 00:36:48 (Lima)` | +1.06h |
| 2 | TARAZONA PECHE roberto Christian FIR 41354552 sw b8b669e34761ec8e253446a9b4df36485e3777f3 | 41354552 | `2026-04-13T05:37:06+00:00` | `2026-04-13 00:37:06 (Lima)` | +1.07h |
| 3 | TELLO PORTILLA eduardo Nicolas FIR 10221562 sw ee24761b7b26537af73d8156ca3fc77590fa4f10 | 10221562 | `2026-04-13T05:37:22+00:00` | `2026-04-13 00:37:22 (Lima)` | +1.07h |
| 4 | TALAVERA ZEGARRA DE OTERO ana Olga Artemia FIR 06460015 sw 04221bb150d57a90a8145fbd7aae911b12327630 | 06460015 | `2026-04-13T05:37:41+00:00` | `2026-04-13 00:37:41 (Lima)` | +1.08h |

- **¿Humanos firmaron post-upload?** **SÍ**
- **Primer humano firmó**: +1.06h vs upload
- **Último humano firmó**: +1.08h vs upload
