#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 12:45:20 2022

@author:  Marco A. Nava-Aguilar (marcoanavaaguilar@gmail.com)
"""

import googlemaps
from GetUbigeo import *
from dataReader import dataReader

dataReader=dataReader()
df=dataReader.read_data('dataset_tasacion_train_vf.xlsx')

gmaps = googlemaps.Client(key=open('clave.txt').readline())


