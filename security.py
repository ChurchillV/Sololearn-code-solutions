from more_itertools import locate 
#Special module to help with finding indexes

#Function to find the index of each instance of G
def find_instance(some_list, item):
    indeces = locate(some_list, lambda x:x == item)
    return(list(indeces))

#Taking input from the user
floor = input()

#Safety points to keep track of the position of guards, the thief and the money
safety_points = 0

#The indexes of each instance of guards is stored here
guards = find_instance(floor, 'G')

money = floor.index('$')
thief = floor.index('T')

#The positional logic
for num in range(len(guards)):
    if guards[num] < money and guards[num] > thief: #Eg. xTxGxx$
        safety_points += 2 
    elif guards[num] > money and guards[num] < thief: #Eg. xx$xGxxTxx
        safety_points += 2
    else: safety_points -= 1

#Output logic
if safety_points >= 0:
    print('quiet')
else:
    print('ALARM')


"""
Evaluate a given floor to determine if there is a guard between the money and 
the thief, if there isn't, you sound an alarm.

Input:
A string of characters that includes symbols $(money), T(thief), and G(guard),
that represents the layout of the floor.
Space on the floor that is occupied by neither money, a thief or guards is 
denoted by the character x.

Output:
A string that says 'ALARM' is the money is in danger ot 'quiet' if the money
is safe.

SAMPLE INPUT:
xxxGxxx$xxxT

SAMPLE OUTPUT:
ALARM
"""