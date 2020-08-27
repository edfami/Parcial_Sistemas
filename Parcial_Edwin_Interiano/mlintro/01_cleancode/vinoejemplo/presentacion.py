import pandas as pd 
from reglas import operacion_vy
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

Alcohol = operacion(listado[0],df. alcohol)
PH = operacion(listado[1], df.pH)
Residual_Sugar = operacion(listado[2], df.residual_sugar)
Citric_acid = operacion(listado[3], df.citric_acid)





