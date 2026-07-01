import sys

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Literal, Annotated

from src.exception import CustomException
from src.logger import get_logger
from src.pipeline.prediction_pipeline import CustomData, PredictionPipeline

logger = get_logger(__name__)

app = FastAPI(title="Insurance Premium Category Predictor")

prediction_pipeline = PredictionPipeline()


class UserInput(BaseModel):
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the user")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user")]
    height: Annotated[float, Field(..., gt=0, lt=2.5, description="Height of the user")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Annual salary of the user in lpa")]
    smoker: Annotated[bool, Field(..., description="Is user a smoker")]
    city: Annotated[str, Field(..., description="The city that the user belongs to")]
    occupation: Annotated[
        Literal[
            "retired",
            "freelancer",
            "student",
            "government_job",
            "business_owner",
            "unemployed",
            "private_job",
        ],
        Field(..., description="Occupation of the user"),
    ]


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Insurance Premium Predictor API is running"}


@app.post("/predict")
def predict_premium(data: UserInput):
    try:
        custom_data = CustomData(
            age=data.age,
            weight=data.weight,
            height=data.height,
            income_lpa=data.income_lpa,
            smoker=data.smoker,
            city=data.city,
            occupation=data.occupation,
        )

        features_df = custom_data.get_data_as_data_frame()

        prediction = prediction_pipeline.predict(features_df)

        return JSONResponse(status_code=200, content={"predicted_category": prediction})

    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise CustomException(e, sys)
