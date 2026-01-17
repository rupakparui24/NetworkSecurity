from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig, DataTransformationconfig, ModelTrainerConfig
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
import sys

if __name__ == '__main__':
    trainingpipelineconfig = TrainingPipelineConfig()
    dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
    dataingestion = DataIngestion(dataingestionconfig)
    logging.info("Stating data ingestion")
    artifact = dataingestion.initiate_data_ingestion()
    print(artifact)
    logging.info("Data Ingestion completed")
    datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
    logging.info("Starting data validation")
    datavalidation = DataValidation(artifact, datavalidationconfig)
    data_validation_artifact = datavalidation.initiate_data_validation()
    logging.info("Data Validation completed")
    print(data_validation_artifact)
    datatransformationconfig = DataTransformationconfig(trainingpipelineconfig)
    logging.info("Starting data transformation")
    datatransformation = DataTransformation(data_validation_artifact, datatransformationconfig)
    data_transformation_artifact = datatransformation.initiate_data_transformation()
    logging.info("Data Transformation completed")
    print(data_transformation_artifact)
    model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
    logging.info("Starting model trainer")
    model_trainer = ModelTrainer(model_trainer_config, data_transformation_artifact)
    model_trainer_artifact = model_trainer.initiate_model_trainer()
    logging.info("Model Trainer completed")
    print(model_trainer_artifact)
