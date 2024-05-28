from typing import Optional, Tuple
from fmeval.constants import MIME_TYPE_JSON
from fmeval.model_runners.model_runner import ModelRunner
import logging
import ollama
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from runners.templates import OPUS_TEMPLATE
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BedrockRunner(ModelRunner):
    def __init__(self):
        print("BedrockRunner initialized")

    def base_predict(
        self, question: str, template: str
    ) -> Tuple[Optional[str], Optional[float]]:
        prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "You are a helpful assistant"),
                ("user", template),
            ]
        )
        llm = ChatBedrock(
            model_id="anthropic.claude-3-haiku-20240307-v1:0",
            model_kwargs={"temperature": 0.8, "max_tokens": 50},
        )
        chain = prompt_template | llm
        res = chain.invoke(HumanMessage(question))
        return res.content, None

    def predict(self, question: str) -> Tuple[Optional[str], Optional[float]]:
        return self.base_predict(question, OPUS_TEMPLATE)
