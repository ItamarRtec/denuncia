# DENUNCIA — Inconsistencias temporales en publicación de actas ONPE EG2026

Este repositorio contiene **evidencia documental verificable** de que la Oficina Nacional de Procesos Electorales (ONPE) del Perú publicó como **"Contabilizadas"** los resultados de **337 mesas de votación** durante la Elección General 2026, **antes de que los miembros de mesa hubieran firmado digitalmente el acta correspondiente**.

## Estado oficial de ONPE

ONPE declaró públicamente: *"no he publicado ningún resultado sin haber digitalizado el acta"*.

La **Cartilla de Instrucciones para Personeros STAE EG2026** (documento oficial de ONPE incluido en este repositorio) establece en sus páginas 18-19 que el orden del flujo de escrutinio es:

1. Miembros de mesa firman digitalmente las actas de escrutinio
2. Se imprimen las actas físicas
3. **Recién después** se transmiten los resultados a ONPE

## Lo que la propia API de ONPE muestra

Para 337 mesas (todas en Lima Metropolitana o Callao), comparando dos campos públicos de la API ONPE:

- `lineaTiempo[0].fechaRegistro` (con `codigoEstadoActa = "C"`): el momento en que ONPE marcó la mesa como **Contabilizada** en su sistema (publicación)
- Timestamp `/M` de cada firma digital dentro del PDF del acta (con certificado X.509 personal y DNI peruano)

Las firmas humanas son **posteriores al `fechaRegistro`** en mediana **+4.07 horas** (máximo +14.50h). Es decir: ONPE marcó la mesa como contabilizada y publicó el resultado, y horas después los miembros de mesa firmaron digitalmente.

**Esto NO es prueba de fraude electoral** — es prueba de que el flujo no funcionó como ONPE públicamente afirma que funciona, y de que los resultados estuvieron publicados antes de que existiera la firma humana de la mesa.

## Estructura

```
denuncia/
├── README.md                            ← este archivo
├── METHODOLOGY.md                       ← cómo medimos, qué significa cada campo
├── HOW_TO_VERIFY.md                     ← cómo verificar independientemente
├── COMUNICADO.md                        ← statement público listo para difundir
├── EVIDENCE_INDEX.csv                   ← 337 mesas, 1 fila c/u con resumen
├── manifest.json                        ← SHA-256 de todos los artefactos
├── ROOT_HASH.txt                        ← SHA-256 del manifest (raíz Merkle)
├── Cartilla-Personeros_STAE_EG2026.pdf  ← documento oficial ONPE: el flujo declarado
├── mesas_anomalas/                      ← 337 mesas confirmadas
│   └── <codigo_mesa>/
│       ├── acta.pdf                     ← copia byte-a-byte del PDF original
│       ├── api_response.json            ← respuesta cruda de API ONPE capturada
│       ├── metadata.json                ← análisis estructurado
│       ├── signatures.json              ← firmantes con DNI + certificados X.509
│       └── analysis.md                  ← reporte legible humano
├── mesas_descartadas/                   ← 12 mesas evaluadas pero NO incluidas (transparencia)
│   └── <codigo_mesa>/                   ← (su análisis no cumplió el criterio estricto)
└── scripts/                             ← scripts reproducibles
    ├── build_evidence.py                ← regenera todo desde fuente ONPE
    ├── verify_manifest.py               ← cualquiera puede correr esto y verificar SHA-256
    ├── recompute_with_fechaRegistro.py  ← recálculo con métrica correcta
    ├── reevaluar_completo.py            ← análisis estadístico de los timestamps
    └── archive_onpe_snapshots.py        ← solicita snapshots a archive.org
```

## Concentración geográfica

Las 337 mesas están **100% en Lima Metropolitana o Callao**:
- LIMA: 298 mesas (88.4%)
- CALLAO: 39 mesas (11.6%)
- Cero mesas en los otros 23 departamentos

Esta distribución indica que el patrón **no es estructural** del sistema STAE — es específico de cierta infraestructura o centros de procesamiento de Lima/Callao.

## Cómo verificar tú mismo (3 minutos)

1. Elegí una mesa cualquiera del archivo `EVIDENCE_INDEX.csv`
2. Andá a https://resultadoelectoral.onpe.gob.pe y buscá esa mesa
3. Descargá el PDF del acta
4. Comparalo con el PDF que está en `mesas_anomalas/<codigo_mesa>/acta.pdf` — el SHA-256 debe coincidir
5. Abrí el PDF en **Adobe Acrobat Reader** (no en navegador), abrí el panel de Firmas, comprobá los timestamps
6. Consultá la API: `https://resultadoelectoral.onpe.gob.pe/presentacion-backend/actas/buscar/mesa?codigoMesa=<MESA>&idEleccion=10` y mirá el `lineaTiempo`
7. Verificá: el timestamp de las firmas humanas (`/M` en el PDF) es POSTERIOR al `fechaRegistro` del estado `C` (Contabilizada)

Detalle paso a paso en `HOW_TO_VERIFY.md`.

## Anti-tamper / preservación de evidencia

Pensando como adversario, la cadena de defensa es:

1. **PDFs copiados byte-a-byte** y hasheados con SHA-256 — si ONPE re-emite los PDFs con timestamps "corregidos", los hashes no coincidirán y eso ya es evidencia adicional
2. **Captura de API ONPE en el momento** — el archivo `api_response.json` registra exactamente qué devolvió la API en el momento de captura (incluyendo el `lineaTiempo` completo); si después modifican la respuesta, queda documentado
3. **Manifest tamper-evident** — `manifest.json` lista SHA-256 de todos los artefactos; `ROOT_HASH.txt` es el SHA-256 del manifest, formando un árbol Merkle minimal
4. **Git history** — cada commit es un timestamp inmutable; pushear a múltiples remotos crea testigos distribuidos
5. **OpenTimestamps** (recomendado, ver `HOW_TO_VERIFY.md`) — sello cripto-temporal de tercera parte vía blockchain Bitcoin

## Limitaciones declaradas

- **No es prueba de fraude electoral**. Solo prueba que la cronología documentada por ONPE (en su Cartilla oficial) no se cumplió en estas 337 mesas.
- **No verificamos que los conteos publicados sean numéricamente incorrectos**. Para eso se requiere comparación con los números escritos a mano en el papel original.
- **No conocemos la causa raíz**. Podría ser falla técnica, decisión administrativa, o protocolo no documentado públicamente. La denuncia exige explicación, no acusa específicamente.
- **Posible subcuenta**: la muestra de 337 surge de un análisis de las 79,014 mesas contabilizadas; la cifra real podría ser mayor si se aplica el mismo análisis con criterios más amplios.

## Errata

Una versión inicial de este análisis usó el campo `daudFechaCreacion` (timestamp administrativo del archivo adjunto) como momento de "publicación", lo cual era incorrecto. El campo correcto es `lineaTiempo[0].fechaRegistro` con `codigoEstadoActa = "C"`. La corrección está documentada en `METHODOLOGY.md`. El análisis publicado utiliza la métrica correcta.

## Contacto

[Por completar]

## Licencia

Datos públicos de ONPE re-empaquetados con análisis. Distribución libre con atribución.
