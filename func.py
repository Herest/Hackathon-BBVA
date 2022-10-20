import os
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer


def categoricalVia(tbl: pd.DataFrame() = None):
    labels={1:'CALLE', 2:'JIRON', 3:'AVENIDA', 4:'PASAJE', 5:'CARRETERA', 
            6:'MANZANA', 7:'LOTE', 8:'PARCELA', 9:'FUNDO', 10:'SIN_VIA'}
    try:
        tbl['VIA'] = pd.cut(x = tbl['Tipo de vía'],
                                  bins = [0,10,18.5,25,35,40,50,60,1000],
                                  include_lowest=True, 
                                  labels = labels.keys()
                                 )
        tbl['bmi_label'] = pd.cut(\
                                  x = tbl['bmi'],
                                  right=False,
                                  bins = [0,10,18.5,25,35,40,50,60,1000],
                                  include_lowest=True, 
                                  labels = labels.values()
                                 )

        return tbl
    
    except:
        print('WARNING: bmi process failed')
        raise
        return tbl