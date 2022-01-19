# Author: CCG 1/18/22

def products(numbs, v):
    for index, value in enumerate(numbs):
        numbs[index] = value * v
        value *= v
    return numbs

print(products([10, 0], 2))
