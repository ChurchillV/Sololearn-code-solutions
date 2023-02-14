count = 0

for num in range(4):
    sign = input()

    count += 1
    if sign[::-1] == sign:
        print("Open")
        quit()
    elif count == 4:
        print("Trash")
