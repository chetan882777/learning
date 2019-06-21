# cook your dish here
import math

t = int(input())
while t > 0:
    n = int(input())
    s = input()
    d = {'P': 0, 'A': 0}
    for i in s:
        d[i] += 1
    a = (d['P'] * 100) / n
    if a >= 75:
        print(0)
    else:

        r = d['P']
        c = 0
        j = 2
        flag = -1
        while j < n - 2:
            if s[j] == 'A' and ((s[j - 1] == 'P' or s[j - 2] == 'P') and (s[j + 1] == 'P' or s[j + 2] == 'P')):

                r += 1
                c += 1
                a = (r * 100) / n
                if a >= 75:
                    print(c)
                    flag = 0
                    break
            j += 1
        if flag == -1:
            print(-1)

    t -= 1
