from most_active_cookie.utils import parse_date
from most_active_cookie.utils import parse_datetime
from most_active_cookie.date import Date
from most_active_cookie.date import Time
from most_active_cookie.date import MINUTES_PER_HOUR
from most_active_cookie.date import SECONDS_PER_MINUTE


def test_parse_date():
    for year in range(2000, 2050):
        for month in range(1, 13):
            for day in range(1, 15):
                assert parse_date(f"{year}-{month}-{day}") == \
                       Date(year, month, day)


def test_parse_datetime():
    year, month, day = 2000, 1, 1
    for hour in range(24):
        for minute in range(0, 59, 10):
            for second in range(0, 59, 10):
                for offset in range(-23, 23):
                    delim = "+" if offset >= 0 else "-"
                    utc = f"{year}-{month}-{day}T{hour:02d}:{minute:02d}:{second:02d}{delim}{abs(offset):02d}:00"  # noqa E510

                    _, time = parse_datetime(utc)

                    assert time == Time(
                        hour * MINUTES_PER_HOUR * SECONDS_PER_MINUTE
                        + minute * SECONDS_PER_MINUTE
                        + second,
                        offset * MINUTES_PER_HOUR,
                    )
