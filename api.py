
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import RootModel
from fastapi.responses import JSONResponse,HTMLResponse
import pandas as pd
import joblib

class WeatherData(RootModel[dict]):
    pass

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("weather_predict.pkl")

@app.post("/predict")
def predict(data: WeatherData):
    input_df = pd.DataFrame([data.root])
    pred = model.predict(input_df)[0]
    return JSONResponse(
        content={"result": "Rain" if pred == 1 else "No Rain"}
    )


@app.get('/',response_class=HTMLResponse)
def home():
    with open('index.html','r') as f:
        return f.read()

