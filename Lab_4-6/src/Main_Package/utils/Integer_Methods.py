'''
Created on Oct 16, 2015

@author: Alex
'''
def isPrime(value):
    """
        Checks if a given number is prime
    """
    if(value == 1 or value == -1): return False
    if(value % 2 == 0 and value != 2): return False
    for i in range(3, value//2 + 1, 2):
        if(value % i == 0):
            return False
    return True