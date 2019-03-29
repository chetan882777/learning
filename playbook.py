# l=[]
# for i in range(2000,3201):
#     if (i%7) and   (i%5!=0):
#         l.append(str(i))
#         print(i)
# print (','.join(l))

# def fact(x):
#     if x==0:
#         return 1
#     return x*fact(x-1)
#
# x=int(input("type number"))
# print(fact(x))
#

n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i
print(d)