def largeststringinlist(List):
    lenlargest = len(List[0])
    largeststring = List[0]
    for i in range(len(List)):
        if len(List[i]) > lenlargest:
            lenlargest = len(List[i])
            largeststring = List[i]
    return largeststring
elementno  = int(input("Enter the number of strings in the list: "))
stringlist = []
for i in range (elementno):
    stringlist.append(input("Enter a string: "))
print(largeststringinlist(stringlist))