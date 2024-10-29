from cnnClassifier.config.configurations import ConfigurationManager
from cnnClassifier import logger
from cnnClassifier.components.model_evaluation import Evaluation
import dagshub

STAGE_NAME = "Model evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config_manager = ConfigurationManager()
        evaluation_config = config_manager.get_evaluation_config()
        evalu = Evaluation(evaluation_config)
        evalu.evaluation()
        evalu.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")

        dagshub.init(
            repo_owner="namant",
            repo_name="Kidney-Disease-Classification-with-MLFlow-and-DVC",
            mlflow=True,
        )

        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
