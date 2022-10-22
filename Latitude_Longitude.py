from cmath import nan
import pandas as pd
import math
def _latitude_Longitude():
    df_Base_Datos = pd.read_csv("Archivo_Edad_Limpia.csv", encoding="latin-1")
    df_Base_Datos2 = pd.read_csv("geodir-ubigeo-inei.csv", encoding="latin-1")
    for i in range(df_Base_Datos.shape[0]):
        #print(df_Base_Datos["Latitud (Decimal)"][i])
        if math.isnan(df_Base_Datos["Latitud (Decimal)"][i]):
            #print("hola")
            linea = df_Base_Datos2.loc[(df_Base_Datos2['Ubigeo']==df_Base_Datos["Ubigeo"][i])]
            df_Base_Datos["Latitud (Decimal)"][i] = float(linea["Y"])
            df_Base_Datos["Longitud (Decimal)"][i] = float(linea["X"])
    df_Base_Datos.to_csv('Archivo_Latitud_Limpia.csv', header = True, encoding="latin-1")
_latitude_Longitude()