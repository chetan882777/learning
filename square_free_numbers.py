from math import sqrt
def is_square(num):
    if sqrt(num)==int(sqrt(num)): return True
    else: return False

def factors(num):
    factors=[]
    for val in range(2,num+1):
        if num/val==num//val: factors.append(val)
    return factors

def is_square_free(num):
    temp=[]
    for val in factors(num):
        temp.append(not(is_square(val)))
    return all(temp)

while(1):
    print((factors(int(input()))))
    # found=[]
    # print(len([val for val in factors(int(input())) if is_square_free(val)]))