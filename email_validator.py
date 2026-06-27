import requests

class EmailValidator:
    def __init__(self, api_key=None):
        # هنا حط رابط الـ Railway بتاعك اللي جربناه وطلع الـ JSON
        self.base_url = "https://public-production-242b.up.railway.app/validate"
        self.api_key = api_key

    def check(self, email):
        headers = {}
        if self.api_key:
            headers["X-API-Key"] = self.api_key
        
        params = {"email": email}
        try:
            response = requests.get(self.base_url, params=params, headers=headers)
            return response.json()
        except Exception as e:
            return {"status": "error", "message": str(e)}
