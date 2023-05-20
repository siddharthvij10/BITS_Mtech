import json
import joblib
import pandas as pd
import os
from sklearn.preprocessing import PowerTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


def init():
    global kmeans
    kmeans = joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/kmeans.joblib"))
    global enc
    enc = joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/enc.bin"))
    global taxi_demand_prediction
    taxi_demand_prediction=joblib.load(os.path.join(os.getenv("AZUREML_MODEL_DIR"), "model_artifacts/taxi_demand_prediction.joblib"))


def run(data):
    test = json.loads(data)
    df_predict = pd.Series(test).to_frame().T
    tpep_pickup_datetime = df_predict['tpep_pickup_datetime'].iloc[0]
    df_predict = df_predict.drop("tpep_pickup_datetime", axis=1)

    df_predict['cluster_label'] = kmeans.predict(df_predict)  
    
    df_predict.insert(loc = 0, column = 'tpep_pickup_datetime',value = [tpep_pickup_datetime]) 
    df_predict["tpep_pickup_datetime"] = df_predict["tpep_pickup_datetime"].apply(pd.to_datetime)
    df_predict['pickup_hour'] = df_predict["tpep_pickup_datetime"].dt.hour
    df_predict['pickup_dayofweek'] = df_predict["tpep_pickup_datetime"].dt.dayofweek

    cat_columns = ['pickup_dayofweek', 'pickup_hour', 'cluster_label']
    datastruct_predict_encoded = enc.transform(df_predict[cat_columns]).toarray()  
    df_predict_encoded_df = pd.DataFrame(datastruct_predict_encoded, columns=enc.get_feature_names_out(cat_columns))
    df_predict_model = pd.concat([df_predict.reset_index(), df_predict_encoded_df], axis=1).drop(['index'], axis=1)

    df_predict_model = df_predict_model.drop(cat_columns, axis=1)
    df_predict_model = df_predict_model.drop(["pickup_latitude", "pickup_longitude" , "tpep_pickup_datetime"], axis=1)
    
    df_predict_model[df_predict_model.columns] = df_predict_model[df_predict_model.columns].astype(int)

    prediction = taxi_demand_prediction.predict(df_predict_model)
    prediction = round(prediction[0]*100, 2)
    return "demand percent is {}".format(prediction)