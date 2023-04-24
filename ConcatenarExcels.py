import pandas as pd

# Leo los archivos excel.
df1 = pd.read_excel('datos\Planilla de Horas - Coordinador A.xlsx')
df2 = pd.read_excel('datos\Planilla de Horas - Coordinador B.xlsx')
df3 = pd.read_excel('datos\Planilla de Horas - Coordinador C.xlsx')
df4 = pd.read_excel('datos\Planilla de Horas - Coordinador D.xlsx')

# Los concateno.
df_concatenado = pd.concat([df1, df2, df3, df4])

# Escribo el dataframe concatenado en un nuevo archivo de Excel
df_concatenado.to_excel('concatenado.xlsx', index=False)
