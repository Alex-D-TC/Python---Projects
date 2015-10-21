'''
Created on Oct 16, 2015

@author: Alex
'''
def get_word_count(string):
    """
        Returns the number of words in a string
        
        Input:
            - string - The string to validate
    """
    return len(string.split(sep = ' '))