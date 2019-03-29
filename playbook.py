l=[]
for i in range(2000,3201):
    if (i%7) and   (i%5!=0):
        l.append(str(i))
        print(i)

print','.join(l)