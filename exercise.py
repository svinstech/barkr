import json
import csv
import datetime
from typing import Iterator, Dict, Optional
import coolapi


def utc_time_to_timestamp(date_str: str) -> Optional[float]:
    """
    This function should take a string in the format of
    '2007-07-15 19:00:00 UTC' and return a timestamp
    """

    dt_format = "%Y-%m-%d %H:%M:%S %Z"
    pass


def read_from_csv(input_file: str) -> Iterator[Dict]:
    """
    This function should read a CSV file and return an iterator that returns
    one row at a time as a Dictionary
    """
    with open(input_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return {"Not": "implemented"}


def preprocess(row: Dict) -> Optional[Dict]:
    """Return a *copy* of the row, with:
    Change the `time_observed_at` to a timestamp
    Remove user_id and user_login from the row
    If the Species is a Coyote, return the row, otherwise return nothing
    """
    return None


def transform(row: Dict) -> Dict:
    """Return a *copy* of the row with the following changes:
    Lat/long should be combined into an address object
    created_at/updated_at should be combined into an datesobject
    Example:

    {
        "id": 1234,
        "address": {"latitude": 123, "longitude": 345},
        "dates": {"created_at": 123456.0, "updated_at": 123457.0}
    }

    """
    return {"doesnt": "work"}


def send_to_api(row: Dict) -> int:
    """Return the status code from the API call"""
    api = coolapi.CoolApi()
    status = api.send_to_api(row)
    return 404


if __name__ == "__main__":
    print("Doesn't work please fix!")
