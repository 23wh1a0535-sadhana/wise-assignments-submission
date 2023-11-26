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