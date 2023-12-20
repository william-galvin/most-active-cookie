import random

import pytest

from most_active_cookie.date import Time
from most_active_cookie.date import Date
from most_active_cookie.date import MINUTES_PER_HOUR
from most_active_cookie.date import SECONDS_PER_MINUTE
from most_active_cookie.date import HOURS_PER_DAY


def test_time_fuzzy():
    for _ in range(10_000):
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)

        time = Time(
            total_seconds=hours * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
            + minutes * SECONDS_PER_MINUTE
            + seconds,
            utc_offset=0,
        )

        assert hours == time.hours()
        assert minutes == time.minutes()
        assert seconds == time.seconds()


def test_time_invalid():
    total = HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE + \
        random.randint(1, 1000)

    with pytest.raises(ValueError) as e:
        Time(total_seconds=total, utc_offset=0)
    assert str(e.value) == "Invalid time specified"


def test_time_utc_invalid():
    for offset in (-24, -25, 24, 25):
        with pytest.raises(ValueError) as e:
            Time(total_seconds=100, utc_offset=offset * MINUTES_PER_HOUR)
        assert str(e.value) == "Invalid UTC offset specified"


def test_date_basic():
    year = 2000
    for month in range(1, 13):
        for day in range(1, 28):
            Date(year, month, day)


def test_date_invalid_month():
    for month in (-1, 0, 13):
        with pytest.raises(ValueError) as e:
            Date(2000, month, 1)
        assert str(e.value) == "Months must be between 1 and 12"


def test_date_february():
    Date(2000, 2, 29)

    with pytest.raises(ValueError) as e:
        Date(2001, 2, 29)
    assert str(e.value) == "Days must be valid for given month"
