import pandas as pd

# Carga el archivo CSV
data = pd.read_csv('pokemon_normalizado.csv')

# Selecciona las columnas que te interesan
filtered_data = data[['name', 'capture_rate', 'base_total']]

# Guarda el resultado en un nuevo archivo CSV
filtered_data.to_csv('pokemon_filtrado.csv', index=False)

# Elimino los NaN
data.dropna().reset_index(drop=True)
data

# Conteo de valores perdidos/faltantes  
data.isna().sum()