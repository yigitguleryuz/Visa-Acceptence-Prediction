import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import pickle
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

# HTML için
templates = Jinja2Templates(directory="templates")
with open('visa_load.pkl', 'rb') as model_file:
    saved_data = pickle.load(model_file)
    model = saved_data['model']
    encoders = saved_data['encoders']
    scaler = saved_data['scaler']

# Veritabanını yükle (EDA için)
df = pd.read_csv('visa.csv', sep=';', index_col='UserID')


class VisaFeatures(BaseModel):
    Age: int
    Occupation: str
    AnnualIncome_TRY: int
    TravelHistoryScore: int
    TargetCountry: str
    VisaType: str


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
async def predict(features: VisaFeatures):

    input_df = pd.DataFrame([features.model_dump()])

    input_encoded = encoders.transform(input_df)
    input_scaled = scaler.transform(input_encoded)

    #HEM PREDICT HEM PREDICT PROBA KULLANILDI

    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1]

    return {
        "prediction": int(prediction[0]),
        "visa_acceptance_rate": f"%{probability * 100:.2f}"
    }

@app.get("/api/country-stats")
async def get_country_stats():
    #Ülkelere göre tahmin
    country_stats = df.groupby('TargetCountry')['IsSuccessful'].agg(['count', 'sum']).reset_index()
    country_stats['success_rate'] = (country_stats['sum'] / country_stats['count'] * 100).round(2)
    country_stats = country_stats.sort_values('success_rate', ascending=False)

    return {
        "labels": country_stats['TargetCountry'].tolist(),
        "success_rates": country_stats['success_rate'].tolist(),
        "counts": country_stats['count'].tolist()
    }