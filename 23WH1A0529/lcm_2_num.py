# -*- coding: utf-8 -*-
"""lcm_2_num.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B_jZqfylg2f-JzivC-ZVrxW5ZQBjprHY
"""

#lcm of 2 numbers
def compute_lcm(x,y):
#choose the greatest number
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x==0) and (greater % y==0)):
            lcm = greater
        break
    greater +=1
    return lcm
num1 = int(input("Enter a number"))
num2 = int(input("Enter a number"))
print("The lcm is ", compute_lcm(num1,num2))