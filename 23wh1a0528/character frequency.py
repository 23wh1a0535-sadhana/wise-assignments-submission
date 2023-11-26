def charfreq(string , char):
    count = 0
    length = len(string)
    for i in range (length):
        if string[i] == char:
            count += 1
    return count
string = input("Enter a string: ")
char = input("Enter the character the string is to be searched for: ")
count = charfreq(string , char)
print(count)