import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Cargar los datos del archivo CSV en un dataframe de pandas
df = pd.read_csv('pokemon.csv')

# Seleccionar las columnas que deseas normalizar
cols_to_normalize = ['attack', 'defense', 'speed']

# Crear un objeto MinMaxScaler
scaler = MinMaxScaler()

# Normalizar los datos seleccionados
df[cols_to_normalize] = scaler.fit_transform(df[cols_to_normalize])

# Guardar los datos normalizados en un nuevo archivo CSV
df.to_csv('pokemon_normalized.csv', index=False)