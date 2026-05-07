import calendar  

month, day, year = list(map(int, input().split()))

def guess_day(month, day, year):
    week_day = calendar.weekday(year, month, day)
    week_day_cap = calendar.day_name[week_day].upper()
    return week_day_cap
    
result = guess_day(month, day, year)
print(result)