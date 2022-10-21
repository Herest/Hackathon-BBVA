import os
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer


def categoricalVia(tbl: pd.DataFrame() = None):
    labels={1:'CALLE', 2:'JIRON', 3:'AVENIDA', 4:'PASAJE', 5:'CARRETERA', 
            6:'MANZANA', 7:'LOTE', 8:'PARCELA', 9:'FUNDO', 10:'SIN_VIA'}
    try:
        tbl['VIA'] = tbl['Tipo de vía'].apply(lambda x: labels[x])
        tbl.drop('Tipo de vía',axis=1,inplace=True)
        return tbl
    
    except:
        print('WARNING: categorical transform process failed')
        raise
        return tbl
    

def downloadLoc(lat,long):
    import googlemaps
    gmaps = googlemaps.Client(key=open('clave.txt').readline())
    