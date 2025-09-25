import requests
from typing import Any, Dict

class HTTPClient:
    def __init__(self, token: str, endpoint: str = "https://api.github.com/graphql"):
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"bearer {token}", "Accept": "application/json"})
        self.endpoint = endpoint

    def post(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        resp = self.session.post(self.endpoint, json=payload, timeout=30)
        resp.raise_for_status()
        return resp.json()
