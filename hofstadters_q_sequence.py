#The recursive Hofstadter's q-sequence function
"""
    UPDATE
    To make the code more efficient in worst case scenarios, eg. q_sequence(1000),
    I'm adding memoisation. ALready-known q-sequence values will be assigned to their
    respective inputs. And new values will be saved for easy reference.
"""

memoisation = { 1:1, 2:1, 3:2, 4:3, 5:3, 6:4, 7:5, 8:5, 9:6, 10:6, 11:6 }

def q_sequence(n):
    """
    The values of q_sequence(1) and q_sequence(2) are fixed as base cases.
    Every other integer above 2 has a q_sequence value given by 
    q_sequence(n- q_sequence(n-1)) + q_sequence(n - q_sequence(n-2))
    """
    if n in memoisation:
        return memoisation[n]
    else:
        output = q_sequence(n - q_sequence(n-1)) + q_sequence(n - q_sequence(n-2))
        memoisation[n] = output
        return output

n = int(input('Enter your value: '))
print(q_sequence(n))