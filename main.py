from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

try:
    model = joblib.load("model.joblib")
except Exception:
    model = None

class WineFeatures(BaseModel):
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_of_ash: float
    magnesium: float
    total_phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanthocyanins: float
    color_intensity: float
    hue: float
    od280_od315_of_diluted_wines: float
    proline: float

target_names = ['class_0', 'class_1', 'class_2']

@app.get("/")
def read_root():
    return {"message": "ML API is running"}

@app.post("/predict")
def predict(features: WineFeatures):
    if model is None:
        return {"error": "Model not loaded properly"}
        
    input_data = np.array([[
        features.alcohol,
        features.malic_acid,
        features.ash,
        features.alcalinity_of_ash,
        features.magnesium,
        features.total_phenols,
        features.flavanoids,
        features.nonflavanoid_phenols,
        features.proanthocyanins,
        features.color_intensity,
        features.hue,
        features.od280_od315_of_diluted_wines,
        features.proline
    ]])
    
    prediction_idx = model.predict(input_data)[0]
    
    return {
        "prediction": int(prediction_idx),
        "predicted_class": target_names[prediction_idx]
    }
