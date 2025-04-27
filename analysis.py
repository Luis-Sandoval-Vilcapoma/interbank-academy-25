#Importar dependecias 
import pandas as pd

# Leer el archivo csv
df = pd.read_csv("data.csv")

# Verificar el numero de filas y columnas
print(df.shape)

#Agrupar por tipo  y sumar los montos de tipo Crédito menos la suma de los montos de tipo Débito
sum = df.groupby('tipo')['monto'].sum()
balance_final = (sum['Crédito'] - sum['Débito'])
#print(sum)
print(type(sum))
#print(balance_final)

# ID y el monto de la transacción con el valor más alto.
max_monto = df.max()
id_max = (df['monto'].idxmax() + 1 )

# Agrupar por tipo y contar el numero de transacciones por tipo
count = df.groupby('tipo')['monto'].count()

print(count['Crédito'])

print(f'''Reporte de Transacciones 
----------------------------------------------
Balance Final:{balance_final:.2f}
Transacción de Mayor Monto: id: {id_max} - {max_monto.monto}
Conteo de Transacciones: Crédito:{count['Crédito']}  Débito:{count['Débito']} ''')