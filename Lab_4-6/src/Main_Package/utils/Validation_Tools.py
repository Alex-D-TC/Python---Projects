'''
Created on Oct 14, 2015

@author: Alex
'''

def validate_int(n, min, max):
    """
        Checks if the given input is valid, and within the specified range
    """
    try: n = int(n)
    except : 
        return None
    if(n < min or n > max):
        print("Input outside of specified range")
        return None
    return n

def validate_index(sequence, index_start, index_end = -1):
    """
        Checks if the given indexes are valid.
        Fails if:
                - index_start < 0 or index_start > index_end
                - index_end > the length of the sequence
    """
    if(index_end == -1): index_end = len(sequence)
    if(index_start > index_end or index_start < 0 or index_end > len(sequence)):
        return False
    return True
