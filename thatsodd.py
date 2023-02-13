count = int(input())
sum = 0

for num in range(count):
    value = int(input())
    if value % 2 == 0:
        sum += value

print("The sum of even numbers is: " + str(sum))