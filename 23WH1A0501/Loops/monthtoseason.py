#Write a Python program that reads two integers
# representing a month and day and prints the season for that month and day.
month = input("Enter the month name: ").lower()
day = int(input("Enter the day of the month: "))

if (month in ('january', 'february')) or ((month == 'march') and (day <= 19)) or ((month == 'december') and (day > 20)):
	season = 'winter'
elif (month in ('april', 'may', 'march')) or ((month == 'june') and (day <= 20)):
	season = 'spring'
elif (month in ('july', 'august',"june" )) or ((month == 'september') and (day <= 21)):
	season = 'summer'
else:
	season = 'autumn'
print("Season is",season)
