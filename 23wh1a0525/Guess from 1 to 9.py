#Guess a number between 1 and 9
num = 5
while 1 :
    guess = int(input("Enter your guess between 1 and 9: "))
    if guess == num:
        print("Yay! You guessed it right! It is" , num)
        break
