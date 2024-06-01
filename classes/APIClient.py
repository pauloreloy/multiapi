import json
import requests

class APIClient:

    def __init__(self, api_type) -> None:
        self.config = self.load_config(api_type)

    @staticmethod
    def load_config(api_type):
        config_file = "config/api.json"
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config[api_type]

    def format_endpoint(self, data):
        for d in data:
            if("$$" in self.config['endpoint']):
                self.config['endpoint'] = self.config['endpoint'].replace("$$"+d, data[d])
        return True
    
    def call_endpoint(self):
        url = f"{self.config['base_url']}{self.config['endpoint']}"
        try:
            response = requests.get(url)
            return response
        except requests.exceptions.RequestException as e:
            return e