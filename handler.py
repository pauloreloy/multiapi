
import json
from classes.APIClient import APIClient

if __name__ == "__main__":
    api = APIClient("cep")
    data = {
        "cep": "13025085",
        "format": "json"
    }
    
    api.format_endpoint(data)
    try:
        api_response = api.call_endpoint()
        if(api_response.status_code == 200):
            api_data = api_response.json()
            print(json.dumps(api_data, indent=4))
    except Exception:
        print(api_response)
   
    

