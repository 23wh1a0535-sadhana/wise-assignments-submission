a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
if a > b:
    maximum = a
else:
    maximum = b

while True :
    if(maximum % a == 0 and maximum % b == 0):
        print(a, b,maximum)
        break;
    maximum = maximum + 1
