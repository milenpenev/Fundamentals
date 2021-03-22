import re
dates = input()

pattern = r"(?P<Day>\d{2})(?P<separator>[/|\-|.])(?P<Month>[A-Z][a-z]{2})(?P=separator)(?P<Year>\d{4})"
matches = [valid_dates.groupdict() for valid_dates in re.finditer(pattern, dates)]
print('\n'.join([f"Day: {data['Day']}, Month: {data['Month']},"
                 f" Year: {data['Year']}" for data in matches]))
