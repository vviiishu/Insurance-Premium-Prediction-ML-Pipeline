import os
import sys
from dataclasses import dataclass

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from src.exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)

TIER_1_CITIES = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
TIER_2_CITIES = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri",
]


def get_age_group(age: int) -> str:
    if age < 25:
        return "young"
    elif age < 45:
        return "adult"
    elif age < 60:
        return "middle_aged"
    return "senior"


def get_lifestyle_risk(row) -> str:
    if row["smoker"] and row["bmi"] > 30:
        return "high"
    elif row["smoker"] or row["bmi"] > 27:
        return "medium"
    else:
        return "low"


def get_city_tier(city: str) -> int:
    if city in TIER_1_CITIES:
        return 1
    elif city in TIER_2_CITIES:
        return 2
    else:
        return 3


@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path: str = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

        self.categorical_features = ["age_group", "lifestyle_risk", "occupation", "city_tier"]
        self.numeric_features = ["bmi", "income_lpa"]
        self.target_column = "insurance_premium_category"

    def get_data_transformer_object(self) -> ColumnTransformer:
        """Builds the ColumnTransformer used to preprocess engineered features."""
        try:
            preprocessor = ColumnTransformer(
                transformers=[
                    ("cat", OneHotEncoder(handle_unknown="ignore"), self.categorical_features),
                    ("num", "passthrough", self.numeric_features),
                ]
            )
            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def engineer_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Derives bmi, age_group, lifestyle_risk and city_tier from raw columns."""
        try:
            df = df.copy()
            df["bmi"] = df["weight"] / (df["height"] ** 2)
            df["age_group"] = df["age"].apply(get_age_group)
            df["lifestyle_risk"] = df.apply(get_lifestyle_risk, axis=1)
            df["city_tier"] = df["city"].apply(get_city_tier)
            return df

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path: str, test_path: str):
        """
        Reads train/test csv files and engineers features (bmi, age_group,
        lifestyle_risk, city_tier). The actual encoding (OneHotEncoder) is
        left to the ColumnTransformer, which is fit later as part of the
        full model pipeline in model_trainer.py - this mirrors the original
        notebook, where the full sklearn Pipeline (preprocessor + classifier)
        is trained directly on the engineered feature dataframe so that
        app.py can call model.predict(df) on raw engineered features.

        Returns (X_train, y_train, X_test, y_test, preprocessing_obj).
        """
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logger.info("Read train and test data completed")

            train_df = self.engineer_features(train_df)
            test_df = self.engineer_features(test_df)

            feature_columns = self.categorical_features + self.numeric_features

            X_train = train_df[feature_columns]
            y_train = train_df[self.target_column]

            X_test = test_df[feature_columns]
            y_test = test_df[self.target_column]

            preprocessing_obj = self.get_data_transformer_object()

            logger.info("Feature engineering completed for train and test dataframes")

            return X_train, y_train, X_test, y_test, preprocessing_obj

        except Exception as e:
            raise CustomException(e, sys)
