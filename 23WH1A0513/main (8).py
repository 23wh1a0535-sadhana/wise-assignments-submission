 alphabet = input("Enter an alphabet: ").lower()
if alphabet.isalpha() and len(alphabet) == 1:
    if alphabet in 'aeiou':
        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
else:
    print("Please enter a single alphabet character.")