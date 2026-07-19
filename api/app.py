from fastapi import FastAPI
from pydantic import BaseModel, Field, StrictFloat, StrictInt, field_validator
from typing import Annotated, Literal 
import joblib 
from pathlib import Path
import pandas as pd 


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "catboost_pipeline.pkl"

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="Student Health Risk Prediction API",
    description="Predicts the health condition of a student using lifestyle and health parameters.",
    version="1.0.0"
)


class HealthInput(BaseModel):
    sleep_duration: Annotated[StrictFloat,Field(...,ge=0,le=24,description="Average Sleep Duration in hours (0-24).",examples=[5.5,6.5])]
    heart_rate: Annotated[StrictFloat,Field(...,ge=30,le=220,description="Resting heart rate (BPM)",examples=[50,70.5])]
    bmi:Annotated[StrictFloat,Field(...,ge=10,le=60,description="Body Mass Index",examples=[20.5,30])]
    calorie_expenditure: Annotated[StrictFloat,Field(...,ge=0,description="Calories burned per day",examples=[500.4,700,900])]
    step_count: Annotated[StrictInt,Field(ge=0,description="Daily steps",examples=[5000,3000])] | None = None
    exercise_duration: Annotated[StrictInt,Field(ge=0,le=300,description="Exercise duration in minutes",examples=[120,65])] | None = None
    water_intake: Annotated[StrictFloat,Field(...,ge=0,le=10,description="Daily water Intake in Liters",examples=[4,5])]
    diet_type: Literal["veg", "non-veg", "balanced"]
    stress_level: Literal["low", "medium", "high"]
    sleep_quality: Literal["poor", "good"]
    physical_activity_level: Literal["sedentary", "moderate", "active"]
    smoking_alcohol: Literal["no", "yes", "occasional"]
    gender: Literal["male", "female", "other"]

    @field_validator(
        "diet_type",
        "stress_level",
        "sleep_quality",
        "physical_activity_level",
        "smoking_alcohol",
        "gender",
        mode="before")
    @classmethod
    def normalize_strings(cls,value):
        if isinstance(value,str):
            return value.strip().lower()
        return value

@app.get("/")
def home():
    return {"message": "Student Health Risk Prediction API","docs": "/docs"}

@app.post("/predict")
def predict(data: HealthInput):

    df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(df)
    probability = model.predict_proba(df)

    # Convert NumPy array/list to Python string
    prediction = prediction.squeeze().item()

    return {
        "prediction": prediction,
        "confidence": float(probability.max())
    }