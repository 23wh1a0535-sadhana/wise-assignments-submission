# Python program to reverse a number using function

def reverseIs(n):  
   reverse = 0
   reminder = 0
   while(n != 0):
      remainder = n % 10
      reverse = reverse * 10 + remainder
      n = int(n / 10)
   return reverse
num = 12345
reverse = reverseIs(num)
print('The reverse number is =', reverse)
