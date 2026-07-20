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

def get_required_fields(data, required_fields):
    for field in required_fields:
        if field not in data:
            raise KeyError(f"Missing required field: {field}")
    return {field: data[field] for field in required_fields}

data2 = {"name": "Ahmad", "email": "ahmad@example.com"}
print(get_required_fields(data2, ["name", "email"]))      