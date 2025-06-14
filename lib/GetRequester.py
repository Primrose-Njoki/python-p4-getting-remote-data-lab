import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  

    def load_json(self):
        import json
        response_body = self.get_response_body()
        return json.loads(response_body.decode('utf-8'))