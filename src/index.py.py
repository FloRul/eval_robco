from fmeval.eval_algorithms.toxicity import Toxicity, ToxicityConfig
from fmeval.eval_algorithms.qa_accuracy import QAAccuracy, QAAccuracyConfig
from fmeval.eval_algorithms.qa_accuracy_semantic_robustness import (
    QAAccuracySemanticRobustness,
    QAAccuracySemanticRobustnessConfig,
)
from fmeval.eval_algorithms.qa_toxicity import QAToxicity, ToxicityConfig
from fmeval.eval_algorithms.classification_accuracy import (
    ClassificationAccuracy,
    ClassificationAccuracyConfig,
)
from fmeval.data_loaders.data_config import DataConfig
from fmeval.eval_algorithms.eval_algorithm import EvalAlgorithmInterface
from robco_runner import RobcoRunner
from utils import csv_to_jsonl, jsonl_to_csv
import dotenv


def classification_converter(input: str, labels: list[str]) -> str:
    # if one of the labels is in the input, return it
    for label in labels:
        if label in input:
            return label
    return ""


def run_test():
    model_runner = RobcoRunner(ws_address=dotenv.dotenv_values().get("WS_ADDRESS"))
    algos: list[EvalAlgorithmInterface] = [
        # Toxicity(ToxicityConfig()),
        QAAccuracy(QAAccuracyConfig()),
        ClassificationAccuracy(
            ClassificationAccuracyConfig(
                valid_labels=["default", "dqdataset", "dqgeneral"],
                converter=classification_converter,
            )
        ),
        # QAToxicity(ToxicityConfig()),
    ]
    config = DataConfig(
        dataset_name="custom_dataset",
        dataset_uri="mcn_test_env_test/test.jsonl",
        dataset_mime_type="application/jsonlines",
        model_input_location="Question",
        model_output_location="generated_answer",
        target_output_location="Reponse",
    )
    for algo in algos:
        res = algo.evaluate(model=model_runner, save=True, dataset_config=config)
        print(res)


def sample_res(prompt: str):
    print("Prompt: ", prompt)
    return RobcoRunner(
        ws_address="wss://qaj2t2uqlj.execute-api.ca-central-1.amazonaws.com/socket/"
    ).predict(prompt)


def main():
    # csv_to_jsonl(
    #     "mcn_test_env_test\working_dataset.csv", "mcn_test_env_test/test.jsonl"
    # )
    # run_test()
    # list files in ./results folder
    # files = os.listdir("mcn_test_env_test/results")
    # for file in files:
    #     jsonl_to_csv(
    #         f"mcn_test_env_test/results/{file}", f"mcn_test_env_test/results/{file}.csv"
    #     )
    res = sample_res("il est jue des donnees pour Laval ?")
    print(res)


if __name__ == "__main__":
    main()
