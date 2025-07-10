import requests
import json
from abc import ABC, abstractmethod


class Adapter(ABC):
    @abstractmethod
    def infer(self, prompt: str) -> str:
        pass

# --- OpenAI Adapter ---


class OpenAIAdapter(Adapter):
    def __init__(self, api_key: str, endpoint: str = "https://api.openai.com/v1/chat/completions", model: str = "gpt-3.5-turbo"):
        self.api_key = api_key
        self.endpoint = endpoint
        self.model = model

    def infer(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0
        }
        response = requests.post(self.endpoint, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

# --- Hugging Face Adapter ---


class HuggingFaceAdapter(Adapter):
    def __init__(self, api_key: str, model_url: str):
        self.api_key = api_key
        self.model_url = model_url

    def infer(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {"inputs": prompt}
        response = requests.post(self.model_url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        # Hugging Face returns list of dicts or single dict depending on model type
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        else:
            return json.dumps(data)  # fallback raw output

# --- Adapter Factory ---


def get_adapter(type_: str, api_key: str, endpoint: str) -> Adapter:
    if type_ == "openai":
        return OpenAIAdapter(api_key=api_key, endpoint=endpoint)
    elif type_ == "huggingface":
        return HuggingFaceAdapter(api_key=api_key, model_url=endpoint)
    else:
        raise ValueError(f"Unsupported adapter type: {type_}")
