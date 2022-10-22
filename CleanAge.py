import pandas as pd
def _Clean_Age():
    age_row = pd.Series([])
    df_Base_Datos = pd.read_csv("Archivo_año_mes.csv", encoding="latin-1")
    for i in range(df_Base_Datos.shape[0]):
        
        try:
            if 480>int(df_Base_Datos["Edad"][i]):
                #print(int(df_Base_Datos["Edad"][i]))
                age_row[i] = int(df_Base_Datos["Edad"][i])
            else:
                age_row[i] = 2022-int(df_Base_Datos["Edad"][i])
                #print("Hola")
        except: 
            age_row[i] = ""
    df_Base_Datos = df_Base_Datos.drop(labels="Edad", axis=1)
    df_Base_Datos.insert(14,"Edad", age_row)
    df_Base_Datos.to_csv('Archivo_Edad_Limpia.csv', header = True, encoding="latin-1")
_Clean_Age()