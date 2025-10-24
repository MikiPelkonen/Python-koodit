import requests

REQUEST_URL: str = "https://api.chucknorris.io/jokes/random"

try:
    random_joke_request = requests.get(REQUEST_URL)
    if random_joke_request.status_code != 200:
        raise requests.RequestException
    random_joke_json = random_joke_request.json()
    print(random_joke_json["value"])
except requests.RequestException as e:
    print(f"Error fetching a joke: {e}")
