a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
if a > b:
    maximum = a
else:
    maximum = b

while True :
    if(maximum % a == 0 and maximum % b == 0):
        print(a, b,maximum)
        break;
    maximum = maximum + 1
