# -*- coding: utf-8 -*-
"""import_random.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B_jZqfylg2f-JzivC-ZVrxW5ZQBjprHY
"""

alphabet = input("Enter an alphabet: ").lower()
if alphabet.isalpha() and len(alphabet) == 1:
    if alphabet in 'aeiou':
        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
else:
    print("Please enter a single alphabet character.")