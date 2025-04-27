#Importar dependecias 
import pandas as pd

# Cargar el archivo CSV 
df = pd.read_csv("data.csv")

#Verificamos que no haya error de tipeo en los tipos de transacciones
tipos = ['Crédito', 'Débito']

if set(df['tipo']) == set(tipos):
    pass
else:
    raise ValueError("El archivo contiene más tipos de transacciones de los esperados.")

#Agrupo por tipo  y sumo los montos de tipo Crédito menos la suma de los montos de tipo Débito
sum = df.groupby('tipo')['monto'].sum()
balance_final = (sum['Crédito'] - sum['Débito'])

# Obtengo el monto máximo
max_monto = df['monto'].max()

# Obtengo el id de la transacción con el monto máximo
id_max = df.loc[df['monto'].idxmax(), 'id' ]

# Agrupar por tipo y contar el numero de transacciones por tipo
count = df.groupby('tipo')['monto'].count()

# Imprimir el reporte
print(f'''Reporte de Transacciones 
----------------------------------------------------------
Balance Final:{balance_final:.2f}
Transacción de Mayor Monto: id: {id_max} - {max_monto}
Conteo de Transacciones: Crédito:{count['Crédito']}  Débito:{count['Débito']} ''')