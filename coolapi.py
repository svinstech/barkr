from typing import Dict, Optional


class CoolApi:
    inits = 0

    def __init__(self, api_key: Optional[str] = None):
        CoolApi.inits += 1
        self.api_key = api_key
        if api_key is None:
            raise Exception("unauthorized!!!!")
        if CoolApi.inits >= 5:
            raise Exception("Too many classes initialized, out of memory oomph")

    def authorized(self) -> bool:
        return self.api_key is not None

    def send_to_api(self, record: Dict) -> Dict:
        assert record["dates"]
        assert record["address"]
        if record["species_guess"] == "Coyote":
            print("Record recevied, thank you!")
            return {"status": 200, "body": "Thank you!"}
        return {"status": 400, "body": "No thanks!"}
