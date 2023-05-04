import pandas as pd
from datetime import datetime, timedelta

# Lee el archivo CSV en un DataFrame de pandas
pokemon_df = pd.read_csv('pokemon.csv')

# Convierte la columna de fecha en un objeto de datetime
pokemon_df['Fecha de finalización'] = pd.to_datetime(pokemon_df['Fecha de finalización'])

# Define el número de días que quieres buscar Pokemon
num_dias = 7

# Define la fecha de inicio de la búsqueda
fecha_inicio = datetime.today()

# Define la fecha final de la búsqueda
fecha_fin = fecha_inicio + timedelta(days=num_dias)

# Crea un bucle que recorra todos los días de búsqueda
while fecha_inicio < fecha_fin:

    # Filtra los Pokemon que todavía están disponibles en este día
    pokemon_disponibles = pokemon_df[pokemon_df['Fecha de finalización'] >= fecha_inicio]

    # Si no hay Pokemon disponibles para capturar en este día, pasa al siguiente día
    if pokemon_disponibles.empty:
        fecha_inicio += timedelta(days=1)
        continue

    # Selecciona el Pokemon con el valor más alto para capturar en este día
    pokemon_capturado = pokemon_disponibles.loc[pokemon_disponibles['Valor'].idxmax()]

    # Imprime el Pokemon capturado y su valor
    print(f"¡Capturaste a {pokemon_capturado['Nombre']} por un valor de {pokemon_capturado['Valor']}!")

    # Avanza la fecha de inicio al día siguiente
    fecha_inicio += timedelta(days=1)
