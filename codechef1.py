for _ in range(int(input())):
    days = int(input())
    attendence = list(input())
    count = dict((('P', 0), ('A', 0)))
    for val in attendence:
        if val in 'PA':
            count[val] += 1
    percent = (count['P'] * 100) / days
    # print(percent)
    proxy_needed = 0
    d = 0
    final = 0
    if (percent>=75) or days==0 : print(0)
    else:
        # flag=-1
        while (percent < 75):
            for idx, val in enumerate(attendence[d + 2:-2]):
                if val == 'A':
                    d = idx
                    break

            count = dict((('P', 0), ('A', 0)))
            for val in attendence:
                if val in 'PA':
                    count[val] += 1

            proxy_needed += 1
            percent = ((count['P'] + proxy_needed) * 100) / days

            final += 1
    if final<:print(final)