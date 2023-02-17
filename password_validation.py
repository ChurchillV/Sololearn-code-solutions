#Taking input from the user
pwd = str(input("Enter Password for Validation: "))

#Pool of special characters
chars = ("!", "@", "#", "$", "%", "&", "*")

#Keeping track of digits and symbols
digit_count = 0
char_count = 0

#Iterating through each character in the password
for i in range(len(pwd)):
    if pwd[i].isdigit(): 
        digit_count += 1    #For every digit, digit_count increments by one

for i in range(len(pwd)):
    if pwd[i] in chars: 
        char_count += 1     #For every special symbol, char_count increments by one

if len(pwd) >= 7 and digit_count >= 2 and char_count >= 2: 
    print("Strong")
    """
    Provided there are at least 2 instances each of characters and digits,
    the password is validated as strong.
    Else, it's weak and you have to enter a new one.
    """

else:
    print("Weak! Try another password")     
