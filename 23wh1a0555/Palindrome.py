#Write a program to check wether a given string is a palindrome or not.
def ifpalindrome(string):
    templist = list(string)
    templist.reverse()
    stringrev = ""
    stringrev = stringrev.join(templist)
    if stringrev == string:
        output  = "Palindrome"
    else:
        output = "Not a palindrome"
    return output
print(ifpalindrome(input("Enter a string")))
