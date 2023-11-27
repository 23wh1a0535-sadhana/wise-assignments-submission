fruits = ["apple", "banana", "guava", "cherry", "mango"]
string_of_fruits = ""
for fruit in fruits:
    string_of_fruits += fruit + ", "
string_of_fruits = string_of_fruits[:-2] 
print(string_of_fruits)
