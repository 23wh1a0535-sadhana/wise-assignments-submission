#This program tells whether the given number is a palindrome or not.
def isPalindrome(s):
    return s == s[::-1]
s = input("Enter a string ")
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")
