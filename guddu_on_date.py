for _ in range(int(input())):
    n=int(input())
    num,count=0,0
    while(count<n):
        num += 1
        if sum(map(int,list(str(num))))%10==0 :
            count+=1
            if count==n: break
    print(num)
