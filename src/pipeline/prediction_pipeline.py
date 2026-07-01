import os
import sys

import pandas as pd

from src.exception import CustomException
from src.logger import get_logger
from src.utils import load_object
from src.components.data_transformation import (
    get_age_group,
    get_lifestyle_risk,
    get_city_tier,
)

logger = get_logger(__name__)


class CustomData:
    """
    Wraps raw user input (as received from the frontend / API) and exposes
    it as a single-row engineered feature dataframe ready for prediction.
    """

    def __init__(
        self,
        age: int,
        weight: float,
        height: float,
        income_lpa: float,
        smoker: bool,
        city: str,
        occupation: str,
    ):
        self.age = age
        self.weight = weight
        self.height = height
        self.income_lpa = income_lpa
        self.smoker = smoker
        self.city = city
        self.occupation = occupation

    def get_data_as_data_frame(self) -> pd.DataFrame:
        try:
            bmi = self.weight / (self.height ** 2)

            row = {
                "bmi": bmi,
                "age_group": get_age_group(self.age),
                "lifestyle_risk": get_lifestyle_risk({"smoker": self.smoker, "bmi": bmi}),
                "city_tier": get_city_tier(self.city),
                "income_lpa": self.income_lpa,
                "occupation": self.occupation,
            }

            return pd.DataFrame([row])

        except Exception as e:
            raise CustomException(e, sys)


class PredictionPipeline:
    def __init__(self, model_path: str = os.path.join("artifacts", "model.pkl")):
        self.model_path = model_path
        self._model = None

    @property
    def model(self):
        if self._model is None:
            logger.info(f"Loading model from {self.model_path}")
            self._model = load_object(self.model_path)
        return self._model

    def predict(self, features: pd.DataFrame):
        try:
            prediction = self.model.predict(features)
            return prediction[0]

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    data = CustomData(
        age=30,
        weight=65,
        height=1.70,
        income_lpa=10,
        smoker=False,
        city="Mumbai",
        occupation="private_job",
    )
    df = data.get_data_as_data_frame()

    pipeline = PredictionPipeline()
    print(pipeline.predict(df))
