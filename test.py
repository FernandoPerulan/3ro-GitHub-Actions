print("Hello, World!")

import pandas as pd

df = pd.read_excel("data/ventas.xlsx")
print("Filas:", len(df))
df.to_csv("resultados.csv", index=False)