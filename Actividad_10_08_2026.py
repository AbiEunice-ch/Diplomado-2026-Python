import pandas as pd
df = pd.read_csv("ecommerce_data.csv")
print(df.head(10))

#-------------EDA -------------
#Cuántos nulos existen
print("Número de valores nulos por cada columna:", df.isnull().sum())

#Porcentaje de nulos por columna
prc_nulos = (df.isnull().sum() / len(df))*100
print("Porcentaje de nulos:", prc_nulos)


#Tipo de datos de cada columna
print("Tipo de datos por columna:", df.dtypes)

#Describiendo cada columna
#print("Descripción de cada columna:", df.describe(include="all"))

#1.Cuántos clientes y transacciones tenemos
print("Número de clientes:", df["ID_Cliente"].nunique())
print("Número de transacciones:", df["ID_Transaccion"].nunique())

#2.Qué porcentaje de datos esta incompleto
print("Porcentaje de valores nulos por columna:", df.isnull().mean()*100)


#3.Qué región genera más ingresos
print("Región con más ingresos:", df.groupby("Region")["Total_Gastado"].sum().idxmax())


#4.Qué categoria tiene mayor gastoo promedio
print("Categoria con mayor gasto promedio:", df.groupby("Categoria")["Total_Gastado"].mean().idxmax())

#5. Qué clientes realizaron compras superiores a $5000?
clientes_mayor_5000 =  df[df["Total_Gastado"]>5000]["ID_Cliente"].unique()
suma_clientes_5000 = len(clientes_mayor_5000)
porcentaje_clientes_5000 = (suma_clientes_5000 / df["ID_Cliente"].nunique()) * 100
print("Clientes con compras superiores a $5000:", clientes_mayor_5000)
print("Número de clientes con compras superiores a $5000:", suma_clientes_5000)
print("Porcentaje de clientes con compras superiores a $5000:", porcentaje_clientes_5000)



