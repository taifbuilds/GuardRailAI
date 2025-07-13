import requests


def check_moderation(api_key: str, text: str) -> dict:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {"input": text}
    response = requests.post(
        "https://api.openai.com/v1/moderations", headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
