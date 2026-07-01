import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.logger import get_logger
from src.utils import save_object

logger = get_logger(__name__)


@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join("artifacts", "model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, X_train, y_train, X_test, y_test, preprocessing_obj):
        """
        Builds a full sklearn Pipeline (preprocessor + RandomForestClassifier),
        trains it on the engineered feature dataframe, evaluates accuracy on
        the test set, and saves the trained pipeline to artifacts/model.pkl.

        The resulting model.pkl is a complete pipeline that accepts a raw
        engineered feature dataframe (bmi, age_group, lifestyle_risk,
        city_tier, income_lpa, occupation) and returns predictions directly -
        matching what app.py expects.
        """
        try:
            logger.info("Building model pipeline")

            model_pipeline = Pipeline(
                steps=[
                    ("preprocessor", preprocessing_obj),
                    ("classifier", RandomForestClassifier(random_state=42)),
                ]
            )

            logger.info("Training model")
            model_pipeline.fit(X_train, y_train)

            y_pred = model_pipeline.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            logger.info(f"Model trained. Test accuracy: {accuracy}")

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=model_pipeline,
            )

            logger.info(f"Saved trained model to {self.model_trainer_config.trained_model_file_path}")

            return accuracy

        except Exception as e:
            raise CustomException(e, sys)
