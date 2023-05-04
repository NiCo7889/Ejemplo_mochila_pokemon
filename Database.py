import csv
import chardet

with open('pokemon.csv', 'rb') as archivo_csv:
    resultado = chardet.detect(archivo_csv.read())
    codificacion = resultado['encoding']

with open('pokemon.csv', 'r', encoding=codificacion) as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    for fila in lector_csv:
        print(fila)

import pandas as pd

# Cargar el archivo CSV en un dataframe
df = pd.read_csv('pokemon.csv')

# Ordenar el dataframe por nombre, peso y beneficio
df = df.sort_values(by=['Name', 'Weight', 'Power'])

# Calcular la media de las estadísticas
df['Avg_Stats'] = df[['Attack', 'Defense', 'HP', 'Speed', 'SpecialAttack', 'SpecialDefense']].mean(axis=1)

# Guardar el dataframe ordenado y con la media de las estadísticas en un nuevo archivo CSV
df.to_csv('pokemon_ordenado.csv', index=False)
