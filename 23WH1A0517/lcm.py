def getHCF(num1, num2):
    while num1!=num2:
        if num1>num2:
            num1-=num2
        else:
            num2-=num1
    return num1


num1 = int(input("enter a number:"))
num2 = int(input("enter another number:"))

# Calculating HCF here
hcf = getHCF(num1, num2)

# LCM formula
lcm = (num1*num2)//hcf

print("LCM of", num1, "and", num2, "is", lcm)