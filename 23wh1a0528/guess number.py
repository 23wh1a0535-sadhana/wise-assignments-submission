number_to_guess = random.randint(1, 9)
guessed = False

while not guessed:
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == number_to_guess:
        print("Congratulations! You guessed the correct number.")
        guessed = True
    else:
        print("Try again.")