import coolapi
import csv
from datetime import datetime, timezone
from typing import Iterator, Dict, Optional


def utc_time_to_timestamp(date_str: str) -> Optional[float]:
    """
    Argument: Either:
      -- an empty string (representing a lack of data)
      -- a string representing the UTC time in the format of '2007-07-15 19:00:00 UTC'
    Returns:
      -- If input is an empty string: None
      -- Otherwise: the numerical Unix timestamp, also in UTC
    """

    dt_format = "%Y-%m-%d %H:%M:%S %Z"
    return None


def read_from_csv(input_file: str) -> Iterator[Dict]:
    """
    Argument: a string representing the path to a CSV file
    Returns: an iterator that yields one row at a time as a dictionary
    """
    with open(input_file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return None


def preprocess(row: Dict) -> Optional[Dict]:
    """
    Argument: a dictionary representing a single row of data
    Returns:
      -- If species_guess is 'Coyote': a *copy* of the dictionary with the following changes:
        -- Replace time_observed_at with its numerical timestamp
        -- Remove user_id and user_login
      -- If species_guess is not 'Coyote': None
    """
    return None


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
    return None


def send_to_api(row: Dict) -> int:
    """
    Argument: a dictionary representing a single row of data
    Returns: the numerical status code from the CoolAPI call
    """
    return None


if __name__ == "__main__":
    print("If your tests work, please implement and run me!")
