import random
import pandas as pd
import os

# Genera 200 números aleatorios sin repetición entre 1 y 1000 y los ordena
numeros_aleatorios = sorted(random.sample(range(1, 4024), 200))

# Crea un DataFrame con los números aleatorios
df = pd.DataFrame({'NumerosAleatorios': numeros_aleatorios})

# Guarda el DataFrame en un archivo Excel
archivo_excel = 'numeros_aleatorios.xlsx'
df.to_excel(archivo_excel, index=False)

print(f"Números aleatorios exportados a {archivo_excel}")

# Abre el archivo Excel con el programa predeterminado
os.system(f'start excel {archivo_excel}')