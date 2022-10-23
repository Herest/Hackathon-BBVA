#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 19:57:27 2022

@author: Marco A. Nava-Aguilar (marcoanavaaguilar@gmail.com)
"""
import sys
import logging
import numpy as np
import pandas as pd
from unidecode import unidecode

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

types={'ID':np.float64,'Fecha de entrega':str, 'Tipo de vía':str, 
       'Piso':str,'Departamento':str,'Provincia':str,
       'Distrito':str, 'Número de estacionamiento':str,
       'Depósitos':np.float64,'Latitud (Decimal)':np.float64,
       'Longitud (Decimal)':np.float64,'Categoría del bien':str,
       'Posición':str, 'Número de frentes':np.float64, 'Edad':np.float64,
       'Elevador':np.float64,'Estado de conservación:':str,
       'Método Representado':str,
       'Área Terreno':str, 'Área Construcción':str,
       'Valor comercial(USD)':np.float64}

class dataReader():
    def _read_xlsx(self, file):
        log.info('Input format is Excel Spreadsheet.')
        try:
            df = pd.read_excel(file,dtype=types)
            df.drop(['Posición','Número de frentes'],axis=1,inplace=True)
    
            df['Área Terreno'] =  df['Área Terreno'].apply(lambda x: 
                                                    float(str(x).replace(',','')))
            df['Área Construcción'] = df['Área Construcción'].apply(lambda x: 
                                                    float(str(x).replace(',','')))
                    
            cols=['Departamento','Provincia','Distrito']
            for col in cols:
                 df[col] = df[col].apply(lambda x: unidecode(x))    
                    
            return df
        except Exception as e: 
            print(e)
            print('Algún tipo de dato introducido es incorrecto')


    def _read_csv(self, file):
        log.info('Input format is Comma Separated Values file')
        try:
            df = pd.read_csv(file,dtype=types,encoding='latin-1')
            df.drop(['Posición','Número de frentes'],axis=1,inplace=True)
       
            df['Área Terreno'] =  df['Área Terreno'].apply(lambda x: 
                                                float(str(x).replace(',','')))
            df['Área Construcción'] = df['Área Construcción'].apply(lambda x: 
                                                float(str(x).replace(',','')))                                                           
            cols=['Tipo de vía','Departamento','Provincia','Distrito',
                  'Categoría del bien', 'Método Representado',
                  'Estado de conservación']
            cols=['Departamento','Provincia','Distrito']
            for col in cols:
                df[col] = df[col].apply(lambda x: unidecode(x))    
            return df
        except Exception as e: 
            print(e)
            print('Algún tipo de dato introducido es incorrecto')


    def _read_tsv(self, file):
        log.info('Input format is Tab Separated Values file')
        try:
            df = pd.read_csv(file,dtype=types,sep='\t',encoding='latin-1')
            df.drop(['Posición','Número de frentes'],axis=1,inplace=True)
             
            df['Área Terreno'] =  df['Área Terreno'].apply(lambda x: 
                                                float(str(x).replace(',','')))
            df['Área Construcción'] = df['Área Construcción'].apply(lambda x: 
                                                float(str(x).replace(',','')))
            cols=['Departamento','Provincia','Distrito']
            for col in cols:
                df[col] = df[col].apply(lambda x: unidecode(x))    
                
            return df
        except Exception as e: 
            print(e)
            print('Algún tipo de dato introducido es incorrecto')




    def read_data(self, file):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            G = self._read_xlsx(file)
        elif file.endswith('.csv'):
            G = self._read_csv(file)
        elif file.endswith('.tsv'):
            G = self._read_tsv(file)
        else:
            log.error('Invalid format. Unrecognized file format. Make sure file ends with .xlsx | .xls | .tsv | .csv')
            sys.exit(1)
        return G
