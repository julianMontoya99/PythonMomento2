# Julián Felipe Castaño Montoya
# Santiago Torres Monsalve
# Sebastián Roldán Zapata

import pandas as pd

df =pd.read_csv('ventas.csv')
pd.set_option('display.max_columns', None)

print("INFORME".center(70," "))

print(("\n1. ¿Cuántos registros (ventas) hay en total?"))
print("Total de registros:", len(df))

print('\n2. ¿Cuántas ventas fueron "Cerradas", "Pendientes" y "Canceladas"?')
print("Ventas por estado:\n",df['ESTADO'].value_counts())

print("\n3. ¿Cuál es el valor total de ventas realizadas?")
print("Valor total ventas realizadas:", f"{df['VALOR_VENTA'].sum():,.2f}")

print("\n4. ¿Cuál es el promedio de comisión pagada por venta cerrada?")
print("Promedio de comisión por venta cerrada:", f"{df[df['ESTADO']=="Cerrado"]['COMISION'].mean():,.2f}")

print("\n5. ¿Qué ciudad generó el mayor número de ventas cerradas?")
print("Ciudad con mayor numero de ventas cerradas:\n", df[df['ESTADO']=="Cerrado"]['CIUDAD'].value_counts().head(1))

print("\n6. ¿Cuál es el valor total de ventas por ciudad? (usar .groupby())")
print("Valor total de ventas por ciudad:\n",df.groupby('CIUDAD')['VALOR_VENTA'].sum())

print("\n7. ¿Cuáles son los 5 productos más vendidos (por número de registros)?")
print("Productos:\n",df['PRODUCTO'].value_counts().head(5))

print("\n8. ¿Cuántos productos únicos fueron vendidos?")
print("Cantidad de produtos:",df['PRODUCTO'].nunique())

print("\n9. ¿Cuál es el vendedor con mayor número de ventas cerradas?")
print(df[df['ESTADO']=='Cerrado']['VENDEDOR'].value_counts().head(1))

print(("\n10. ¿Cuál es la venta con el mayor valor y qué cliente la realizó?"))
print("Venta de mayor valor:\n",df[df['ESTADO']=='Cerrado'][['VALOR_VENTA', 'VENDEDOR']].max())

print("\n11. ¿Existen ventas con valor o comisión nula o negativa? (usar filtros)")
print("Ventas o comisiones negativas o nulas:", "Si Existen" if not df[(df['VALOR_VENTA'] <= 0) | (df['COMISION'] <= 0)].empty else "No Existen")

print("\n12. ¿Cuál es la media de ventas por mes? (usar .dt.month)")
df['FECHA'] = pd.to_datetime(df['FECHA'])
print("Ventas por mes:\n",df.groupby([df['FECHA'].dt.month_name()])['VALOR_VENTA'].mean())

print("\n13. ¿Cuál fue el mes con más ventas cerradas?")
print("Mes con mas ventas cerradas:\n",df[df['ESTADO']=='Cerrado']['FECHA'].dt.month_name().value_counts().head(1))

print("\n14. ¿Cuántas ventas se realizaron en cada trimestre del año?")
print("Ventas por trimestre:\n",df.groupby(df['FECHA'].dt.quarter)['VALOR_VENTA'].count())

print("\n15. ¿Qué productos han sido vendidos en más de 3 ciudades diferentes?")
print("Productos mas vendidos en mas de 3 ciuadades:\n",df.groupby('PRODUCTO')['CIUDAD'].nunique()[lambda x: x>3])

print("\n16. ¿Existen duplicados en los datos? ¿Cómo los identificarías?")
print("Existen duplicados:",df.duplicated().sum(), "registros")
print("Registros duplicados","No hay registros duplicados" if not df.duplicated().empty else df[df.duplicated()])

print("\n17. Eliminar las filas que tengan valores nulos en columnas clave (CLIENTE, PRODUCTO, VALOR_VENTA).")
df_eliminar = df.dropna(subset=['CLIENTE', 'PRODUCTO', 'VALOR_VENTA'])
print("Registros despues de limpiar campos nulos:", len(df_eliminar))

print("\n18. Crear una nueva columna llamada UTILIDAD que sea igual al 95% del VALOR_VENTA (simulando costo), y analizar cuál producto dejó mayor utilidad total.")
df['UTILIDAD'] = df['VALOR_VENTA'] * 0.95
df_MayorUtilidad = df.groupby('PRODUCTO')['UTILIDAD'].sum().sort_values(ascending = False).head(1)
producto = df_MayorUtilidad.index[0]
utilidad = df_MayorUtilidad.iloc[0]
print(f"Producto con mayor utilidad:\n{producto}, Utilidad total: ${utilidad:,.2f}")

#Preguntas con groupby
print("")
print("PREGUNTAS con groupby()".center(70," "))

print("\n¿Cuál es el valor total de ventas por ciudad?")
print("Valor total de ventas por ciudades:\n",df.groupby('CIUDAD')['VALOR_VENTA'].sum())

print("\n¿Cuál es el promedio de comisión por vendedor?")
print("Promedio de comision por vendedor:\n",df.groupby('VENDEDOR')['COMISION'].mean())

print("\n¿Cuál es el número de ventas por estado y por ciudad?")
print("Numero de ventas por estado y por ciudad:\n",df.groupby(['ESTADO', 'CIUDAD'])['VALOR_VENTA'].count())

print("\n¿Qué categoría de producto tiene el mayor valor de ventas?")
print("Categoria de producto con mayor valor de ventas:",df.groupby('CATEGORIA')['VALOR_VENTA'].sum().sort_values(ascending=False).head(1))

print("\n¿Cuál es el total de ventas mensuales por ciudad? (requiere convertir fecha a datetime y agrupar)")
print("\nTotal de ventas mensuales por ciudad:\n", df.groupby([df["FECHA"].dt.to_period("M"), "CIUDAD"])["VALOR_VENTA"].sum())

print("\n¿Cuántas ventas cerradas hizo cada vendedor por ciudad?")
print("\nVentas cerradas por vendedor y ciudad:\n",df[df["ESTADO"]=="Cerrado"].groupby(["VENDEDOR","CIUDAD"])["VALOR_VENTA"].count())
