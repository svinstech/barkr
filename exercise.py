from csv import DictReader
from coolapi import CoolApi
from datetime import datetime, timezone
from typing import Iterator, Dict, Optional


def utc_time_to_timestamp(date_str: str) -> Optional[float]:
    """
    Argument: Either:
      -- an empty string (representing a lack of data)
      -- a string of the form "%Y-%m-%d %H:%M:%S %Z" e.g. '2007-07-15 19:00:00 UTC'
    Returns:
      -- If input is an empty string: None
      -- Otherwise: the numerical Unix timestamp, also in UTC
    """
    pass


def read_from_csv(input_file: str) -> Iterator[Dict]:
    """
    Argument: a string representing the path to a CSV file
    Returns: an iterator that yields one row at a time as a dictionary
    """
    pass


def preprocess(row: Dict) -> Optional[Dict]:
    """
    Argument: a dictionary representing a single row of data
    Returns:
      -- If species_guess is 'Coyote': a *copy* of the dictionary with the following changes:
        -- Replace time_observed_at with its numerical timestamp
        -- Remove user_id and user_login
      -- If species_guess is not 'Coyote': None
    """
    pass


def transform(row: Dict) -> Dict:
    """
    Argument: a dictionary representing a single row of data
    Returns: a *copy* of the dictionary with the following changes:
      -- Replace latitude and longitude with a single address object containing both
      -- Replace created_at and updated_at with a single dates object containing both

    Example of new objects:
    {
        "address": {"latitude": 123, "longitude": 345},
        "dates": {"created_at": 123456.0, "updated_at": 123457.0}
    }
    """
    pass


def send_to_api(row: Dict) -> int:
    """
    Argument: a dictionary representing a single row of data
    Returns: the numerical status code from the CoolAPI call
    """
    pass


if __name__ == "__main__":
    # Once the tests work, implement and run this!
    pass
