def stringrev(string):
    templist = list(string)
    templist.reverse()
    string = ""
    string = string.join(templist)
    return (string)
print(stringrev("Gnanika"))