import calendar
from datetime import datetime
def is_leap_year(year):
    return calendar.isleap(year)
def future_leap_years(start_year, end_year):
    leap_years = []
    for year in range(start_year + 1, end_year + 1):  
        if is_leap_year(year):
            leap_years.append(year)
    return leap_years

current_year = datetime.now().year
end_year = int(input("Enter the end year: "))
leap_years = future_leap_years(current_year, end_year)

if leap_years:
    print(f"Future leap years from {current_year} to {end_year}: {leap_years}")
else:
    print(f"There are no leap years between {current_year} and {end_year}.")

