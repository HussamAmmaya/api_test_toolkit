import requests


def fetch_data(url):
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    
        

fetched_data = fetch_data("https://jsonplaceholder.typicode.com/posts/1")
#fetched_data1 = fetch_data("https://jsonplaceholder.typicode.com/posts/9999")

def fetch_status(url):
    response = requests.get(url)
    return response.status_code

status = fetch_status("https://jsonplaceholder.typicode.com/posts/1")
print(status)

status_fail = fetch_status("https://jsonplaceholder.typicode.com/posts/9999")
print(status_fail)

def send_data(url, payload):
    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()

print(send_data("https://jsonplaceholder.typicode.com/posts", {"title": "foo", "body": "bar", "userId": 1}))
