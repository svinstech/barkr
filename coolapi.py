from typing import Dict, Optional


class CoolApi:
    inits = 0

    def __init__(self, api_key: Optional[str] = None):
        CoolApi.inits += 1
        if CoolApi.inits >= 5:
            raise Exception("ERROR: Too many instances initialized; out of memory!")
        self.api_key = api_key

    def authorized(self) -> bool:
        return self.api_key is not None

    def send_to_api(self, record: Dict) -> Dict:
        if not self.authorized():
            return {"status": 401, "body": "API not authorized! Any key will do."}
        elif not record["address"] or not record["dates"]:
            return {"status": 400, "body": "Record rejected; required fields not found."}
        elif record["species_guess"] != "Coyote":
            return {"status": 400, "body": "Record rejected; coyotes only, please!"}
        else:
            print("Record received! Thank you!")
            return {"status": 200, "body": "Success!"}
