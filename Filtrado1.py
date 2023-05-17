import pandas as pd

# Carga el archivo CSV
data = pd.read_csv('pokemon.csv')

# Selecciona las columnas que te interesan
filtered_data = data[['name', 'capture_rate', 'base_total']]

# Guarda el resultado en un nuevo archivo CSV
filtered_data.to_csv('pokemon_filtrado1.csv', index=False)