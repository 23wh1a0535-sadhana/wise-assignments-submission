#This is to find the length of the string.
def findLen(s):
    count = 0   
    for i in s:
        count += 1
    return count
str = "WISE ASSIGNMENT"
print(findLen(str))
