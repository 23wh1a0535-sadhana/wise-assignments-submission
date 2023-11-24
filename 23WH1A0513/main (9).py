month_name = input("Enter month name: ").lower()
days_in_month = {
    "january": 31, "february": 28, "march": 31, "april": 30,
    "may": 31, "june": 30, "july": 31, "august": 31,
    "september": 30, "october": 31, "november": 30, "december": 
                }
if month_name in days_in_month:
    print(f"Number of days in {month_name.capitalize()}: {days_in_month[month_name]}")
else:
    print("Invalid month name entered.")