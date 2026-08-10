"""A dependency-free AD (Gregorian) <-> BS (Bikram Sambat) date calculator.

The conversion uses a table of actual BS month lengths, not a fixed number of
days.  It supports BS 2000-2100 (AD 1943-2044).
"""

from __future__ import annotations

from datetime import date, timedelta


# Each row is: BS year followed by the 12 month lengths.  The data is based on
# the Apache-2.0 licensed nepali-datetime calendar dataset:
# https://github.com/amitgaru/nepali-datetime
_CALENDAR_ROWS = """
2000 30 32 31 32 31 30 30 30 29 30 29 31
2001 31 31 32 31 31 31 30 29 30 29 30 30
2002 31 31 32 32 31 30 30 29 30 29 30 30
2003 31 32 31 32 31 30 30 30 29 29 30 31
2004 30 32 31 32 31 30 30 30 29 30 29 31
2005 31 31 32 31 31 31 30 29 30 29 30 30
2006 31 31 32 32 31 30 30 29 30 29 30 30
2007 31 32 31 32 31 30 30 30 29 29 30 31
2008 31 31 31 32 31 31 29 30 30 29 29 31
2009 31 31 32 31 31 31 30 29 30 29 30 30
2010 31 31 32 32 31 30 30 29 30 29 30 30
2011 31 32 31 32 31 30 30 30 29 29 30 31
2012 31 31 31 32 31 31 29 30 30 29 30 30
2013 31 31 32 31 31 31 30 29 30 29 30 30
2014 31 31 32 32 31 30 30 29 30 29 30 30
2015 31 32 31 32 31 30 30 30 29 29 30 31
2016 31 31 31 32 31 31 29 30 30 29 30 30
2017 31 31 32 31 31 31 30 29 30 29 30 30
2018 31 32 31 32 31 30 30 29 30 29 30 30
2019 31 32 31 32 31 30 30 30 29 30 29 31
2020 31 31 31 32 31 31 30 29 30 29 30 30
2021 31 31 32 31 31 31 30 29 30 29 30 30
2022 31 32 31 32 31 30 30 30 29 29 30 30
2023 31 32 31 32 31 30 30 30 29 30 29 31
2024 31 31 31 32 31 31 30 29 30 29 30 30
2025 31 31 32 31 31 31 30 29 30 29 30 30
2026 31 32 31 32 31 30 30 30 29 29 30 31
2027 30 32 31 32 31 30 30 30 29 30 29 31
2028 31 31 32 31 31 31 30 29 30 29 30 30
2029 31 31 32 31 32 30 30 29 30 29 30 30
2030 31 32 31 32 31 30 30 30 29 29 30 31
2031 30 32 31 32 31 30 30 30 29 30 29 31
2032 31 31 32 31 31 31 30 29 30 29 30 30
2033 31 31 32 32 31 30 30 29 30 29 30 30
2034 31 32 31 32 31 30 30 30 29 29 30 31
2035 30 32 31 32 31 31 29 30 30 29 29 31
2036 31 31 32 31 31 31 30 29 30 29 30 30
2037 31 31 32 32 31 30 30 29 30 29 30 30
2038 31 32 31 32 31 30 30 30 29 29 30 31
2039 31 31 31 32 31 31 29 30 30 29 30 30
2040 31 31 32 31 31 31 30 29 30 29 30 30
2041 31 31 32 32 31 30 30 29 30 29 30 30
2042 31 32 31 32 31 30 30 30 29 29 30 31
2043 31 31 31 32 31 31 29 30 30 29 30 30
2044 31 31 32 31 31 31 30 29 30 29 30 30
2045 31 32 31 32 31 30 30 29 30 29 30 30
2046 31 32 31 32 31 30 30 30 29 29 30 31
2047 31 31 31 32 31 31 30 29 30 29 30 30
2048 31 31 32 31 31 31 30 29 30 29 30 30
2049 31 32 31 32 31 30 30 30 29 29 30 30
2050 31 32 31 32 31 30 30 30 29 30 29 31
2051 31 31 31 32 31 31 30 29 30 29 30 30
2052 31 31 32 31 31 31 30 29 30 29 30 30
2053 31 32 31 32 31 30 30 30 29 29 30 30
2054 31 32 31 32 31 30 30 30 29 30 29 31
2055 31 31 32 31 31 31 30 29 30 29 30 30
2056 31 31 32 31 32 30 30 29 30 29 30 30
2057 31 32 31 32 31 30 30 30 29 29 30 31
2058 30 32 31 32 31 30 30 30 29 30 29 31
2059 31 31 32 31 31 31 30 29 30 29 30 30
2060 31 31 32 32 31 30 30 29 30 29 30 30
2061 31 32 31 32 31 30 30 30 29 29 30 31
2062 31 31 31 32 31 31 29 30 29 30 29 31
2063 31 31 32 31 31 31 30 29 30 29 30 30
2064 31 31 32 32 31 30 30 29 30 29 30 30
2065 31 32 31 32 31 30 30 30 29 29 30 31
2066 31 31 31 32 31 31 29 30 30 29 29 31
2067 31 31 32 31 31 31 30 29 30 29 30 30
2068 31 31 32 32 31 30 30 29 30 29 30 30
2069 31 32 31 32 31 30 30 30 29 29 30 31
2070 31 31 31 32 31 31 29 30 30 29 30 30
2071 31 31 32 31 31 31 30 29 30 29 30 30
2072 31 32 31 32 31 30 30 29 30 29 30 30
2073 31 32 31 32 31 30 30 30 29 29 30 31
2074 31 31 31 32 31 31 30 29 30 29 30 30
2075 31 31 32 31 31 31 30 29 30 29 30 30
2076 31 32 31 32 31 30 30 30 29 29 30 30
2077 31 32 31 32 31 30 30 30 29 30 29 31
2078 31 31 31 32 31 31 30 29 30 29 30 30
2079 31 31 32 31 31 31 30 29 30 29 30 30
2080 31 32 31 32 31 30 30 30 29 29 30 30
2081 31 32 31 32 31 30 30 30 29 30 29 31
2082 31 31 32 31 31 31 30 29 30 29 30 30
2083 31 31 32 31 31 31 30 29 30 29 30 30
2084 31 31 32 31 31 30 30 30 29 30 30 30
2085 31 32 31 32 30 31 30 30 29 30 30 30
2086 30 32 31 32 31 30 30 30 29 30 30 30
2087 31 31 32 31 31 31 30 29 30 30 30 30
2088 30 31 32 32 30 31 30 30 29 30 30 30
2089 30 32 31 32 31 30 30 30 29 30 30 30
2090 30 32 31 32 31 30 30 30 29 30 30 30
2091 31 31 32 31 31 31 30 30 29 30 30 30
2092 30 31 32 32 31 30 30 30 29 30 30 30
2093 30 32 31 32 31 30 30 30 29 30 30 30
2094 31 31 32 31 31 30 30 30 29 30 30 30
2095 31 31 32 31 31 31 30 29 30 30 30 30
2096 30 31 32 32 31 30 30 29 30 29 30 30
2097 31 32 31 32 31 30 30 30 29 30 30 30
2098 31 31 32 31 31 31 29 30 29 30 29 31
2099 31 31 32 31 31 31 30 29 29 30 30 30
2100 31 32 31 32 30 31 30 29 30 29 30 30
"""

