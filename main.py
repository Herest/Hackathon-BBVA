#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 08:36:44 2022

@author: herestkamah
"""

import pickle
import numpy as np
from func import *
from CleanAge import _Clean_Age
from InsertColumnNew import _insert_Ubigeo_, _get_Ubigeo
from dataReader import dataReader
import pandas.api.types as ptypes

dataReader=dataReader()
df=dataReader.read_data('~/Downloads/data_test_final_equipos_consolidado.xlsx')


ID=df['ID']
df=_insert_Ubigeo_(df)
df=_CleanAge(df)
df['Tipo de vía']=df['Tipo de vía'].astype(str)
df=categoricalVia(df)

df=df[['VIA', 'Ubigeo', 'Número de estacionamiento', 'Depósitos',
       'Latitud (Decimal)', 'Longitud (Decimal)', 'Categoría del bien',
       'Estado de conservación', 'Edad', 'Método Representado',
       'Área Terreno', 'Área Construcción']]


for col in ['VIA','Categoría del bien','Estado de conservación','Método Representado']:
    df=pd.concat([df,pd.get_dummies(df[col])],axis=1)
    df.drop(col,axis=1,inplace=True)


pickled_model = pickle.load(open('model6_52.pkl', 'rb'))
pred=pickled_model.predict(df)
output=pd.concat([ID,pd.Series(pred,name='Valor comercial(USD)',dtype=int]),
                  axis=1)
output.to_csv('output.csv',encoding='latin-1', index=False)                  

