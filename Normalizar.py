#normalizamos y hacemos la inversa



minimo = df_pokemon_filt['capture_rate'].min()
maximo = df_pokemon_filt['capture_rate'].max()

df_pokemon_filt['capture_rate_normalizada'] = (df_pokemon_filt['capture_rate'] -minimo) / (maximo - minimo)
df_pokemon_filt['capture_rate_normalizada'] = df_pokemon_filt['capture_rate_normalizada'] * (10 - 0) + 0

df_pokemon_filt.head()