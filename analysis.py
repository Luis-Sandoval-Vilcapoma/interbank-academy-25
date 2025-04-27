#Importar dependecias 
import pandas as pd

# Cargar el archivo CSV 
df = pd.read_csv("data.csv")

#Verificamos que no haya error de tipeo en los tipos de transacciones
tipos = ['Crédito', 'Débito']

if set(df['tipo']) == set(tipos):
    pass
else:
    print("Error: El archivo contiene más de dos tipos de transacciones") 


#Agrupar por tipo  y sumar los montos de tipo Crédito menos la suma de los montos de tipo Débito
sum = df.groupby('tipo')['monto'].sum()
balance_final = (sum['Crédito'] - sum['Débito'])

# ID y el monto de la transacción con el valor más alto.
max_monto = df.max()
id_max = (df['monto'].idxmax() + 1 )

# Agrupar por tipo y contar el numero de transacciones por tipo
count = df.groupby('tipo')['monto'].count()

print(f'''Reporte de Transacciones 
----------------------------------------------------------
Balance Final:{balance_final:.2f}
Transacción de Mayor Monto: id: {id_max} - {max_monto.monto}
Conteo de Transacciones: Crédito:{count['Crédito']}  Débito:{count['Débito']} ''')