print("Enter map values: \n")
our_map = input().upper()
test_map = our_map.split(',')
y_positions = []
x_positions = []

for x in range(len(test_map)):
    for y in range(len(test_map)):
        if test_map[x][y] == 'P':
            y_positions.append(y+1)
            x_positions.append(x+1)
total_steps = abs((y_positions[1] - y_positions[0])) + abs((x_positions[1] - x_positions[0]))
for i in range(len(test_map)):
    print(test_map[i])
print("Number of steps: " + str(total_steps))

'''
Premise:
You're given a representation of a 5 x 5 2D map and you can only move left, right, up or down.
Determine how many moves you would have to make to get between two points on the map.

Question:
Determine the total number of moves needed to move between 2 points on the map.The points marked P
are those which you move between and those marked X are the spaces in between.

Representation:
    Map:
    XPXXX
    XXXXX
    XXXXX
    XXXXX
    XXXPX

    Number of steps: 6

Sample input:
    XPXXX,XXXXX,XXXXX,XXXXX,XXXPX
'''