import pandas as pd
df = pd.read_csv("dataset_practica.csv")

#Mostrar las primeras 10 filas 
print(df.head(10))

#Mostrar las ùltimas 5 filas 
print(df.tail(5))

#Obtner las dimensiones
print("Dimensiones del Dataset:", df.shape)

#Mostrar las columnas
print(df.columns)

#Mostrar el tipo de datos de cada columna
print(df.dtypes)

#Seleccionar Nombre, Ciudad y Total Gastado
new_df = df[["Nombre", "Ciudad", "Total_Gastado"]]
print(new_df)

#Mostrar las primeras 10 filas
print(new_df.head(10))

#Calcular el gasto promedio
Gasto_prom = df["Total_Gastado"].mean()
print("Gasto promedio:", Gasto_prom)

#Identificar el gasto máximo 
Gasto_max = df["Total_Gastado"].max()
print("Gasto máximo:", Gasto_max)

#Nuevo DataFrame con clientes mayores a 5 compras, Gasto superior a 3000 y de CDMX
filtered_df = df[(df["Num_Compras"] > 5) & (df["Total_Gastado"] > 3000) & (df["Ciudad"] == "CDMX")]
print(filtered_df)

