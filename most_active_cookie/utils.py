import argparse

from typing import Tuple

from .date import Date
from .date import Time
from .date import SECONDS_PER_MINUTE
from .date import MINUTES_PER_HOUR


def parse_args() -> Tuple[str, str]:
    """
    Parses the CLI args and returns a tuple of
    (filename, date), both as strings.

    Prints the help message and exits if the arguments are incorrect.
    """
    parser = argparse.ArgumentParser(
        prog="most_active_cookie",
        description="This script finds the most active cookie(s) for a day",
    )

    parser.add_argument(
        "filename",
        help="Path to log file with cookies and timestamps"
    )

    parser.add_argument(
        "-d",
        "--date",
        required=True,
        help="Date in yyyy-mm-dd form with which to filer cookies",
    )

    args = parser.parse_args()

    return args.filename, args.date


def parse_date(date: str) -> Date:
    """
    Parses the given yyyy-mm-dd str into a
    Date object
    """
    year, month, day = date.split("-")
    return Date(int(year), int(month), int(day))


def parse_datetime(utc_str: str) -> Tuple[Date, Time]:
    """
    Parses the given utc string into the corresponding calendar
    date and time, returned as a tuple

    Raises value error if date or time are invalid.
    """
    date, utc = utc_str.split("T")
    date = parse_date(date)

    delim, offset = ("+", 1) if "+" in utc else ("-", -1)

    timestamp, utc_offset = utc.split(delim)
    time = Time(
        total_seconds=to_seconds(*timestamp.split(":")),
        utc_offset=to_minutes(*utc_offset.split(":")) * offset,
    )

    return date, time


def to_minutes(hours: str, minutes: str) -> int:
    """
    Converts hours, minutes to total minutes
    """
    hours, minutes = int(hours), int(minutes)
    return hours * MINUTES_PER_HOUR + minutes


def to_seconds(hours: str, minutes: str, seconds: str = "0") -> int:
    """
    Converts hours, minutes[, seconds] to total seconds
    """
    hours, minutes, seconds = int(hours), int(minutes), int(seconds)
    return (
        hours * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
        + minutes * SECONDS_PER_MINUTE
        + seconds
    )
