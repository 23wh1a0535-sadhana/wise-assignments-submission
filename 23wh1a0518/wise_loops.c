#guess the number
import random
number_to_guess=random.randint(1,9)
guessed=False
while not guessed:
    guess=int(input("guess a number between 1 to 9:"))
    if guess==number_to_guess:
        print("congratulations!you guessed the correct number.")
        guessed=True
    else:
       print("try again.")

  guess a number between 1 to 9:5
try again.
guess a number between 1 to 9:1
try again.
guess a number between 1 to 9:2
try again.
guess a number between 1 to 9:3
try again.
guess a number between 1 to 9:4
congratulations!you guessed the correct number.



#pattern
for i in range(1,6):
    print('*'*i)
for i in range(4,0,-1):
    print('*'*i)

*
**
***
****
*****
****
***
**
*



#range 1 to 6 except 3 and 6
for i in range(7):
    if i!=3 and i!=6:
        print(i)

0
1
2
4
5



#alphabet and integers in a string
string=input("enter a string:")
letters=sum(c.isalpha()for c in string)
digits=sum(c.isdigit()for c in string)
print(f"letters:{letters},digits:{digits}")

enter a string:diya060605
letters:4,digits:6



 #factorial of a number
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
num=int(input("enter a number:"))
print("factorial:",factorial(num))

 enter a number:5
factorial: 120



  #arithematic progresstion
import random
def generate_arithematic_progression(initial_number,common_difference,terms):
    progression=[initial_number + i * common_difference for i in range(terms)]
    return progression
initial_number = 25
common_difference = random.randint(1,10)
terms=5
random_ap = generate_arithematic_progression(initial_number,common_difference,terms)
print(f"random arithematic progression:{random_ap}")

  random arithematic progression:[25, 31, 37, 43, 49]



#program to print reverse of a word
word = input("enter a word:")
reversed_word = word[::-1]
print("reversed word:",reversed_word)

enter a word:diya
reversed word: ayid



#is vowel or consonent
alphabet = input("enter an alphabet:").lower()
if alphabet.isalpha() and len(alphabet) == 1:
    if alphabet in'aeiou':
        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
else:
    print("please enter a single alphabet character.")

enter an alphabet:d
d is a consonant.



#number of days in months
month_name = input("enter month name:").lower()
days_in_month={
    "january":31, "february":28, "march":31, "april":30, "may":31, "june":30, 
    "july":31, "august":31, "september":30, "october":31, "november":30, 
    "december":31
}
if month_name in days_in_month:
    print(f"number of days in{month_name.capitalize()}:{days_in_month[month_name]}")
else:
    print("invalid month name entered.")

enter month name:june
number of days inJune:30



#month and its season
month=input("input the month(e.g. january,february etc.):")
day=int(input("input the day:"))
if month in ('january','fabruary','march'):
    season='winter'
elif month in ('april','may','june'):
    season='spring'
elif month in('july','august','september'):
    season='summer'
else:
    season='autumn'
if (month == 'march') and (day > 19):
    season = 'spring'
elif(month == 'june') and (day > 20):
    season = 'summer'
elif(month == 'september') and (day > 21):
    season = 'autumn'
elif(month == 'december') and (day > 20):
    season = 'winter'
print("season is",season)

input the month(e.g. january,february etc.):june
input the day:30
season is summer




#leap year
def is_leap_year(year):
    return(year%4==0 and year%100!=0) or (year%400==0)
def get_next_day(year,month,day):
    days_in_month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year):
        days_in_month[2] = 29
    if day<days_in_month[month]:
        return year,month,day+1
    else:
        if month==12:
            return year +1,1,1
        else:
            return year,month +1,1
# input date
year=int(input("enter year:"))
month=int(input("enter month(1-12): "))
day=int(input("enter day (1-31): "))
next_year, next_month,next_day = get_next_day(year,month,day)
print(f"the next day is:{next_year}-{next_month:02d}-{next_day:02d}")

enter year:2005
enter month(1-12): 6
enter day (1-31): 6
the next day is:2005-06-07



number=int(input("enter a number"))
i=number
while(i>=1):
    print(i)
    i=i-1

 enter a number:6
  5
  4
  3
  2
  1
  
