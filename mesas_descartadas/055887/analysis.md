# Mesa 055887 — evidencia Nivel 2 (digital)

_Capturado: 2026-04-19T22:53:58.165888+00:00_

## Ubicación
- **Departamento**: LIMA
- **Provincia**: LIMA
- **Distrito**: SAN JUAN DE MIRAFLORES
- **Local de votación**: IE 7070 DRA MARIA REICHE GROSSE NEUMAN (código 53231)
- **Ubigeo**: 140136

## Resultado declarado por ONPE
- Estado del acta: **Contabilizada** (código `C`)
- Electores hábiles: 299
- Votos emitidos: 231
- Votos válidos: 220
- Participación: 77.258%

## Los dos timestamps clave

| Evento | UTC | Hora Perú (UTC-5) |
|---|---|---|
| ONPE registró el voto (`daudFechaCreacion`) | `2026-04-13T01:33:06.746000+00:00` | `2026-04-12 20:33:06 (Lima)` |
| PDF de respaldo creado (`/CreationDate`) | `2026-04-13T02:41:17+00:00` | `2026-04-12 21:41:17 (Lima)` |

**Brecha:** PDF creado **1.14 horas DESPUÉS del upload** (0.05 días).

## Verificación independiente

1. Visitar https://resultadoelectoral.onpe.gob.pe y buscar la mesa **055887**
2. Descargar el PDF del acta
3. Verificar SHA-256: `658e1d549d45d4f3ea601d02fbd27439711c802f46e08e8440d102fbf8379477`
4. Abrir el PDF en **Adobe Acrobat Reader** (no en navegador)
5. Click en el icono de pluma (panel "Firmas") en la barra izquierda
6. Verificar las 4 firmas: **3** humanas + **1** "AGENTE AUTOMATIZADO STAE"

## Firmas extraídas del PDF

| # | Firmante | DNI | Firmó (UTC) | Firmó (Hora Perú) | vs upload |
|---|---|---|---|---|---|
| Agente | AGENTE AUTOMATIZADO STAE (software ONPE) | — | `2026-04-13T00:54:36+00:00` | `2026-04-12 19:54:36 (Lima)` | -0.64h |
| 1 | GONZALES PAUCAR wendell Saul FIR 77415693 sw 5d9b832b462786edf1fff0d638b135bd8822043e | 77415693 | `2026-04-13T02:41:43+00:00` | `2026-04-12 21:41:43 (Lima)` | +1.14h |
| 2 | GUTIERREZ CIEZA edinzon FIR 46366848 sw 5601a7aaa5c160cbd9c8a34b7bff09dbdca14eac | 46366848 | `2026-04-13T02:42:03+00:00` | `2026-04-12 21:42:03 (Lima)` | +1.15h |
| 3 | GUZMAN ANTUNEZ camila Alejandra FIR 73426302 sw 3601d4cb34abcd7c2658fea13e367216c6f8eb90 | 73426302 | `2026-04-13T02:42:18+00:00` | `2026-04-12 21:42:18 (Lima)` | +1.15h |

- **¿Humanos firmaron post-upload?** **SÍ**
- **Primer humano firmó**: +1.14h vs upload
- **Último humano firmó**: +1.15h vs upload
