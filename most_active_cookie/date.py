from dataclasses import dataclass


SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24


@dataclass
class Time:
    """
    This class holds a date-agnostic time of day,
    specified by time since midnight and utc offset.

    It enforces that the time specified is less than one
    full day after midnight, and that the utc offset
    is not >= 24 hours. No support for daylight savings time.
    """

    total_seconds: int  # seconds past midnight
    utc_offset: int  # utc offset in minutes

    def __post_init__(self):
        if (
            self.total_seconds < 0
            or self.total_seconds
            > SECONDS_PER_MINUTE * MINUTES_PER_HOUR * HOURS_PER_DAY
        ):
            raise ValueError("Invalid time specified")

        if abs(self.utc_offset) / MINUTES_PER_HOUR >= HOURS_PER_DAY:
            print(abs(self.utc_offset) / MINUTES_PER_HOUR, self.utc_offset)
            raise ValueError("Invalid UTC offset specified")

    def hours(self) -> int:
        """
        Returns the number of whole hours since midnight without
        considering utc offset
        """
        return self.total_seconds // (MINUTES_PER_HOUR * SECONDS_PER_MINUTE)

    def minutes(self) -> int:
        """
        Returns the number of whole minutes since the last whole hour
        without considering utc offset
        """
        return (self.total_seconds // SECONDS_PER_MINUTE) % MINUTES_PER_HOUR

    def seconds(self) -> int:
        """
        Returns the number of seconds since the last whole minute
        without considering utc offset
        """
        return self.total_seconds % SECONDS_PER_MINUTE


@dataclass
class Date:
    """
    This class holds a single time-agnostic data
    (year, month, day)

    It has no restrictions on years, requires months to be
    in [1, 12], and days to be a valid day for that month

    For best results, use only with standard date conventions.
    For more robust uses (e.g. Gregorian calendar discontinuities), see
    https://docs.python.org/3/library/datetime.html
    """

    year: int
    month: int
    day: int

    def __post_init__(self):
        if self.month < 1 or self.month > 12:
            raise ValueError("Months must be between 1 and 12")

        if self.month == 2:
            if self.year % 4 == 0:
                max_days = 29
            else:
                max_days = 28
        elif self.month in [1, 3, 5, 7, 8, 10, 12]:
            max_days = 30
        else:
            max_days = 31

        if self.day < 1 or self.day > max_days:
            raise ValueError("Days must be valid for given month")
