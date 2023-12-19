#Python program to convert all the characters into uppercase and lowercase  and eliminate duplicate letters from a given sequence.Using ,map()function
def change_cases(s):
  return str(s).upper(), str(s).lower()
characters ={'a','b','c','d','e','c','d','i'}
print("Original Characters:\n",characters)
 
result = map(change_cases, characters)
print("\nAfter converting above characters into upper and lower cases and eliminating duplicate letters:")
print(set(result))
