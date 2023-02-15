value = int(input())
expressions = input().split()

for i in range (len(expressions)):
    if eval(expressions[i]) == value:
        print("Index " + str(i))
        break
    elif i == len(expressions) - 1 and eval(expressions[i]) != value:
        print("None")