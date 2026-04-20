# Mesa 041246 — evidencia Nivel 2 (digital)

_Capturado: 2026-04-19T22:54:00.107009+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IEP MI BUEN JESUS (código 50988)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 245
- Votos válidos: 194
- Participación: 81.94%

## Los dos timestamps clave

| Evento | UTC | Hora Perú (UTC-5) |
|---|---|---|
| ONPE registró el voto (`daudFechaCreacion`) | `2026-04-13T02:30:01.383000+00:00` | `2026-04-12 21:30:01 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:38:18+00:00` | `2026-04-12 22:38:18 (Lima)` |

**Brecha:** PDF creado **1.14 horas DESPUÉS del upload** (0.05 días).

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar la mesa **041246**
2. Descargar el PDF del acta
3. Verificar SHA-256: `73c1719b2e681b1dd095e604ec5f8a79a9b611eb1d03b7cdf8d2d382b7b439ac`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las 4 firmas: **3** humanas + **1** "AGENTE AUTOMATIZADO STAE"

## Firmas extraídas del PDF

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs upload |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE) | — | `2026-04-13T01:57:31+00:00` | `2026-04-12 20:57:31 (Lima)` | -0.54h |
| 1 | QUEZADA CUBA luis Alberto FIR 09473817 sw 0ef2d13bd507871d75fae2bb961f1e44f1c9b05b | 09473817 | `2026-04-13T03:39:00+00:00` | `2026-04-12 22:39:00 (Lima)` | +1.15h |
| 2 | ROCCA COLLANTES hugo Miguel FIR 06949754 sw 69cd7d20f55c37bb98fd02154430a5b198295b90 | 06949754 | `2026-04-13T03:39:15+00:00` | `2026-04-12 22:39:15 (Lima)` | +1.15h |
| 3 | ROMERO CASTILLO maria Esperanza FIR 06875237 sw cd1f7552496cad2ed0df08de167714080beef731 | 06875237 | `2026-04-13T03:39:26+00:00` | `2026-04-12 22:39:26 (Lima)` | +1.16h |

- **¿Humanos firmaron post-upload?** **SÍ**
- **Primer humano firmó**: +1.15h vs upload
- **Último humano firmó**: +1.16h vs upload
