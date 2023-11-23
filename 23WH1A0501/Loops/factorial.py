#Write a program to calculate factorial of a given number.
def fact(no):
    product = 1
    for i in range(1 , no + 1):
        product *= i
    return product
num = int(input("Enter a number :"))
print(fact(num))