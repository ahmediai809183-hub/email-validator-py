import requests

class EmailValidator:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = "https://email-validator.lemonsqueezy.com/api/v1/check"

    def check(self, email):
        params = {"email": email}
        if self.api_key:
            params["api_key"] = self.api_key
        
        response = requests.get(self.base_url, params=params)
        return response.json()
