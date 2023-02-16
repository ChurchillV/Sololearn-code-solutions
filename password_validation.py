pwd = str(input("Enter Password for Validation: "))
chars = ("!", "@", "#", "$", "%", "&", "*")
digit_count = 0
char_count = 0

for i in range(len(pwd)):
    if pwd[i].isdigit():
        digit_count += 1

for i in range(len(pwd)):
    if pwd[i] in chars:
        char_count += 1

if len(pwd) >= 7 and digit_count >= 2 and char_count >= 2:
    print("Strong")

else:
    print("Weak! Try another password")     
