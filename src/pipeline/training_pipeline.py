import sys

from src.exception import CustomException
from src.logger import get_logger
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

logger = get_logger(__name__)


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def run_pipeline(self, source_path: str = None):
        """Runs the full training pipeline end to end."""
        try:
            logger.info("Training pipeline started")

            if source_path:
                train_path, test_path = self.data_ingestion.initiate_data_ingestion(source_path)
            else:
                train_path, test_path = self.data_ingestion.initiate_data_ingestion()

            X_train, y_train, X_test, y_test, preprocessing_obj = (
                self.data_transformation.initiate_data_transformation(train_path, test_path)
            )

            accuracy = self.model_trainer.initiate_model_trainer(
                X_train, y_train, X_test, y_test, preprocessing_obj
            )

            logger.info(f"Training pipeline completed. Final test accuracy: {accuracy}")
            print(f"Model training complete. Test accuracy: {accuracy:.4f}")

            return accuracy

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    pipeline = TrainingPipeline()
    pipeline.run_pipeline()
