# Requisitos del proyecto

## Nombre del proyecto

Analizador de Secuencias FASTA

## Descripción del problema

En bioinformática es común trabajar con archivos en formato FASTA. Estos archivos almacenan secuencias biológicas, como ADN, ARN o proteínas, junto con un encabezado que identifica cada secuencia.

El problema que resuelve este programa es leer un archivo FASTA y obtener información básica de cada secuencia de ADN, como su identificador, longitud y porcentaje de contenido GC.

Además, el programa permite aplicar filtros sencillos para mostrar únicamente las secuencias que cumplan ciertas condiciones.

## Objetivo general

Crear un programa en Python que lea archivos FASTA, analice las secuencias contenidas en ellos y muestre un resumen claro en la terminal.

## Requisitos funcionales

El programa debe:

1. Recibir como argumento la ruta de un archivo FASTA.
2. Leer correctamente archivos con una o varias secuencias.
3. Identificar el encabezado de cada secuencia.
4. Unir las líneas de una misma secuencia cuando estén separadas en varias líneas.
5. Calcular la longitud de cada secuencia.
6. Calcular el porcentaje de GC de cada secuencia.
7. Mostrar el número total de secuencias analizadas.
8. Mostrar los resultados en la terminal.
9. Permitir filtrar secuencias por longitud mínima usando `--min-len`.
10. Permitir filtrar secuencias por porcentaje mínimo de GC usando `--min-gc`.
11. Mostrar un mensaje de error claro si el archivo no existe.
12. Mostrar un mensaje de error claro si el archivo está vacío o no contiene secuencias válidas.

## Requisitos no funcionales

El programa debe:

1. Estar escrito en Python.
2. Tener funciones separadas para leer, analizar y mostrar resultados.
3. Incluir docstrings en todas las funciones principales.
4. Tener instrucciones de uso claras en el archivo `README.md`.
5. Incluir un archivo FASTA de ejemplo en la carpeta `data`.
6. Estar organizado en carpetas `src`, `data` y `docs`.
7. Tener historial de commits con prefijos como `init:`, `doc:`, `feat:`, `refactor:` y `fix:`.