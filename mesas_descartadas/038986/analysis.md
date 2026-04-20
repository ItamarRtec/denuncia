# Mesa 038986 — evidencia Nivel 2 (digital)

_Capturado: 2026-04-19T22:54:15.864545+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: BREÑA
- **Local de votación**: IE 0005 ROSA DE SANTA MARIA (código 2755)
- **Ubigeo**: 140104

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 296
- Votos emitidos: 237
- Votos válidos: 217
- Participación: 80.068%

## Los dos timestamps clave

| Evento | UTC | Hora Perú (UTC-5) |
|---|---|---|
| ONPE registró el voto (`daudFechaCreacion`) | `2026-04-13T02:34:48.949000+00:00` | `2026-04-12 21:34:48 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T03:04:06+00:00` | `2026-04-12 22:04:06 (Lima)` |

**Brecha:** PDF creado **0.49 horas DESPUÉS del upload** (0.02 días).

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar la mesa **038986**
2. Descargar el PDF del acta
3. Verificar SHA-256: `c723f57923eb1725eb8db52a7e1ae813907e78c85d1223354697a588b54af393`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las 4 firmas: **3** humanas + **1** "AGENTE AUTOMATIZADO STAE"

## Firmas extraídas del PDF

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs upload |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE) | — | `2026-04-13T01:40:56+00:00` | `2026-04-12 20:40:56 (Lima)` | -0.90h |
| 1 | HURTADO SALAZAR ana Susana FIR 06772585 sw 71db9d71de68fd620913a2e23446e9e066fb5be5 | 06772585 | `2026-04-13T03:04:24+00:00` | `2026-04-12 22:04:24 (Lima)` | +0.49h |
| 2 | HUANHUAYO MACHUCA marisol FIR 40361136 sw 86f2c5102cfe13e9f19a1cc39ff5a1fa0a57451e | 40361136 | `2026-04-13T03:04:41+00:00` | `2026-04-12 22:04:41 (Lima)` | +0.50h |
| 3 | HURTADO EGOAVIL luis Alvaro FIR 73352183 sw ff63a86481e7a1d0c8993de8330a99380bc6b98d | 73352183 | `2026-04-13T03:04:55+00:00` | `2026-04-12 22:04:55 (Lima)` | +0.50h |

- **¿Humanos firmaron post-upload?** **SÍ**
- **Primer humano firmó**: +0.49h vs upload
- **Último humano firmó**: +0.50h vs upload
