from itertools import combinations as cmb
from itertools import permutations as per
# import datetime


def monthcheck(month):
    return 0 < month <= 12

def minutecheck(minute):
    return 1<minute<=59

def hourcheck(hour):
    return 0<hour<=23

def daycheck(month,day):
    monthlist1 = [1,3,5,7,8,10,12] ## monthlist for months with 31 days.
    monthlist2 = [4,6,9,11] ## monthlist for months with 30 days.
    monthlist3 = 2 ## month with month with 28 days.

    for mon in monthlist1: ## iterate through monthlist1.
        if month == mon: ## Check if the parameter month equals to any month with 31 days.
            if day >=1 and day <= 31: ## If the parameter day is between 1 and 31, return True.
                return True
            else:
                return False

    for mon in monthlist2: ## iterate through the monthlist with 30 days.
        if month == mon: ## check if the parameter month equals to any month with 30 days.
            if day >= 1 and day <= 30: ## if the parameter day is between 1 and 30,return True.
                return True
            else:
                return False

    if month == monthlist3: ## check if parameter month equals month with 28 days.
        if day >=1 and day <= 28: ## if the parameter day is between 1 and 28,return True.
            return True
        else:
            return False

l=input()
listing=l.split(',')
# print(list)
listing=list(map(int,listing))
print(listing)
combi=list(cmb(listing,2))
print(combi)
month=[]
for val in combi:
    templisting=listing.copy()
    monthing=''.join(map(str,val))
    if int(monthing[:1]) in templisting:
        templisting.remove(int(monthing[:1]))
        if int(monthing[1:]) in templisting:
            templisting.remove(int(monthing[1:]))
            if monthcheck(int(monthing)):
                month.append(monthing)
for val in [(t[1], t[0]) for t in combi]:
    templisting = listing.copy()
    # val[1], val[0] = val[0], val[1]
    monthing = ''.join(map(str, val))
    if int(monthing[1:]) in templisting:
        templisting.remove(int(monthing[1:]))
        if int(monthing[:1]) in templisting:
            templisting.remove(int(monthing[:1]))
            if monthcheck(int(monthing)):
                month.append(monthing)
# print(listing)
final_month=max(month)
listing.remove(int(str(final_month)[:1]))
listing.remove(int(str(final_month)[1:]))
# print(month)
# print(final_month)
# print(listing)
combi=list(cmb(listing,2))
day=[]
for val in combi:
    templisting=listing.copy()
    daying=''.join(map(str,val))
    if int(daying[:1]) in templisting:
        templisting.remove(int(daying[:1]))
        if int(daying[1:]) in templisting:
            templisting.remove(int(daying[1:]))
            if daycheck(int(final_month),int(daying)):
                # print('working')
                day.append(daying)
for val in [(t[1], t[0]) for t in combi]:
    templisting=listing.copy()
    # val[1],val[0]=val[0],val[1]
    daying = ''.join(map(str, val))
    if int(daying[1:]) in templisting:
        templisting.remove(int(daying[1:]))
        if int(daying[:1]) in templisting:
            templisting.remove(int(daying[:1]))
            if daycheck(int(final_month),int(daying)):
                day.append(daying)
# print('daying',day)
final_day=max(day)

listing.remove(int(str(final_day)[:1]))
listing.remove(int(str(final_day)[1:]))

combi=list(cmb(listing,2))
hour=[]
for val in combi:
    templisting=listing.copy()
    daying=''.join(map(str,val))
    if int(daying[:1]) in templisting:
        templisting.remove(int(daying[:1]))
        if int(daying[1:]) in templisting:
            templisting.remove(int(daying[1:]))
            if hourcheck(int(daying)):
                # print('working')
                hour.append(daying)
for val in [(t[1], t[0]) for t in combi]:
    templisting=listing.copy()
    # val[1],val[0]=val[0],val[1]
    daying = ''.join(map(str, val))
    if int(daying[1:]) in templisting:
        templisting.remove(int(daying[1:]))
        if int(daying[:1]) in templisting:
            templisting.remove(int(daying[:1]))
            if hourcheck(int(daying)):
                hour.append(daying)
# print('daying',day)
final_hour=max(hour)

listing.remove(int(str(final_hour)[:1]))
listing.remove(int(str(final_hour)[1:]))
combi=list(cmb(listing,2))
minute=[]
for val in combi:
    templisting=listing.copy()
    daying=''.join(map(str,val))
    if int(daying[:1]) in templisting:
        templisting.remove(int(daying[:1]))
        if int(daying[1:]) in templisting:
            templisting.remove(int(daying[1:]))
            if minutecheck(int(daying)):
                # print('working')
                minute.append(daying)
for val in [(t[1], t[0]) for t in combi]:
    templisting=listing.copy()
    # val[1],val[0]=val[0],val[1]
    daying = ''.join(map(str, val))
    if int(daying[1:]) in templisting:
        templisting.remove(int(daying[1:]))
        if int(daying[:1]) in templisting:
            templisting.remove(int(daying[:1]))
            if minutecheck(int(daying)):
                minute.append(daying)
# print('daying',day)
final_minute=max(minute)

listing.remove(int(str(final_minute)[:1]))
listing.remove(int(str(final_minute)[1:]))
print(final_month+'/'+final_day+' '+final_hour+':'+final_minute)
print(listing)

# datetime.datetime(year=2018,month=month,day=day,hour=hour,minute=minute)

#

#
