#!/usr/bin/env python3

"""
This script finds the most active cookie(s) for a given day

Usage:
```bash
most_active_cookie [file].csv -d [date]
```
"""

from typing import List
from typing import Dict

from .date import Date
from .utils import parse_args
from .utils import parse_date
from .utils import parse_datetime


def get_cookie_counts(
    lines: List[str],
    target_date: Date = None,
    delim: str = ","
) -> Dict[str, int]:
    """
    Given the lines from a csv file where each line is `cookie,timestamp`,
    returns a dictionary mapping each cookie to its number of occurences in
    file. Optionally, if a Date is provided, only cookies matching that date
    are counted.
    """
    counts = {}

    for line in lines:
        cookie, timestamp = line.split(delim)
        date, _time = parse_datetime(timestamp)
        if target_date is None or target_date == date:
            counts[cookie] = counts.get(cookie, 0) + 1

    return counts


def main():
    filename, date_str = parse_args()

    date = parse_date(date_str)
    with open(filename, "r") as f:
        lines = f.readlines()[1:]

    counts = get_cookie_counts(lines, date)
    max_count = max(counts.values())

    for cookie, count in counts.items():
        if count == max_count:
            print(cookie)
