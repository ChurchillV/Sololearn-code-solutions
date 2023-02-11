items = input().split(',')
goal = input()
time = 5

for i in range(len(items)):
    if items[i] != goal:
        time += 5
    if items[i] == goal:
        print(time)