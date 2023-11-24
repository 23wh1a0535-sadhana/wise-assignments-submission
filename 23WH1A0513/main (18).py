def rev_string(s):
    str = " "
    for i in s:
        str = i + str
    return str
s = "SaiDevi"
print(rev_string(s))