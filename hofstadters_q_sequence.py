#The recursive Hofstadter's q-sequence function
def q_sequence(n):
    if n == 1 or n == 2:
        return 1
    else:
        return q_sequence(n - q_sequence(n-1)) + q_sequence(n - q_sequence(n-2))

n = int(input('Enter your value: '))
print(q_sequence(n))