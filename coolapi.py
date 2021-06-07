from typing import Dict, Optional


class CoolApi:
    inits = 0

    def __init__(self, api_key: Optional[str] = None):
        CoolApi.inits += 1
        self.api_key = api_key
        if api_key is None:
            raise Exception("ERROR: Unauthorized! Any key will do!")
        if CoolApi.inits >= 5:
            raise Exception("ERROR: Too many instances initialized; out of memory!")

    def authorized(self) -> bool:
        return self.api_key is not None

    def send_to_api(self, record: Dict) -> Dict:
        assert record["dates"]
        assert record["address"]
        if record["species_guess"] == "Coyote":
            print("Record received! Thank you!")
            return {"status": 200, "body": "Success!"}
        return {"status": 400, "body": "Oh dear; something's gone wrong."}
