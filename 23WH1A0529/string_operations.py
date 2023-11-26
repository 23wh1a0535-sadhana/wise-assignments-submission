# -*- coding: utf-8 -*-
"""string_operations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B_jZqfylg2f-JzivC-ZVrxW5ZQBjprHY
"""

string = input("Enter a string: ")
digits = sum(c.isdigit() for c in string)
letters = sum(c.isalpha() for c in string)
print(f"Number of digits: {digits}")
print(f"Number of letters: {letters}")

