#Write a python program to convert a number into a list of its digits.
def numtolist(num):
    numtemp = num
    numdigitlist = []
    while numtemp != 0:
        rem = numtemp % 10
        numdigitlist.append(rem)
        numtemp //= 10
    numdigitlist.reverse()
    return numdigitlist
print(numtolist(123456))

