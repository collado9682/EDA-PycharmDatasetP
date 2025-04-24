# 1. Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

# 2. Leer el archivo CSV
df_movies= pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

# 3. Mostrar las primeras filas del DataFrame para revisar su contenido
print(df_movies.head())
print(df_movies.dtypes)

