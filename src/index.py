import os
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
from utils import csv_to_jsonl, jsonl_to_csv
import dotenv
from dotenv import load_dotenv
import re
from runners.ollama_runner import OllamaRunner
from runners.robco_runner import RobcoRunner
from runners.bedrock_runner import BedrockRunner

import re
from utils import combine_from_folder
from fmeval.model_runners.model_runner import ModelRunner


def classification_converter(input: str, labels: list[str]) -> str:
    matches = re.findall("<intention>(.*?)</intention>", input)
    if len(matches) == 0:
        return "irrelevant"
    else:
        for match in matches:
            if match in labels:
                return match
    return "irrelevant"


def run_test(runner: ModelRunner, config: DataConfig = None) -> None:

    valid_labels = [
        "irrelevant",
        "pii",
        "dqgeneral",
        "greeting",
        "redirection",
        "contact",
    ]

    algos: list[EvalAlgorithmInterface] = [
        # QAAccuracy(QAAccuracyConfig()),
        ClassificationAccuracy(
            ClassificationAccuracyConfig(
                valid_labels=valid_labels,
                converter_fn=classification_converter,
            )
        ),
    ]

    for algo in algos:
        res = algo.evaluate(
            model=runner,
            save=True,
            dataset_config=config,
            num_records=1000,
        )
        print(res)


def main():
    load_dotenv()
    os.environ["EVAL_RESULTS_PATH"] = "./src/results"
    os.environ["PARALLELIZATION_FACTOR"] = "18"
    os.environ["WS_THROTTLE"] = "0.2"

    path = "src/data/working_dataset_with_intent.jsonl"

    # with open(path, "w", encoding="utf8") as f:
    #     f.writelines(combine_from_folder("src/datasets/master_datasets", n=40))
    config = DataConfig(
        dataset_name="ds_with_intent",
        dataset_uri=path,
        dataset_mime_type="application/jsonlines",
        model_input_location="Question",
        target_output_location="Intent",
    )

    ollama_runner = OllamaRunner()
    ws_address = os.environ.get("WS_ADDRESS")
    robco_runner = RobcoRunner(ws_address=ws_address)
    bedrock_runner = BedrockRunner()

    run_test(runner=robco_runner, config=config)


if __name__ == "__main__":
    main()
