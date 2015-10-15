'''
Created on Oct 14, 2015

@author: Alex
'''

def validate_int(input_text, min, max):
    n = input(input_text)
    try: n = int(n)
    except : 
        print("Invalid input")
        return None
    if(n < min or n > max):
        print("Input outside of specified range")
        return None
    return n
