
#import geopy
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer



def get_zipcode(geolocator, lat_field, lon_field):
    location = geolocator.reverse((lat_field, lon_field))
    return location.raw['address']['postcode']



def categoricalVia(tbl: pd.DataFrame() = None):
    labels={'1.0':'CALLE', '2.0':'JIRON', '3.0':'AVENIDA', '4.0':'PASAJE', 
            '5.0':'CARRETERA', '6.0':'MANZANA', '7.0':'LOTE', '8.0':'PARCELA', 
            '9.0':'FUNDO', '10.0':'SIN_VIA','nan':'nan',
            '1':'CALLE', '2':'JIRON', '3':'AVENIDA', '4':'PASAJE', 
            '5':'CARRETERA', '6':'MANZANA', '7':'LOTE', '8':'PARCELA', 
            '9':'FUNDO', '10':'SIN_VIA','nan':'nan'}
    try:
        tbl['VIA'] = tbl['Tipo de vía'].apply(lambda x: labels[x])
        tbl.drop('Tipo de vía',axis=1,inplace=True)
        return tbl
    
    except:
        print('WARNING: categorical transform process failed')
        raise
        return tbl
    

def downloadLoc(lat,long,loc,gmaps):
    #locaciones=['escuelas','parques','restaurantes','bares','gasolineras']
    #locs={key:0 for key in locaciones}
    #for loc in locaciones:
    try:
        call=gmaps.places_nearby((lat,long), radius=1000,keyword=loc)
    
        return len(call['results'])
    except:
        return 0

