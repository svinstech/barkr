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
            return {
                "status": 401,
                "body": "API not authorized! Any key will do."
            }
        elif "address" not in record or "dates" not in record or "species_guess" not in record:
            return {
                "status": 400,
                "body": "Record #{id} rejected; required field(s) not found.".format(id=record.get("id"))
            }
        elif record["species_guess"] != "Coyote":
            return {
                "status": 400,
                "body": "Record #{id} rejected; coyotes only, please!".format(id=record.get("id"))
            }
        else:
            print("Record #{id} received! Thank you!".format(id=record.get("id")))
            return {
                "status": 200,
                "body": "Success!"
            }
