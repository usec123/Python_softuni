from math import floor
pageCount = int(input())
pagesPerHour = int(input())
days = int(input())
hours = pageCount / pagesPerHour
dailyHours = hours/days
print(floor(dailyHours))