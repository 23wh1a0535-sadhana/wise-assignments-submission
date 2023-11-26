#Write a Python program that accepts a word from the user and reverses it
string = input("Enter a word: ")
templist = list(string)
templist.reverse()
string = ""
string = string.join(templist)
print(string)