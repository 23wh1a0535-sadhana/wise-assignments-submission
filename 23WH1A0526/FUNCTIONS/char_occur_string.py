#To count the occurance of characters in a string.
count = 0
my_string = input("Enter a string : ")
my_char = input("Enter a character : ")
for i in my_string:
    if i == my_char:
        count += 1
print(count)
