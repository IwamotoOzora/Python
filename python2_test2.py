def is_leap_year(year):
    return (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))

from dateutil.relativedelta import relativedelta
import datetime

today = datetime.date.today()
next_year = today + relativedelta(years =+ 1)
last_year = (today + relativedelta(years =- 1))

years = [last_year, today, next_year]

for year in years:
    if is_leap_year(year.year):
        print("{}は閏年です".format(year))
    else:
        print("{}は閏年ではありません".format(year))