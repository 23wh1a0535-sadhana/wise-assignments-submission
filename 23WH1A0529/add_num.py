# -*- coding: utf-8 -*-
"""add_num.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B_jZqfylg2f-JzivC-ZVrxW5ZQBjprHY
"""

#adding numbers
total = 0
list1 = [11,4,67,54,78]
for ele in range(0,len(list1)):
    total = total + list1[ele]
print("Sum of all elements in given list: ",total)