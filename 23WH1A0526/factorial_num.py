#This program is to find the factorial of a given number.
def fact(num):
  product = 1
  for i in range(1, num + 1):
    product *= i
  return product
num = int(input("Enter a number : "))
print(fact(num))
