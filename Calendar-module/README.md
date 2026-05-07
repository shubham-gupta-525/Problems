# Calendar Module

## Problem
Given a date in `MM DD YYYY` format, determine the day of the week for that date.

## HackerRank Link
https://www.hackerrank.com/challenges/calendar-module/problem

## Difficulty
Easy

## Approach
- Used Python's built-in `calendar` module.
- `calendar.weekday(year, month, day)` returns the weekday index.
- `calendar.day_name[]` converts the index into the corresponding weekday name.
- Converted the output to uppercase using `.upper()`.

## Complexity
- Time Complexity: O(1)
- Space Complexity: O(1)

## Solution (Python)

```python
import calendar  

month, day, year = list(map(int, input().split()))

def guess_day(month, day, year):
    week_day = calendar.weekday(year, month, day)
    week_day_cap = calendar.day_name[week_day].upper()
    return week_day_cap
    
result = guess_day(month, day, year)
print(result)
```