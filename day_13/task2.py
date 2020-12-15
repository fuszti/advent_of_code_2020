"""
Source of the used chinese remainder solver:
https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
2020.12.13.
"""
from functools import reduce

def solve_task2(file_name):
    with open(file_name,"r") as f:
        time = int(f.readline())
        buses = [int(i) if i != "x" else -1 for i in f.readline().split(",")]

    indices = [-i for i in range(len(buses)) if buses[i] != -1]
    buses_small = [buses[i] for i in range(len(buses)) if buses[i] != -1]

    time = chinese_remainder(buses_small,indices)
    
    return time

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

if __name__=="__main__":
    print(solve_task2("day_13/input.txt"))
    