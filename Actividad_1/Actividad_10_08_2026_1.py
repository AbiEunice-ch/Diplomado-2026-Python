import pandas as pd
df = pd.read_csv("dataset_practica.csv")

#Mostrar las primeras 10 filas 
#print(df.head(10))

#Mostrar las ùltimas 5 filas 
#print(df.tail(5))

#Obtner las dimensiones
#print("Dimensiones del Dataset:", df.shape)

#Mostrar las columnas
#print(df.columns)

#Mostrar el tipo de datos de cada columna
#print(df.dtypes)

#Seleccionar Nombre, Ciudad y Total Gastado
#new_df = df[["Nombre", "Ciudad", "Total_Gastado"]]
#print(new_df)

#Mostrar las primeras 10 filas
#print(new_df.head(10))

#Calcular el gasto promedio
#Gasto_prom = df["Total_Gastado"].mean()
#print("Gasto promedio:", Gasto_prom)

#Identificar el gasto máximo 
#Gasto_max = df["Total_Gastado"].max()
#print("Gasto máximo:", Gasto_max)

#Nuevo DataFrame con clientes mayores a 5 compras, Gasto superior a 3000 y de CDMX
#filtered_df = df[(df["Num_Compras"] > 5) & (df["Total_Gastado"] > 3000) & (df["Ciudad"] == "CDMX")]
#print(filtered_df)

#--------Identificar valores faltantes -------
#Eliminar registros sin correo
registros_sin_correo = df[df["Email"].isnull()]
print("Registros sin correo:", registros_sin_correo)

#Imputar una variable numerica utilizando la media
df["Total_Gastado"].fillna(df["Total_Gastado"].mean(), inplace=True)

#Contar duplicados en la columna ID_Cliente
duplicados = df["ID_Cliente"].duplicated().sum()
print("Número de duplicados en la columna ID_Cliente:", duplicados)

#*****************************
#Gasto promedio por membresia
gasto_promedio_membresia = df.groupby("Membresia")["Total_Gastado"].mean()
print("Gasto promedio por membresia:", gasto_promedio_membresia)

#Nùmero de clientes por ciudad 
num_clientes_ciudad = df.groupby("Ciudad")["ID_Cliente"].nunique()
print("Número de clientes por ciudad:", num_clientes_ciudad)


#Gasto total por ciudad
gasto_total_ciudad = df.groupby("Ciudad")["Total_Gastado"].sum()
print("Gasto total por ciudad:", gasto_total_ciudad)
