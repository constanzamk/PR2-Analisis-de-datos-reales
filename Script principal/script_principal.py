# -*- coding: utf-8 -*-
"""Script Principal

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fPrDaEFD7l4hc2Xn-CzCZ5TB-gapoI04
"""

import pandas as pd

#Creando Dataframe del dataset
ruta_calidad='https://drive.google.com/uc?id=1gUgPXLjbh67UbFIKjqWxZGq7Ds4W_ddV'
df_calidad= pd.read_csv(ruta_calidad, index_col=0)

#Detallando índice del dataframe
df_calidad.index.name = 'Posición'

#Renombrando columnas
df_calidad.rename(columns = {'Country':'País','Stability(14%)':'Estabilidad',
                             'Rights(15%)':'Derechos','Health(14%)':'Salud','Safety(14%)':'Seguridad',
                             'Climate(14%)':'Clima','Costs(15%)':'Costos','Popularity(14%)':'Popularidad'},
                  inplace = True)
df_calidad

#Revisandoq que el tipo de data en cada columna sea el correcto
df_calidad.info()

#Comprobación de NaN
df_calidad.isnull().values.any()