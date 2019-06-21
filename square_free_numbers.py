from functools import reduce
def factors(n):
    step = 2 if n % 2 else 1
    return list(sorted(set(reduce(list.__add__,([i, n // i] for i in range(1, int(n**0.5) + 1, step) if n % i == 0)))))

def is_square_free(num): return all([not(val**0.5==int(val**0.5)) for val in factors(num)][1:])

print(len(([val for val in factors(int(input())) if is_square_free(val)])[1:]))