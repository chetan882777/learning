from functools import reduce
from math import sqrt
def is_square(num):
    if sqrt(num)==int(sqrt(num)): return True
    else: return False

def factors(n):
    step = 2 if n % 2 else 1
    return list(sorted(set(reduce(list.__add__,([i, n // i] for i in range(1, int(sqrt(n)) + 1, step) if n % i == 0)))))

def is_square_free(num):
    temp=[]
    [temp.append(not (is_square(val))) for val in factors(num)]
    return all(temp[1:])

print(len(([val for val in factors(int(input())) if is_square_free(val)])[1:]))