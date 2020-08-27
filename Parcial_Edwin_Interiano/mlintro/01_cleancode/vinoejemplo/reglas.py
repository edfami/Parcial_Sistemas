import pandas as pd


df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

listado = [df.alcohol.median(),df.pH.median(),
    df.residual_sugar.median(),df.citric_acid.median()]

def operacion_vy(mediana, columna):
    for i, operacion in enumerate (columna):
        if operacion >= mediana:
            df.loc[i, columna] = 'alto'
        else:
            df.loc[i, columna] = 'bajo'
    listado = df.groupby(operacion).quality.mean()

    print(listado)
    
    return listado





