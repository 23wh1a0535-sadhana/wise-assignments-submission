#Guess a number between 1 and 9
num = 5
while True:
  guess = int(input("Enter your guessed number between 1 and 9: "))
  if guess == num:
    print("Congratulations! You've guessed it correctly! The number is : ",num)
    break
