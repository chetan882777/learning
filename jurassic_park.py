x_map,y_map=map(int,input().split())
x_gateone,y_gateone,x_gatetwo,y_gatetwo,x_gatethree,y_gatethree,x_cage,y_cage=map(lambda x:x-1,map(int,input().split()))
layout=[]
for i in range(y_map):
    layout.append(list(input().split()))
# print(layout)

mountains=[(idx1,idx2) for idx1,val in enumerate(layout) for idx2,char in enumerate(val) if char=='M']
grassland=[(idx1,idx2) for idx1,val in enumerate(layout) for idx2,char in enumerate(val) if char=='G']
water=[(idx1,idx2) for idx1,val in enumerate(layout) for idx2,char in enumerate(val) if char=='W']
gates=[(x_gateone,y_gateone),(x_gatetwo,y_gatetwo),(x_gatethree,y_gatethree)]
cage=[(x_cage,y_cage)]
# print('mountains',mountains)
# print('water',water)
# print('gates',gates)
# print(layout[1][1])

total_safe=[]
total_safe_count=len(total_safe)

grassland=[item for item in grassland if item not in gates]
# print('grassland',grassland)
# print(total_safe)

total_unsafe=cage
total_unsafe_count=len(total_unsafe)

for val in gates:
    path=[]
    path.append(val)
    # total_safe.append(val)
    for val2 in path:
        temp_x,temp_y=val2
        print('this')
        while temp_x>-1:
            # temp_x-=1
            if layout[temp_x][temp_y]=='G':
                tup=(temp_x,temp_y)
                path.append(tup)
            if layout[temp_x][temp_y] in 'WM' :
                break
            print(temp_x)
            if temp_x==0:
                break
            temp_x -= 1
        while temp_x<x_map+1:
            # temp_x += 1
            if layout[temp_x][temp_y] == 'G':
                tup = (temp_x, temp_y)
                path.append(tup)
            if layout[temp_x][temp_y] in 'WM':
                break
            if temp_x==x_map:
                break
            # print(temp_x)
            temp_x += 1
        while temp_y>-1:
            # temp_y -= 1
            if layout[temp_x][temp_y] == 'G':
                tup = (temp_x, temp_y)
                path.append(tup)
            if layout[temp_x][temp_y] in 'WM':
                break
            if temp_y==0:
                break
            temp_y -= 1
        while temp_y<y_map+1:
            # temp_y += 1
            if layout[temp_x][temp_y] == 'G':
                tup = (temp_x, temp_y)
                path.append(tup)
            if layout[temp_x][temp_y] in 'WM':
                break
            if temp_y==y_map:
                break
            temp_y += 1
    print(path)