MONTH_NAMES = (
    "Baisakh", "Jestha", "Ashar", "Shrawan", "Bhadra", "Asoj",
    "Kartik", "Mangsir", "Poush", "Magh", "Falgun", "Chait",
)
BS_MONTHS = {
    values[0]: tuple(values[1:])
    for line in _CALENDAR_ROWS.strip().splitlines()
    for values in [tuple(map(int, line.split()))]
}

# 2000-01-01 BS was 1943-04-14 AD.
BS_EPOCH = (2000, 1, 1)
AD_EPOCH = date(1943, 4, 14)


def _validate_bs(year: int, month: int, day: int) -> None:
    if year not in BS_MONTHS:
        raise ValueError(f"BS year must be between {min(BS_MONTHS)} and {max(BS_MONTHS)}.")
    if not 1 <= month <= 12:
        raise ValueError("BS month must be between 1 and 12.")
    max_day = BS_MONTHS[year][month - 1]
    if not 1 <= day <= max_day:
        raise ValueError(f"{MONTH_NAMES[month - 1]} {year} has {max_day} days.")


def _days_from_epoch(year: int, month: int, day: int) -> int:
    """Return the zero-based day number of a valid BS date."""
    return (
        sum(sum(BS_MONTHS[current_year]) for current_year in range(BS_EPOCH[0], year))
        + sum(BS_MONTHS[year][: month - 1])
        + day - 1
    )


def bs_to_ad(year: int, month: int, day: int) -> date:
    """Convert a valid Bikram Sambat date to a Gregorian date."""
    _validate_bs(year, month, day)
    return AD_EPOCH + timedelta(days=_days_from_epoch(year, month, day))


def ad_to_bs(ad_date: date) -> tuple[int, int, int]:
    """Convert a supported Gregorian date to ``(BS year, month, day)``."""
    offset = (ad_date - AD_EPOCH).days
    if offset < 0:
        raise ValueError(f"AD date is before the supported range ({AD_EPOCH.isoformat()}).")

    for year, months in BS_MONTHS.items():
        year_days = sum(months)
        if offset < year_days:
            for month, days_in_month in enumerate(months, start=1):
                if offset < days_in_month:
                    return year, month, offset + 1
                offset -= days_in_month
        else:
            offset -= year_days
    raise ValueError(f"AD date is after the supported range ({bs_to_ad(2100, 12, 30).isoformat()}).")


def _read_ad_date() -> date:
    raw = input("Enter AD date (YYYY-MM-DD): ").strip()
    try:
        return date.fromisoformat(raw)
    except ValueError as error:
        raise ValueError("Use a real Gregorian date in YYYY-MM-DD format.") from error


def _read_bs_date() -> tuple[int, int, int]:
    raw = input("Enter BS date (YYYY-MM-DD): ").strip()
    try:
        year, month, day = (int(part) for part in raw.split("-"))
    except ValueError as error:
        raise ValueError("Use a BS date in YYYY-MM-DD format.") from error
    _validate_bs(year, month, day)
    return year, month, day


def main() -> None:
    print("\nAD ↔ BS Date Calculator")
    print(f"Supported: BS {min(BS_MONTHS)}-01-01 to {max(BS_MONTHS)}-12-30")

    while True:
        print("\n1. AD to BS\n2. BS to AD\n3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "3":
            print("Goodbye!")
            return
        try:
            if choice == "1":
                ad_date = _read_ad_date()
                year, month, day = ad_to_bs(ad_date)
                print(f"BS date: {year:04d}-{month:02d}-{day:02d} ({MONTH_NAMES[month - 1]})")
            elif choice == "2":
                year, month, day = _read_bs_date()
                print(f"AD date: {bs_to_ad(year, month, day).isoformat()}")
            else:
                print("Please choose 1, 2, or 3.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
