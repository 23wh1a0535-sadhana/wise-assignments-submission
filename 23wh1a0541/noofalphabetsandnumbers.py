#Write a Python program that accepts a string and calculates the number of digits and letters.
string = input("Enter a string: ")
length = len(string)
countnum = 0
countalpha = 0
for i in range(length):
    if string[i].isnumeric():
        countnum += 1
    elif string[i].isalpha():
        countalpha += 1
print("The given string," , string , "has" , countalpha , "letters and" , countnum , "numbers.")