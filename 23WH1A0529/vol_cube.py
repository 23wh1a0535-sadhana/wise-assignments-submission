# -*- coding: utf-8 -*-
"""vol_cube.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1B_jZqfylg2f-JzivC-ZVrxW5ZQBjprHY
"""

#volume of a cube
def vol_cube(a):
    volume = a**3
    return volume
s = int(input("Enter side: "))
print(vol_cube(s))