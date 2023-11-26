#Write a Python program to convert a month name to a number of days.
monthname = input("Enter the month name: ").lower()
noofdaysinmonth = {"january": 31, "february": 28, "march": 31, "april": 30,
"may": 31, "june": 30, "july": 31, "august": 31,
"september": 30, "october": 31, "november": 30, "december": 31}
if monthname in noofdaysinmonth:
    print(f"Number of days in {monthname}: {noofdaysinmonth[monthname]}")
else:
    print("Invalid month name entered.")