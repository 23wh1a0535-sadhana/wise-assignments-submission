# -*- coding: utf-8 -*-
"""num_list.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B_jZqfylg2f-JzivC-ZVrxW5ZQBjprHY
"""

#number into list
num = int(input("Enter a number: "))
print("Given number: ",num)
list = [int(x) for x in str(num)]
print("List of number: \n",list)