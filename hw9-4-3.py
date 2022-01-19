# Author: CCG 1/18/22

def count_e(numb):
    x = 0
    for input in numb:
        if input.lower() == "e":
           x += 1
    return x

print(count_e("thereforE"))
