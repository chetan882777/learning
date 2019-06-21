def traverse(x,y):
    temp=[]
    traversed.append((x,y))
    destination=0
    if -1<x+1<n and -1<y<n and (x+1,y) not in traversed:
        if layout[x+1][y] is 'R' :   togo=(x+1,y)
        elif layout[x+1][y] in 'MA':  pass
        elif layout[x+1][y] is 'D': destination=1
        else: temp.append(layout[x+1][y]) and traversed.append((x+1,y))

    if -1<x+1<n and -1<y+1<n and (x+1,y+1) not in traversed:
        if layout[x+1][y+1] is 'R' :   togo=(x+1,y+1)
        elif layout[x+1][y+1] in 'MA':  pass
        elif layout[x+1][y+1] is 'D': destination=1
        else: temp.append(layout[x+1][y+1]) and traversed.append((x+1,y+1))

    if -1<x<n and -1<y+1<n and (x,y+1) not in traversed:
        if layout[x][y+1] is 'R' :   togo=(x,y+1)
        elif layout[x][y+1] in 'MA':  pass
        elif layout[x][y+1] is 'D': destination=1
        else: temp.append(layout[x][y+1]) and traversed.append((x,y+1))

    if -1<x-1<n and -1<y+1<n and (x-1,y+1) not in traversed:
        if layout[x-1][y+1] is 'R' :   togo=(x-1,y+1)
        elif layout[x-1][y+1] in 'MA':  pass
        elif layout[x-1][y+1] is 'D': destination=1
        else: temp.append(layout[x-1][y+1]) and traversed.append((x-1,y+1))

    if -1<x-1<n and -1<y<n and (x-1,y) not in traversed:
        if layout[x-1][y] is 'R' :   togo=(x-1,y)
        elif layout[x-1][y] in 'MA':  pass
        elif layout[x-1][y] is 'D': destination=1
        else: temp.append(layout[x-1][y]) and traversed.append((x-1,y))

    if -1<x-1<n and -1<y-1<n and (x-1,y-1) not in traversed:
        if layout[x-1][y-1] is 'R' :   togo=(x-1,y-1)
        elif layout[x-1][y-1] in 'MA':  pass
        elif layout[x-1][y-1] is 'D': destination=1
        else: temp.append(layout[x-1][y-1]) and traversed.append((x-1,y-1))

    if -1<x<n and -1<y-1<n and (x,y-1) not in traversed:
        if layout[x][y-1] is 'R' :   togo=(x,y-1)
        elif layout[x][y-1] in 'MA':  pass
        elif layout[x][y-1] is 'D': destination=1
        else: temp.append(layout[x][y-1]) and traversed.append((x,y-1))

    if -1<x+1<n and -1<y-1<n and (x+1,y-1) not in traversed:
        if layout[x+1][y-1] is 'R':   togo=(x+1,y-1)
        elif layout[x+1][y-1] in 'MA':  pass
        elif layout[x+1][y-1] is 'D': destination=1
        else: temp.append(layout[x+1][y-1]) and traversed.append((x+1,y-1))

    if layout[x][y] is not 'A' :  print(' '.join(sorted(temp)))
    if destination==1:
        print('DESTINATION')
        return 0
    traverse(*togo)
    return 0

n,layout,traversed,temp=int(input()),[],[],[]
for _ in range(n):
    layout.append(list(input().split()))
a,d=(0,0),[(idx1,idx2) for idx1,val1 in enumerate(layout) for idx2,val in enumerate(val1) if val is 'D']
traverse(*a)