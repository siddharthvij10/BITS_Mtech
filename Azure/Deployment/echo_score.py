import json
import joblib
import pandas as pd
import os
from sklearn.preprocessing import PowerTransformer
from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import OneHotEncoder



def init():
    print("This is init")
    global loaded_model
    loaded_model = joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/random_forest_v4.joblib"))
    global power
    power = joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/power.bin"))
    global std_scaler
    std_scaler=joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/std_scaler.bin"))
    global ohe
    ohe=joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/ohe.bin"))
    global WindGustDir_FE
    WindGustDir_FE = joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/WindGustDir_FE.bin"))
    global WindDir9am_FE
    WindDir9am_FE = joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/WindDir9am_FE.bin"))
    global WindDir3pm_FE
    WindDir3pm_FE = joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/WindDir3pm_FE.bin"))
    global Location_FE
    Location_FE = joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/Location_FE.bin"))
    global le  
    le = joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/le.bin"))



def run(data):
    test = json.loads(data)

    df = pd.Series(test).to_frame().T
    skewed_features = ['WindGustSpeed', 'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am']
    df[skewed_features] = power.transform(df[skewed_features])

    cols_for_standardization = ['MinTemp', 'MaxTemp', 'WindGustSpeed','WindSpeed9am', 'WindSpeed3pm','Humidity9am', 'Humidity3pm', 'Pressure9am']
    df[cols_for_standardization] = std_scaler.transform(df[cols_for_standardization])

    # Raintoday (OHE) wasn't working. So, for time being, we removed RainToday column itself from model. TO BE CHECKED

    def freq_encode(df):
        df.loc[:, 'WindGustDir_Freq_Encoded'] = df['WindGustDir'].map(WindGustDir_FE)
        df.loc[:, 'WindDir9am_Freq_Encoded'] = df['WindDir9am'].map(WindDir9am_FE)
        df.loc[:, 'WindDir3pm_Freq_Encoded'] = df['WindDir3pm'].map(WindDir3pm_FE)
        df.loc[:, 'Location_Freq_Encoded'] = df['Location'].map(Location_FE)
        df = df.drop(['WindGustDir', 'WindDir9am', 'WindDir3pm', 'Location', 'Date'], axis=1)
        return df

    df = freq_encode(df)
    
    lst_cols = ['Humidity3pm', 'Pressure9am', 'Humidity9am', 'WindGustSpeed','MaxTemp', 'MinTemp', 'Location_Freq_Encoded', 'WindSpeed3pm','WindSpeed9am','WindGustDir_Freq_Encoded','WindDir3pm_Freq_Encoded',
 'WindDir9am_Freq_Encoded']  

    prediction = loaded_model.predict(df[lst_cols])   
    prediction_category = le.inverse_transform(prediction)

    return f"RainTomorrow is {prediction} which encodes to {prediction_category}"
