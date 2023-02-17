ages = []

for num in range(3):
    ages.append(int(input()))

for i in range(len(ages)):
    if ages[i] < 16:
        print("Too young!")
        break
    elif i == len(ages) - 1 and ages[i] >= 16:
        print("Get ready!")
        
print(1+"1" == 2)