# 5.	Directores Destacados
# Finalmente, se analizarán los directores más frecuentes y las valoraciones promedio de sus películas.
# •	Cuenta cuántas películas ha dirigido cada director usando value_counts() en la columna directors.
# •	Muestra los 10 directores que aparecen con más frecuencia.
# •	Calcula el promedio de tomatometer_rating para las películas de solo estos 10 directores. Pista: Puedes filtrar el DataFrame original para incluir solo las filas de estos directores y luego usar groupby('directors')['tomatometer_rating'].mean().
# •	Crea un gráfico de barras simple que muestre el nombre de estos 5 directores y su tomatometer_rating promedio

#Importar las librerías
import pandas as pd
import matplotlib.pyplot as plt

df_movies= pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

# Cuenta cuántas películas ha dirigido cada director usando value_counts() en la columna directors.

peliculas_director= df_movies['directors'].value_counts()
#print(peliculas_director)

# •	Muestra los 10 directores que aparecen con más frecuencia.
top_10_directores = peliculas_director.head(10)
print(top_10_directores)

#Dataframe original
top_10_nombres= top_10_directores.index.tolist()
df_top_10_directores= df_movies[df_movies['directors'].isin(top_10_nombres)].copy()

#calcular el promedio de tomatometer_rating para peliculas de solo los 10 directores
promedio_por_director= df_top_10_directores.groupby('directors')['tomatometer_rating'].mean().sort_values(ascending=False)
print(promedio_por_director)

# •	Crea un gráfico de barras simple que muestre el nombre de estos 5 directores y su tomatometer_rating promedio
top_5= promedio_por_director.head(5)

plt.figure(figsize = (8,8))
plt.bar(top_5.index.tolist(), top_5.values, color = 'skyblue')
plt.title("Calificación promedio de los top 5 directores más frecuentes")
plt.xlabel('Director')
plt.xticks(rotation=45, ha='right')
plt.ylabel("Promedio Tomatómetro")
plt.tight_layout()
plt.show()