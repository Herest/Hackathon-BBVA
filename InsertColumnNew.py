# -*- coding: utf-8 -*-
"""InsertColumn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ttDbz9x2ZuGIFeCe87FRPF3LyQuCNEr-
"""

import pandas as pd
def _get_Ubigeo(Departamento, Provincia, Distrito):
  #Departamento=Departamento.upper()
  #Provincia=Provincia.upper()
  #Provincia=Provincia.upper()
  df = pd.read_excel("geodir-ubigeo-inei.xlsx")
  #print(df.head(5))
  #print(df.loc[(df['Departamento']==Departamento)])
  #print(df.loc[(df['Provincia']==Provincia)])
  #print(df.loc[(df['Distrito']==Distrito)])
  try: 
      solucion = df.loc[(df['Departamento']==Departamento)&(df['Provincia']==Provincia)&(df['Distrito']==Distrito)]
      return int(solucion["Ubigeo"])
  except:
      return 0
#_get_Ubigeo("Amazonas", "Chachapoyas", "Chachapoyas")

import pandas as pd
import json

  #hace un diccionario y lo agrega
def _insert_Ubigeo_(df):
  #Aquí cambiar el nombre al de la base de datos
  ubigeo_row = df[['Departamento','Provincia','Distrito']].apply(lambda x:
        _get_Ubigeo(str(x['Departamento']),str(x['Provincia']),str(x['Distrito'])),
        axis=1)
  
  df.insert(6,"Ubigeo", ubigeo_row)
  return df

