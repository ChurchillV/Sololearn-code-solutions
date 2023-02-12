orders = input().split()
cost = 0
tax = 0.07
sum = 0

for num in range(len(orders)):
    if orders[num] == 'Nachos' or orders[num] == 'Pizza':
        cost = 6
        sum += cost
    elif orders[num] == 'Cheeseburger':
        cost = 10
        sum += cost
    elif orders[num] == 'Water':
        cost = 4
        sum += cost
    else:
        cost = 5
        sum += cost

sum = (tax * sum) + sum
print(sum)