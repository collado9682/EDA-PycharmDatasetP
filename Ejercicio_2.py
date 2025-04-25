# 2.	Exploración Básica
# Se realizará una exploración inicial del dataset para conocer su tamaño, los géneros más comunes y las categorías de calificación.
# •	¿Cuántas películas hay? Muestra el número total de filas en el DataFrame (que corresponde al número de películas). Pista: Usa len() o df_movies.shape.
# •	¿Cómo se distribuyen las calificaciones? Cuenta cuántas películas pertenecen a cada categoría en tomatometer_status (Certified Fresh, Fresh, Rotten) usando value_counts().
# •	Visualiza la distribución de calificaciones: Crea un gráfico circular (pie chart) simple para mostrar la proporción de cada tomatometer_status. Asegúrate de añadir etiquetas.

#IMPORTAR LAS LIBRERIAS

import pandas as pd
import matplotlib.pyplot as plt

df_movies= pd.read_csv("./Data/Rotten Tomatoes Movies.csv")
#print(df_movies)

# 8. ¿Cuántas películas hay en total? Mostrar en consola

print(f"Total de peliculas: {len(df_movies)}")

# 9. ¿Cuántas películas fueron calificadas como "Certified Fresh", "Fresh" y "Rotten"? usa value counts sobre la columna tomatometer_status

df_movies_calificaciones= df_movies['tomatometer_status'].value_counts()
print(df_movies_calificaciones)

#10 •	Visualiza la distribución de calificaciones: Crea un gráfico circular (pie chart) simple para mostrar la proporción de cada tomatometer_status. Asegúrate de añadir etiquetas.

#Propiedades del grafico
plt.figure(figsize= (10,10))
plt.pie(df_movies_calificaciones, labels=['Rotten', 'Fresh','Certified Fresh'], autopct='%1.0f%%', colors=['steelblue', 'darkorange', 'green'], startangle=140)
plt.title("Distribución de calificaciones")
plt.show()
