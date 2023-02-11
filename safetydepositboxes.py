items = input("Enter the items in each box in order: ").split(',')
goal = input("What are you looking for? ")
time = int(input("How long will it take to drill each box? "))
interval = time

for i in range(len(items)):
    if items[i] != goal:
        interval += time
    if items[i] == goal:
        print(str(interval) + " minutes" )


"""
    You're robbing a bank, but you're not taking everything. 
    You are looking for a specific item in the safety deposit
    boxes and you are going to drill into each one in order to
    find your item. Once you find your item, you can make your 
    escape. But how long will it take you to get that item?

    Task: 
        Determine the amount of time it will take you to find the
        item you are looking for if it takes you X minutes to drill 
        into each box.

    Input Format:
        A string representing the items in each box that will be drilled
        in order, and secondly, a string of which item you are looking 
        for. Finally, you must enter the time needed to drill one box

    Output Format:
        An integer of the amount of time it will take for you to find the item.
    
    Sample input:
        'gold, diamonds,documents,Declaration of independence,keys'
        'Declaration of independence'
        '5'
    
    Sample output:
        '20'
    """