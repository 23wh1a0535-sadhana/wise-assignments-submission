# -*- coding: utf-8 -*-
"""multiply_num.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B_jZqfylg2f-JzivC-ZVrxW5ZQBjprHY
"""

# Multiplication table of 1 to 10
for i in range(1,11):
    print("\n\nMULTIPLICATION TABLE FOR %d\n" %(i))
    for j in range(1,11):
        print("%-5d X %5d = %5d" % (i, j, i*j))