# import csv

# with open('pokemon.csv', 'r', encoding='utf-8') as archivo_csv:
#     lector_csv = csv.reader(archivo_csv)
#     for fila in lector_csv:
#         print(fila)

import csv
import chardet

with open('pokemon.csv', 'rb') as archivo_csv:
    resultado = chardet.detect(archivo_csv.read())
    codificacion = resultado['encoding']

with open('pokemon.csv', 'r', encoding=codificacion) as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)
