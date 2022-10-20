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

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
log = logging.getLogger(__name__)

cols=['Fecha de entrega', 'Tipo de vía', 'Piso o nivel', 'Departamento',
      'Provincia', 'Distrito', 'Número de estacionamientos',
      'Número de depósitos', 'Latitud (Decimal)', 'Longitud (Decimal)',
      'Categoría del bien', 'Posición', 'Número de frentes', 'Edad', 'Elevador',
      'Estado de conservación:', 'Método Representado',
      'Moneda Principal para cálculos', 'ÁREA del Terreno',
      'ÁREA de Edificación', 'Valor Comercial']

types={'Fecha de entrega':str, 'Tipo de vía':str, 
       'Piso o nivel':np.float64,'Departamento':str,'Provincia':str,
       'Distrito':str, 'Número de estacionamientos':np.float64,
       'Número de depósitos':np.float64,'Latitud (Decimal)':np.float64,
       'Longitud (Decimal)':np.float64,'Categoría del bien':str,
       'Posición':str, 'Número de frentes':np.float64, 'Edad':np.float64,
       'Elevador':np.float64,'Estado de conservación:':str,
       'Método Representado':str, 'Moneda Principal para cálculos':str,
       'ÁREA del Terreno':np.float64, 'ÁREA de Edificación':np.float64,
       'Valor Comercial':np.float64}

class dataReader:
    def _read_xlsx(self, file):
        log.info('Input format is Excel Spreadsheet.')
        return pd.read_excel(file,dtype=types)


    def _read_csv(self, file):
        log.info('Input format is Comma Separated Values file')
        return pd.read_csv(file,dtype=types)


    def _read_tsv(self, file):
        log.info('Input format is Tab Separated Values file')
        return pd.read_csv(file,dtype=types,sep='\t')



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
