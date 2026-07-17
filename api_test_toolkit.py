import requests



def fetch_data(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    

def fetch_status(url):
    response = requests.get(url)
    return response.status_code


def send_data(url, payload):
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()
