
import geopy
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer



def get_zipcode(df, geolocator, lat_field, lon_field):
    location = geolocator.reverse((df[lat_field], df[lon_field]))
    return location.raw['address']['postcode']



def categoricalVia(tbl: pd.DataFrame() = None):
    labels={'1':'CALLE', '2':'JIRON', '3':'AVENIDA', '4':'PASAJE', 
            '5':'CARRETERA', '6':'MANZANA', '7':'LOTE', '8':'PARCELA', 
            '9':'FUNDO', '10':'SIN_VIA'}
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
    call=gmaps.places_nearby((lat,long), radius=1000,keyword=loc)
    #    locs[loc]=len(call['results'])
    return len(call['results'])

    
    