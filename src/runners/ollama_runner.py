from typing import Optional, Tuple
from fmeval.constants import MIME_TYPE_JSON
from fmeval.model_runners.model_runner import ModelRunner
import logging
import ollama
from ollama._types import Options

from runners.templates import OPUS_TEMPLATE

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OllamaRunner(ModelRunner):
    def __init__(self):
        print("OllamaRunner initialized")

    def base_predict(
        self, question: str, template: str
    ) -> Tuple[Optional[str], Optional[float]]:
        template = template.format(question=question)
        res = ollama.chat(
            model="mistral:instruct",
            messages=[{"role": "user", "content": template}],
            options=Options(temperature=0.2, top_k=50),
        )
        return res["message"]["content"], None

    def predict(self, prompt: str) -> Tuple[Optional[str], Optional[float]]:
        return self.base_predict(prompt, OPUS_TEMPLATE)
