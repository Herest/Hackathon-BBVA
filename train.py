#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:45:20 2022

@author:  Marco A. Nava-Aguilar (marcoanavaaguilar@gmail.com)
"""
import numpy as np
import googlemaps
from func import *
from GetUbigeo import *
from dataReader import dataReader
import pandas.api.types as ptypes

dataReader=dataReader()
df=dataReader.read_data('dataset_tasacion_train_vf.xlsx')

gmaps = googlemaps.Client(key=open('clave.txt').readline())
geolocator = geopy.Nominatim(user_agent="bbvaluate")

locaciones=['escuelas','parques','restaurantes','bares','gasolineras','tiendas']

from sklearn.impute import KNNImputer

objectCols=[col for col in df2.columns if isinstance(col, object)]
floatCols=['Número de estacionamiento','Depósitos','Elevador','Edad']

imputer = KNNImputer()
imputed = imputer.fit_transform(df2[floatCols])    
df2[floatCols] = pd.DataFrame(imputed, columns=floatCols)


