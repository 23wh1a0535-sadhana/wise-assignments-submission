#5. Write a python program to create a list of names of students, their grades and join them together in the form of tuples.

names = ["mahesh", "sukesh", "mukesh"]
roll_no = [112 ,113, 114]
marks = [78, 34, 90]
print(list(zip(names, roll_no, marks)))
