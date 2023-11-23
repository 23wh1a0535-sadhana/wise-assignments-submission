day  = int(input("Enter the day: "))
month = int(input("Enter the month number"))
year = int(input("Enter the year: "))
if year % 100 == 0 :
    if year % 400 == 0 :
        febdays = 29
    else:
        febdays = 28
else:
    if year % 4 == 0:
        febdays = 29
    else:
        febdays = 28
if month in [1 , 3 , 5 , 7 , 10 , 12]:
    monthlen = 31
elif month == 2 :
    monthlen = febdays
else:
    monthlen = 30
if day < monthlen:
    day += 1
else:
    day = 1
    if month < 12:
        month = 1
        year += 1
    else:
        month += 1
print(f'The next days is {day} - {month} - {year}')