# Mesa 040118 — evidencia Nivel 2 (digital)

_Capturado: 2026-04-19T22:53:59.588720+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: COMAS
- **Local de votación**: IE 2077 SAN MARTIN DE PORRES (código 2799)
- **Ubigeo**: 140106

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 258
- Votos válidos: 213
- Participación: 86.288%

## Los dos timestamps clave

| Evento | UTC | Hora Perú (UTC-5) |
|---|---|---|
| ONPE registró el voto (`daudFechaCreacion`) | `2026-04-13T02:22:13.630000+00:00` | `2026-04-12 21:22:13 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T04:27:29+00:00` | `2026-04-12 23:27:29 (Lima)` |

**Brecha:** PDF creado **2.09 horas DESPUÉS del upload** (0.09 días).

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar la mesa **040118**
2. Descargar el PDF del acta
3. Verificar SHA-256: `8be2f574db53084b7dba27a23df163f8a019ba3c85a4ded45cfb37dfb656323d`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las 5 firmas: **4** humanas + **1** "AGENTE AUTOMATIZADO STAE"

## Firmas extraídas del PDF

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs upload |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE) | — | `2026-04-13T01:31:06+00:00` | `2026-04-12 20:31:06 (Lima)` | -0.85h |
| 1 | HUACAHUASI ACEVEDO jose Luis FIR 09973639 sw 62610ce5ef28c5c6c8a9c87a2cc97f42c2b001d6 | 09973639 | `2026-04-13T04:27:45+00:00` | `2026-04-12 23:27:45 (Lima)` | +2.09h |
| 2 | JANAMPA YNGUNZA maria De Los Angeles Elizabeth FIR 42526524 sw 433869466ae970197889eea29163c3fb4889c1bb | 42526524 | `2026-04-13T04:28:00+00:00` | `2026-04-12 23:28:00 (Lima)` | +2.10h |
| 3 | HUAMAN POVIS carlos Alberto FIR 41612260 sw 119410ff7ba95a1b9bde35a2ffaa11a7a97c8a09 | 41612260 | `2026-04-13T04:28:11+00:00` | `2026-04-12 23:28:11 (Lima)` | +2.10h |
| 4 | BARBOZA HUAMAN melissa Eveling FIR 41739071 sw c79a39d5d07606f2afc655920744de0ceb4390ef | 41739071 | `2026-04-13T04:28:59+00:00` | `2026-04-12 23:28:59 (Lima)` | +2.11h |

- **¿Humanos firmaron post-upload?** **SÍ**
- **Primer humano firmó**: +2.09h vs upload
- **Último humano firmó**: +2.11h vs upload
