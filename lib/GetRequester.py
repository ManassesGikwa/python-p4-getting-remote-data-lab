import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        decoded_response = response_body.decode('utf-8')  # Decode the byte string to UTF-8
        return json.loads(decoded_response) 