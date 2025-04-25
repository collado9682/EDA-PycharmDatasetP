# 4.	Análisis por Género
# Muchas películas tienen múltiples géneros. Aquí deberás a separar esos géneros y analizar promedios por cada uno.
# •	Este paso se requiere manejar géneros múltiples. Primero, crea una copia de tu DataFrame para no modificar el original.
# •	En la copia, divide la columna genre por “,” para obtener una lista de géneros para cada película y expande estas listas para que cada género tenga su propia fila. Pista: Usa .str.split(',').explode(). Asigna el resultado generado en un nuevo DataFrame “df_genres_exploded”.
# •	Usando df_genres_exploded, calcula el promedio de audience_rating para cada género individual. Pista: Usa groupby('genre')['audience_rating'].mean().
# •	Muestra los 10 géneros con el promedio de calificación de audiencia más alto haciendo uso de un diagrama de pastel.

#Importar las librerías
import pandas as pd
import matplotlib.pyplot as plt

df_movies= pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

df_movies_copy=df_movies.copy()

#separar los géneros

df_genres_exploded = df_movies_copy.assign(
  genre=df_movies_copy['genre'].str.split(',')
).explode('genre')

#print(df_movies_copy)
df_genres_exploded['genre'] = df_genres_exploded['genre'].str.strip()

#Calcular el promedio de audience_rating para cada género individual
promedio_audiencia_géneros= df_genres_exploded.groupby('genre')['audience_rating'].mean().sort_values(ascending=False)
#print(promedio_audiencia_géneros)

# •	Muestra los 10 géneros con el promedio de calificación de audiencia más alto haciendo uso de un diagrama de pastel.
Top_10_generos= promedio_audiencia_géneros.head(10)
print(Top_10_generos)

#Propiedades del gráfico
plt.figure(figsize= (10,10))
plt.pie(Top_10_generos,labels=Top_10_generos.index, colors=['steelblue', 'darkorange', 'green','gold','lightpink', 'slateblue','lightblue', 'khaki','indianred','goldenrod'], startangle=140)
plt.title("Top 10 géneros con mejor promedio de valoración")
plt.tight_layout()
plt.show()