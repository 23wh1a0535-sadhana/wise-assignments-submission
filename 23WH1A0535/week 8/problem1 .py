#Problem 1
#Given a string of the form "mmddyyyy", (example: "02072016") compute the seven digit number yyyyddd, where ddd is the nth days of the year. 
#For example "02072016" is the 38th day of the year and 2016038 is the expected result; similarly "12201996" -> 1996355

def compute_seven_digit_number(date_string):
    # Extract month, day, and year from the input string
    month = int(date_string[0:2])
    day = int(date_string[2:4])
    year = int(date_string[4:])
    # Define a list representing the number of days in each month
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Check for leap year and update February's days accordingly
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29
    # Calculate the day of the year
    day_of_year = sum(days_in_month[:month]) + day
    # Create the seven-digit result
    result = int(f"{year}{day_of_year:03}")
    return result

date_input = "02072016"
result_output = compute_seven_digit_number(date_input)
print(result_output)

date_input = "12201996"
result_output = compute_seven_digit_number(date_input)
print(result_output)

#General format:
date_input = input("Enter a date in mmddyyyy format : ")
result_output = compute_seven_digit_number(date_input)
print(result_output)
