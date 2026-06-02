#!/usr/bin/env python3
"""
Analizador de Secuencias FASTA.

Este programa lee un archivo FASTA, calcula métricas básicas de las secuencias
y permite aplicar filtros por longitud mínima y porcentaje mínimo de GC.

Uso:
    python src/analizador.py data/ejemplo.fasta
    python src/analizador.py data/ejemplo.fasta --min-len 20
    python src/analizador.py data/ejemplo.fasta --min-gc 50
"""

import argparse
import os
import sys


def leer_fasta(ruta_archivo):
    """
    Lee un archivo FASTA y extrae sus secuencias.

    Args:
        ruta_archivo (str): Ruta del archivo FASTA.

    Returns:
        list: Lista de diccionarios. Cada diccionario contiene el encabezado
        y la secuencia correspondiente.

    Raises:
        FileNotFoundError: Si el archivo no existe.
        ValueError: Si el archivo no contiene secuencias válidas.
    """
    secuencias = []
    encabezado_actual = None
    partes_secuencia = []

    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea = linea.strip()

            if not linea:
                continue

            if linea.startswith(">"):
                if encabezado_actual is not None:
                    secuencias.append(
                        {
                            "encabezado": encabezado_actual,
                            "secuencia": "".join(partes_secuencia).upper(),
                        }
                    )

                encabezado_actual = linea[1:].strip()
                partes_secuencia = []
            else:
                partes_secuencia.append(linea)

    if encabezado_actual is not None:
        secuencias.append(
            {
                "encabezado": encabezado_actual,
                "secuencia": "".join(partes_secuencia).upper(),
            }
        )

    secuencias_validas = []
    for item in secuencias:
        if item["encabezado"] and item["secuencia"]:
            secuencias_validas.append(item)

    if not secuencias_validas:
        raise ValueError("El archivo no contiene secuencias FASTA válidas.")

    return secuencias_validas


def calcular_gc(secuencia):
    """
    Calcula el porcentaje de contenido GC de una secuencia.

    El contenido GC corresponde al porcentaje de bases que son G o C
    respecto al total de bases de la secuencia.

    Args:
        secuencia (str): Secuencia de ADN.

    Returns:
        float: Porcentaje de GC.
    """
    if len(secuencia) == 0:
        return 0.0

    seq = secuencia.upper()
    cantidad_g = seq.count("G")
    cantidad_c = seq.count("C")
    bases_gc = cantidad_g + cantidad_c
    gc = (bases_gc / len(seq)) * 100

    return gc


def analizar_secuencias(secuencias):
    """
    Calcula métricas básicas para cada secuencia.

    Args:
        secuencias (list): Lista de diccionarios con encabezado y secuencia.

    Returns:
        list: Lista de diccionarios con encabezado, longitud y porcentaje GC.
    """
    resultados = []

    for item in secuencias:
        secuencia = item["secuencia"]

        resultados.append(
            {
                "encabezado": item["encabezado"],
                "longitud": len(secuencia),
                "gc": calcular_gc(secuencia),
            }
        )

    return resultados


def filtrar_resultados(resultados, min_len=None, min_gc=None):
    """
    Filtra los resultados según longitud mínima y porcentaje mínimo de GC.

    Args:
        resultados (list): Lista de resultados del análisis.
        min_len (int, optional): Longitud mínima requerida.
        min_gc (float, optional): Porcentaje mínimo de GC requerido.

    Returns:
        list: Lista de resultados que cumplen los filtros.
    """
    filtrados = []

    for resultado in resultados:
        cumple_longitud = min_len is None or resultado["longitud"] >= min_len
        cumple_gc = min_gc is None or resultado["gc"] >= min_gc

        if cumple_longitud and cumple_gc:
            filtrados.append(resultado)

    return filtrados


def mostrar_resultados(resultados, total_original):
    """
    Muestra los resultados del análisis en la terminal.

    Args:
        resultados (list): Lista de resultados filtrados.
        total_original (int): Número total de secuencias antes de filtrar.

    Returns:
        None
    """
    print("\n=== Analizador de Secuencias FASTA ===\n")
    print(f"Secuencias encontradas: {total_original}")
    print(f"Secuencias mostradas: {len(resultados)}\n")

    if not resultados:
        print("Ninguna secuencia cumple con los filtros indicados.")
        return

    for numero, resultado in enumerate(resultados, start=1):
        print(f"Secuencia {numero}")
        print(f"  Encabezado: {resultado['encabezado']}")
        print(f"  Longitud: {resultado['longitud']} bases")
        print(f"  GC: {resultado['gc']:.2f}%")
        print()


def crear_parser():
    """
    Crea y configura el parser de argumentos de la terminal.

    Returns:
        argparse.ArgumentParser: Parser configurado para el programa.
    """
    parser = argparse.ArgumentParser(
        description="Analiza secuencias de ADN en formato FASTA y permite aplicar filtros."
    )

    parser.add_argument(
        "archivo",
        help="Ruta del archivo FASTA que se desea analizar.",
    )

    parser.add_argument(
        "--min-len",
        type=int,
        default=None,
        help="Longitud mínima de las secuencias que se mostrarán.",
    )

    parser.add_argument(
        "--min-gc",
        type=float,
        default=None,
        help="Porcentaje mínimo de GC de las secuencias que se mostrarán.",
    )

    return parser


def main():
    """
    Ejecuta el flujo principal del programa.

    Lee argumentos, procesa el archivo FASTA, calcula métricas, aplica filtros
    y muestra los resultados en la terminal.

    Returns:
        None
    """
    parser = crear_parser()
    args = parser.parse_args()

    try:
        if not os.path.exists(args.archivo):
            raise FileNotFoundError(f"El archivo '{args.archivo}' no existe.")

        secuencias = leer_fasta(args.archivo)
        resultados = analizar_secuencias(secuencias)
        resultados_filtrados = filtrar_resultados(
            resultados,
            min_len=args.min_len,
            min_gc=args.min_gc,
        )
        mostrar_resultados(resultados_filtrados, total_original=len(resultados))

    except FileNotFoundError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    except Exception as error:  # pragma: no cover - unexpected errors
        print(f"Error inesperado: {error}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
