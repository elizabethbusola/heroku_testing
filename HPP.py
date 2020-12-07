# Importing Libraries
from fastapi import FastAPI
import uvicorn
import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
import category_encoders as ce
from sklearn.ensemble import RandomForestRegressor, VotingRegressor
from xgboost.sklearn import XGBRegressor 
import joblib

app = FastAPI()

Encode = joblib.load(open('predictHousePricesEncode.pkl', 'rb'))
Scaler = joblib.load(open('PredictHousePricesScaler.pkl', 'rb'))
Ensemble = joblib.load(open('predictHousePricesEnsemble.pkl', 'rb'))

@app.get('/')
async def index():
    return 'Welcome to the House Pricing Prediction App'

#Price Prediction

@app.post('/predict')
def predict_price(Location:str, Locality:str, Type:str, Bedroom:int, Toilet:int, Bathroom:int, Estate: str , Parking:int, Year:int):
    #Structuring all inputs into a dictionary

    data = {}
    data['Location'] = Location
    data['Locality'] = Locality
    data['Type'] = Type
    data['Bedrooms'] = Bedroom
    data['Bathrooms'] = Bathroom
    data['Estate'] = Estate
    data['Toilets'] = Toilet
    data['Parking Spaces'] = Parking
    data['Year'] = Year
    #Dictionary to DataFrame
    data1 = pd.DataFrame([data.values()], columns=data.keys())
    data2 = Encode.transform(data1)
    data3 = Scaler.transform(data2)
    Price = Ensemble.predict(data3)
    return {round(Price[0], 2)}
