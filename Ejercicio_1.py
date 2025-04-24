# 1. Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

# 2. Leer el archivo CSV
df_movies= pd.read_csv("./Data/Rotten Tomatoes Movies.csv")

# 3. Mostrar las primeras filas del DataFrame para revisar su contenido
print(df_movies.head(10))


# 4. Verificar los nombres de las columnas
print("Tipos de datos:")
print(df_movies.info())

# 5. Convertir la columna 'in_theaters_date' al tipo datetime
df_movies["in_theaters_date"]= pd.to_datetime(df_movies["in_theaters_date"])

# 6. Verificar que la conversión fue exitosa (dtypes)
print(df_movies.dtypes)
