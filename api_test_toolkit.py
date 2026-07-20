import requests
import os
from dotenv import load_dotenv

load_dotenv()



def get_env_var(name: str) -> str:
    value = os.getenv(name)
    if value is None:
        raise RuntimeError(
              f"Environment variable '{name}' is not set."
            f"Check that your .env file exists and contains it."
        )
    return value

BASE_URL = get_env_var("BASE_URL")

def fetch_data(BASE_URL):
        response = requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    

def fetch_status(BASE_URL):
    response = requests.get(BASE_URL)
    return response.status_code


def send_data(BASE_URL, payload):
    response = requests.post(BASE_URL, json=payload)
    response.raise_for_status()
    return response.json()

def get_required_fields(data, required_fields):
    for field in required_fields:
        if field not in data:
            raise KeyError(f"Missing required field: {field}")
    return {field: data[field] for field in required_fields}
