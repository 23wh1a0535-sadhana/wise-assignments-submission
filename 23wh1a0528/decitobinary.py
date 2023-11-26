def decitobinary(num):
    binary = 0
    while(num != 0):
        rem = num % 2
        binary = binary*10 + rem
        num //= 2
    return binary
testnum = int (input("Enter a number: "))
print(decitobinary(testnum))