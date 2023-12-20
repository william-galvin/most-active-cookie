import random
import string

from most_active_cookie.main import get_cookie_counts
from most_active_cookie.date import Date


def test_main_fuzzy():
    lines, targets = get_random_lines()
    for day in range(1, 25):
        date = Date(2000, 1, day)
        counts = get_cookie_counts(lines, date)
        for cookie, count in targets[day]:
            assert count == counts[cookie]


def get_random_lines():
    lines = []
    targets = {}

    for _ in range(10):
        cookie = "".join(
            random.choices(
                string.ascii_lowercase +
                string.ascii_uppercase +
                string.digits,
                k=10
            )
        )
        for day in range(1, 25):
            timestamp = f"2000-1-{day}T00:00:00+00:00"
            count = random.randint(0, 100)
            for _ in range(count):
                lines.append(f"{cookie},{timestamp}")

            if day not in targets or count > targets[day][0][1]:
                targets[day] = [(cookie, count)]
            elif count == targets[day][0][1]:
                targets[day].append((cookie, count))

    random.shuffle(lines)
    return lines, targets
