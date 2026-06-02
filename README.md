# Analizador de Secuencias FASTA

Este proyecto es un programa en Python para analizar secuencias de ADN en formato FASTA.

El programa lee un archivo `.fasta`, identifica las secuencias contenidas en él y calcula métricas básicas como:

- Encabezado de cada secuencia.
- Longitud de cada secuencia.
- Porcentaje de contenido GC.
- Número total de secuencias analizadas.

También permite aplicar filtros por longitud mínima y porcentaje mínimo de GC.

## Estructura del proyecto

```text
analizador-fasta/
├── README.md
├── docs/
│   ├── requisitos.md
│   └── diseño.md
├── src/
│   └── analizador.py
└── data/
    └── ejemplo.fasta
```

## Requisitos

Para ejecutar el programa se necesita tener instalado Python 3.

Se puede revisar la versión de Python con:

```bash
python --version
```

o:

```bash
python3 --version
```

## Uso del programa

Desde la carpeta principal del proyecto, ejecutar:

```bash
python src/analizador.py data/ejemplo.fasta
```

Si en el sistema el comando `python` no funciona, usar:

```bash
python3 src/analizador.py data/ejemplo.fasta
```

## Uso sin filtros

```bash
python src/analizador.py data/ejemplo.fasta
```

Este comando analiza todas las secuencias del archivo.

## Filtrar por longitud mínima

```bash
python src/analizador.py data/ejemplo.fasta --min-len 20
```

Este comando muestra solo las secuencias con longitud mayor o igual a 20 bases.

## Filtrar por porcentaje mínimo de GC

```bash
python src/analizador.py data/ejemplo.fasta --min-gc 50
```

Este comando muestra solo las secuencias con porcentaje GC mayor o igual a 50%.

## Usar ambos filtros

```bash
python src/analizador.py data/ejemplo.fasta --min-len 20 --min-gc 50
```

Este comando muestra solo las secuencias que cumplen ambas condiciones.

## Ejemplo de salida

```text
=== Analizador de Secuencias FASTA ===

Secuencias encontradas: 4
Secuencias mostradas: 3

Secuencia 1
  Encabezado: secuencia_1_humana
  Longitud: 40 bases
  GC: 55.00%
```

## Manejo de errores

Si el archivo no existe, el programa muestra un mensaje claro:

```bash
python src/analizador.py data/noexiste.fasta
```

Salida esperada:

```text
Error: El archivo 'data/noexiste.fasta' no existe.
```

## Archivos de documentación

La carpeta `docs` contiene:

- `requisitos.md`: descripción del problema, objetivo y requisitos funcionales.
- `diseño.md`: algoritmo del programa y diagrama Mermaid.

## Autor
Torres Rojas Camila
Proyecto realizado como práctica de programación.
