def check(check_x,check_y):
    if (check_x,check_y) not in total_safe: total_safe.append((check_x, check_y))

    if (check_x-1,check_y) not in cage and (check_x-1,check_y) not in total_safe and check_x-1>-1 and layout[check_x-1][check_y]=='G': check(check_x - 1, check_y)

    if (check_x+1, check_y) not in cage and (check_x+1, check_y) not in total_safe and check_x+1<x_map and layout[check_x+1][check_y]=='G': check(check_x + 1, check_y)

    if (check_x, check_y-1) not in cage and (check_x, check_y-1) not in total_safe and check_y-1>-1 and layout[check_x][check_y-1]=='G': check(check_x,check_y-1)

    if (check_x, check_y+1) not in cage and (check_x, check_y+1) not in total_safe and check_y+1<y_map and layout[check_x][check_y+1]=='G': check(check_x, check_y + 1)

    return 0

def check_unsafe(check_x,check_y):

    total_unsafe.append((check_x, check_y))

    if (check_x-1,check_y) not in total_unsafe and check_x-1>-1 and layout[check_x-1][check_y] in 'GM': check_unsafe(check_x - 1, check_y)

    if (check_x+1, check_y) not in total_unsafe and check_x+1<x_map and layout[check_x+1][check_y] in 'GM': check_unsafe(check_x + 1, check_y)

    if (check_x, check_y-1) not in total_unsafe and check_y-1>-1 and layout[check_x][check_y-1] in 'GM': check_unsafe(check_x,check_y-1)

    if (check_x, check_y+1) not in total_unsafe and check_y+1<y_map and layout[check_x][check_y+1] in 'GM': check_unsafe(check_x, check_y + 1)

    return 0

x_map,y_map=map(int,input().split())
x_gateone,y_gateone,x_gatetwo,y_gatetwo,x_gatethree,y_gatethree,x_cage,y_cage=map(lambda x:x-1,map(int,input().split()))

total_safe,total_unsafe,layout,cage=[],[],[],[(x_cage,y_cage)]

for i in range(y_map):
    layout.append(list(input().split()))

for val in [(x_gateone,y_gateone),(x_gatetwo,y_gatetwo),(x_gatethree,y_gatethree)]:
    check(*val)

check_unsafe(x_cage,y_cage)

total_safe.extend(list(set([(idx1,idx2) for idx1,val in enumerate(layout) for idx2,val2 in enumerate(val) if val2=='G'])-set(set(total_unsafe)-set([(idx1,idx2) for idx1,val in enumerate(layout) for idx2,val2 in enumerate(val) if val2=='M']))))
print(round((len(total_safe)*100)/len([val2 for val in  layout for val2 in val if val2=='G']),2))