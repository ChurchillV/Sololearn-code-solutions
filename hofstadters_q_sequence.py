#The recursive Hofstadter's q-sequence function
def q_sequence(n):
    """
    The values of q_sequence(1) and q_sequence(2) are fixed as base cases.
    Every other integer above 2 has a q_sequence value given by 
    q_sequence(n- q_sequence(n-1)) + q_sequence(n - q_sequence(n-2))
    """
    if n == 1 or n == 2:
        return 1
    else:
        return q_sequence(n - q_sequence(n-1)) + q_sequence(n - q_sequence(n-2))
        #Recursion

n = int(input('Enter your value: '))
print(q_sequence(n))