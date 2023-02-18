from more_itertools import locate

def find_instance(some_list, item):
    indeces = locate(some_list, lambda x:x == item)
    return(list(indeces))

floor = input()
safety_points = 0

guards = find_instance(floor, 'G')

money = floor.index('$')
thief = floor.index('T')

for num in range(len(guards)):
    if guards[num] < money and guards[num] > thief:
        safety_points += 1 
    elif guards[num] > money and guards[num] < thief:
        safety_points += 1
    else: safety_points -= 1

if safety_points >= 0:
    print('quiet')
else:
    print('ALARM')
