from core.config import get_settings
from openai import OpenAI

settings = get_settings()
gpt_client = OpenAI(api_key=settings.OPENAI_API_KEY)


def call_chat(instructions: str, input: str, model: str = "gpt-4o-mini"):
    params = {model: model, input: input}

    if instructions:
        params["instructions"] = instructions

    response = gpt_client.responses.create(**params)

    return response
