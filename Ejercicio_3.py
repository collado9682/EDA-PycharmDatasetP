
# 3.	Comparación de Valoraciones
# En esta sección se comparan las valoraciones de la crítica (tomatometer_rating) y de la audiencia (audience_rating) para detectar diferencias.
# •	Calcula y muestra el promedio (media) de tomatometer_rating para todas las películas.
# •	Calcula y muestra el promedio (media) de audience_rating para todas las películas.
# •	Crea una nueva columna en tu DataFrame llamada rating_diff que sea la resta entre audience_rating y tomatometer_rating para cada película.
# •	Genera un histograma de la columna rating_diff. Esto te mostrará visualmente si las diferencias entre audiencia y críticos son mayormente pequeñas, grandes, positivas (audiencia califica más alto) o negativas (críticos califican más alto). Nota: Agrupar en intervalos de 30 (bins=30)

#Importar las librerías
import pandas as pd
import matplotlib.pyplot as plt

df_movies= pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

# 11. Promedio de valoración del tomatómetro y la audiencia o publico

# Promedio de valoración del tomatómetro
promedio_críticos= df_movies['tomatometer_rating'].mean()

# Promedio de valoración de la audiencia o publico
promedio_audiencia= df_movies['audience_rating'].mean()


print(f"Promedio de valoración por críticos: {promedio_críticos:.2f}")
print(f"Promedio de valoración por audiencia: {promedio_audiencia:.2f}")





